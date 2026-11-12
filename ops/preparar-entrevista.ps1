# Gera cópias leves (proxies) das gravações da entrevista e um manifesto, e envia para o repositório PRIVADO
# temporário raphalanalves/malvora-entrevista-tmp, para o Claude assistir, sincronizar as câmeras e montar a edição.
# NÃO altera, move nem apaga os vídeos originais. As cópias ficam fora da pasta do OneDrive.
# Uso: powershell -ExecutionPolicy Bypass -File preparar-entrevista.ps1 [-Pasta "subpasta"] [-Prefixo "N"] [-Saida "proxies-nycole"]
param([string]$Pasta = "03 Brutos e gravações\Gravações", [string]$Prefixo = "", [string]$Saida = "proxies")
$ErrorActionPreference = "Stop"
$raiz = Get-ChildItem $env:USERPROFILE -Directory -Recurse -Depth 2 -ErrorAction SilentlyContinue |
  Where-Object { $_.Name -like "Malvora Marketing*Documentos*" } | Select-Object -First 1
if (-not $raiz) { throw "Pasta sincronizada do Malvora Marketing não encontrada." }
$src = Join-Path $raiz.FullName $Pasta
if (-not (Test-Path $src)) { throw "Pasta não encontrada: $src" }
$repo = Join-Path $env:USERPROFILE "malvora-entrevista-tmp"
if (-not (Test-Path (Join-Path $repo ".git"))) {
  if (Test-Path $repo) { throw "A pasta $repo existe mas não é um clone do repositório. Apague-a (com o ok do Raphael) e rode de novo." }
  git clone https://github.com/raphalanalves/malvora-entrevista-tmp.git $repo
  if (-not (Test-Path (Join-Path $repo ".git"))) { throw "Não consegui clonar o repositório (login do git?). Nada foi enviado." }
}
git -C $repo pull -q
$px = Join-Path $repo $Saida; New-Item -ItemType Directory -Force -Path $px | Out-Null
$ErrorActionPreference = "Continue"
$linhas = @("arquivo;proxy;duracao_s;largura;altura;rotacao;fps;criado_em;aparelho;tamanho_mb")
$n = 0
Get-ChildItem $src -File | Where-Object { $_.Extension -match '^\.(mov|mp4|m4v)$' } | Sort-Object Name | ForEach-Object {
  $f = $_.FullName; $n++
  $null = Get-Content -Path $f -TotalCount 1 -Encoding Byte   # força o download do OneDrive
  $j = (& ffprobe -v error -print_format json -show_format -show_streams "$f") | ConvertFrom-Json
  $v = $j.streams | Where-Object { $_.codec_type -eq "video" } | Select-Object -First 1
  $t = $j.format.tags
  $aparelho = @($t.'com.apple.quicktime.model', $t.'com.android.manufacturer', $t.'com.android.model', $t.model, $t.make) -ne $null -join ' '
  $criado = @($t.'com.apple.quicktime.creationdate', $t.creation_time) -ne $null | Select-Object -First 1
  $rot = if ($v.side_data_list) { ($v.side_data_list | Where-Object { $_.rotation -ne $null } | Select-Object -First 1).rotation } else { $v.tags.rotate }
  $nome = "{0}{1:D2}_{2}.mp4" -f $Prefixo, $n, $_.BaseName
  $out = Join-Path $px $nome
  if ((Test-Path $out) -and ((Get-Item $out).Length -lt 20KB)) { Remove-Item $out }   # cópia incompleta de uma tentativa anterior
  if (-not (Test-Path $out)) {
    # lado maior 960 px, H.264 leve, áudio mono 96 kbps (mantém o áudio para sincronizar as câmeras)
    & cmd /c "ffmpeg -nostdin -y -loglevel error -i ""$f"" -vf ""scale='if(gt(iw,ih),960,-2)':'if(gt(iw,ih),-2,960)'"" -c:v libx264 -preset veryfast -crf 30 -c:a aac -b:a 96k -ac 1 -ar 48000 -movflags +faststart ""$out"""
    if ((Get-Item $out).Length -gt 95MB) {
      & cmd /c "ffmpeg -nostdin -y -loglevel error -i ""$f"" -vf ""scale='if(gt(iw,ih),720,-2)':'if(gt(iw,ih),-2,720)'"" -c:v libx264 -preset veryfast -crf 34 -c:a aac -b:a 64k -ac 1 -ar 48000 -movflags +faststart ""$out"""
    }
  }
  $linhas += "{0};{1};{2};{3};{4};{5};{6};{7};{8};{9}" -f $_.Name, $nome, [math]::Round([double]$j.format.duration,2), $v.width, $v.height, $rot, $v.r_frame_rate, $criado, $aparelho, [math]::Round($_.Length/1MB,1)
  "ok  $nome"
  # envia de 4 em 4 para não ficar um push gigante
  if ($n % 4 -eq 0) { git -C $repo add $Saida; git -C $repo commit -q -m "proxies ate $n"; git -C $repo push -q }
}
$linhas | Set-Content -Path (Join-Path $repo ("manifesto" + $(if ($Prefixo) { "-$Prefixo" } else { "" }) + ".csv")) -Encoding UTF8
git -C $repo add -A; git -C $repo commit -q -m "proxies e manifesto ($n videos)"; git -C $repo push -q
"Pronto: $n vídeos enviados para raphalanalves/malvora-entrevista-tmp"
