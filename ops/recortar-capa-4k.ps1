# Recorta em 4K os 2 trechos curtos usados na CAPA do Ep. 01 (Pablo sorrindo para a câmera)
# e envia ao repositório PRIVADO raphalanalves/malvora-entrevista-tmp (pasta hires/). NÃO altera os originais.
# Uso: powershell -ExecutionPolicy Bypass -File recortar-capa-4k.ps1
$ErrorActionPreference = "Stop"
$raiz = Get-ChildItem $env:USERPROFILE -Directory -Recurse -Depth 2 -ErrorAction SilentlyContinue |
  Where-Object { $_.Name -like "Malvora Marketing*Documentos*" } | Select-Object -First 1
if (-not $raiz) { throw "Pasta sincronizada do Malvora Marketing não encontrada." }
$src = Join-Path $raiz.FullName "01 Conteúdo orgânico\Séries\Entrevistas VIP\IMG_3036.mov"
if (-not (Test-Path $src)) { throw "IMG_3036.mov não encontrado em $src" }
$repo = Join-Path $env:USERPROFILE "malvora-entrevista-tmp"
if (-not (Test-Path (Join-Path $repo ".git"))) { throw "Clone do repositório não encontrado em $repo." }
git -C $repo pull -q
$out = Join-Path $repo "hires"; New-Item -ItemType Directory -Force -Path $out | Out-Null
$null = Get-Content -Path $src -TotalCount 1 -Encoding Byte   # força o download do OneDrive
foreach ($t in @(@("2.00","3.00"), @("876.50","3.00"))) {
  $dst = Join-Path $out ("N07_IMG_3036__{0}.mp4" -f $t[0])
  & cmd /c "ffmpeg -nostdin -y -loglevel error -ss $($t[0]) -i ""$src"" -t $($t[1]) -c:v libx264 -preset medium -crf 14 -pix_fmt yuv420p -r 30 -an -movflags +faststart ""$dst"""
  "ok  $(Split-Path $dst -Leaf)  ($([math]::Round((Get-Item $dst).Length/1MB,1)) MB)"
}
git -C $repo add hires; git -C $repo commit -q -m "hires: trechos da capa (Pablo)"; git -C $repo push -q
"Pronto: 2 trechos da capa enviados para raphalanalves/malvora-entrevista-tmp/hires"
