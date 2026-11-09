# Gera folhas de contato (12 quadros) e dados de áudio de cada vídeo de Brutos\Gravações, em Brutos\Gravações\_analise.
# Não altera nem apaga os vídeos originais.
$ErrorActionPreference = "Stop"
$raiz = Get-ChildItem $env:USERPROFILE -Directory -Recurse -Depth 2 -ErrorAction SilentlyContinue |
  Where-Object { $_.Name -like "Malvora Marketing*Documentos*" } | Select-Object -First 1
if (-not $raiz) { throw "Pasta sincronizada do Malvora Marketing não encontrada." }
$src = Join-Path $raiz.FullName "Brutos\Gravações"
$out = Join-Path $src "_analise"
New-Item -ItemType Directory -Force -Path $out | Out-Null
$linhas = @("arquivo;duracao_s;largura;altura;volume_medio_db;trechos_com_som_s")
Get-ChildItem $src -File | Where-Object { $_.Extension -match '^\.(mov|mp4)$' } | Sort-Object Name | ForEach-Object {
  $f = $_.FullName; $base = $_.BaseName
  # força o download do OneDrive (arquivo sob demanda)
  $null = Get-Content -Path $f -TotalCount 1 -Encoding Byte
  $dur = [double](& ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  $wh = (& ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$f") -split ','
  $fps = [math]::Round(12 / [math]::Max($dur, 1), 4)
  & ffmpeg -nostdin -y -loglevel error -i "$f" -vf "fps=$fps,scale=360:-2,tile=4x3:padding=6:color=black" -frames:v 1 -q:v 4 (Join-Path $out "$base.jpg")
  $vol = (& ffmpeg -nostdin -i "$f" -vn -af volumedetect -f null - 2>&1 | Select-String "mean_volume").ToString() -replace '.*mean_volume: ([-\d\.]+) dB.*','$1'
  $sil = (& ffmpeg -nostdin -i "$f" -vn -af silencedetect=n=-40dB:d=1 -f null - 2>&1 | Select-String "silence_duration") |
    ForEach-Object { [double]($_.ToString() -replace '.*silence_duration: ([\d\.]+).*','$1') } | Measure-Object -Sum
  $som = [math]::Round($dur - $sil.Sum, 1)
  $linhas += "{0};{1};{2};{3};{4};{5}" -f $_.Name, [math]::Round($dur,1), $wh[0], $wh[1], $vol, $som
  "ok  $($_.Name)  ($([math]::Round($dur,1)) s)"
}
$linhas | Set-Content -Path (Join-Path $out "resumo.csv") -Encoding UTF8
"Pronto: $out"
