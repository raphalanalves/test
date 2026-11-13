# Recorta em 4K só os trechos usados na edição aprovada da entrevista e envia ao repositório PRIVADO
# raphalanalves/malvora-entrevista-tmp (pasta hires/). NÃO altera nem apaga os originais.
# Uso: powershell -ExecutionPolicy Bypass -File recortar-4k.ps1
$ErrorActionPreference = "Stop"
$raiz = Get-ChildItem $env:USERPROFILE -Directory -Recurse -Depth 2 -ErrorAction SilentlyContinue |
  Where-Object { $_.Name -like "Malvora Marketing*Documentos*" } | Select-Object -First 1
if (-not $raiz) { throw "Pasta sincronizada do Malvora Marketing não encontrada." }
$pastas = @{ "Entrevistas VIP" = "01 Conteúdo orgânico\Séries\Entrevistas VIP"; "Gravações" = "03 Brutos e gravações\Gravações" }
$repo = Join-Path $env:USERPROFILE "malvora-entrevista-tmp"
if (-not (Test-Path (Join-Path $repo ".git"))) { throw "Clone do repositório não encontrado em $repo." }
git -C $repo pull -q
$out = Join-Path $repo "hires"; New-Item -ItemType Directory -Force -Path $out | Out-Null
$seg = @'
[
{
"proxy": "N08_IMG_3037.mp4",
"original": "IMG_3037.mov",
"pasta": "Entrevistas VIP",
"ss": 114.48,
"d": 6.42,
"nome": "N08_IMG_3037__114.48.mp4"
},
{
"proxy": "N08_IMG_3037.mp4",
"original": "IMG_3037.mov",
"pasta": "Entrevistas VIP",
"ss": 160.44,
"d": 4.46,
"nome": "N08_IMG_3037__160.44.mp4"
},
{
"proxy": "N08_IMG_3037.mp4",
"original": "IMG_3037.mov",
"pasta": "Entrevistas VIP",
"ss": 175.67,
"d": 8.43,
"nome": "N08_IMG_3037__175.67.mp4"
},
{
"proxy": "23_20261107_200041000_iOS.mp4",
"original": "20261107_200041000_iOS.MOV",
"pasta": "Gravações",
"ss": 0,
"d": 2.77,
"nome": "23_20261107_200041000_iOS__0.00.mp4"
},
{
"proxy": "N04_IMG_3015.mp4",
"original": "IMG_3015.mov",
"pasta": "Entrevistas VIP",
"ss": 1.0,
"d": 4.3,
"nome": "N04_IMG_3015__1.00.mp4"
},
{
"proxy": "N04_IMG_3015.mp4",
"original": "IMG_3015.mov",
"pasta": "Entrevistas VIP",
"ss": 7.0,
"d": 4.0,
"nome": "N04_IMG_3015__7.00.mp4"
},
{
"proxy": "N04_IMG_3015.mp4",
"original": "IMG_3015.mov",
"pasta": "Entrevistas VIP",
"ss": 13.0,
"d": 4.4,
"nome": "N04_IMG_3015__13.00.mp4"
},
{
"proxy": "N04_IMG_3015.mp4",
"original": "IMG_3015.mov",
"pasta": "Entrevistas VIP",
"ss": 19.0,
"d": 4.0,
"nome": "N04_IMG_3015__19.00.mp4"
},
{
"proxy": "N04_IMG_3015.mp4",
"original": "IMG_3015.mov",
"pasta": "Entrevistas VIP",
"ss": 25.0,
"d": 4.72,
"nome": "N04_IMG_3015__25.00.mp4"
},
{
"proxy": "N05_IMG_3021.mp4",
"original": "IMG_3021.mov",
"pasta": "Entrevistas VIP",
"ss": 1.5,
"d": 7.7,
"nome": "N05_IMG_3021__1.50.mp4"
},
{
"proxy": "10_20261107_194957000_iOS.mp4",
"original": "20261107_194957000_iOS.MOV",
"pasta": "Gravações",
"ss": 0,
"d": 3.5,
"nome": "10_20261107_194957000_iOS__0.00.mp4"
},
{
"proxy": "N06_IMG_3023.mp4",
"original": "IMG_3023.mov",
"pasta": "Entrevistas VIP",
"ss": 3.0,
"d": 4.4,
"nome": "N06_IMG_3023__3.00.mp4"
},
{
"proxy": "N06_IMG_3023.mp4",
"original": "IMG_3023.mov",
"pasta": "Entrevistas VIP",
"ss": 13.0,
"d": 4.0,
"nome": "N06_IMG_3023__13.00.mp4"
},
{
"proxy": "N06_IMG_3023.mp4",
"original": "IMG_3023.mov",
"pasta": "Entrevistas VIP",
"ss": 29.0,
"d": 3.38,
"nome": "N06_IMG_3023__29.00.mp4"
},
{
"proxy": "N11_IMG_3043.mp4",
"original": "IMG_3043.mov",
"pasta": "Entrevistas VIP",
"ss": 125.59,
"d": 7.99,
"nome": "N11_IMG_3043__125.59.mp4"
},
{
"proxy": "N07_IMG_3036.mp4",
"original": "IMG_3036.mov",
"pasta": "Entrevistas VIP",
"ss": 173.53,
"d": 7.51,
"nome": "N07_IMG_3036__173.53.mp4"
},
{
"proxy": "N07_IMG_3036.mp4",
"original": "IMG_3036.mov",
"pasta": "Entrevistas VIP",
"ss": 329.7,
"d": 6.58,
"nome": "N07_IMG_3036__329.70.mp4"
},
{
"proxy": "N07_IMG_3036.mp4",
"original": "IMG_3036.mov",
"pasta": "Entrevistas VIP",
"ss": 681.9,
"d": 13.8,
"nome": "N07_IMG_3036__681.90.mp4"
},
{
"proxy": "N07_IMG_3036.mp4",
"original": "IMG_3036.mov",
"pasta": "Entrevistas VIP",
"ss": 924.52,
"d": 6.94,
"nome": "N07_IMG_3036__924.52.mp4"
},
{
"proxy": "N07_IMG_3036.mp4",
"original": "IMG_3036.mov",
"pasta": "Entrevistas VIP",
"ss": 990.08,
"d": 4.03,
"nome": "N07_IMG_3036__990.08.mp4"
},
{
"proxy": "35_20261107_205758000_iOS.mp4",
"original": "20261107_205758000_iOS.MOV",
"pasta": "Gravações",
"ss": 13.81,
"d": 4.99,
"nome": "35_20261107_205758000_iOS__13.81.mp4"
},
{
"proxy": "N03_IMG_3014.mp4",
"original": "IMG_3014.mov",
"pasta": "Entrevistas VIP",
"ss": 8.0,
"d": 4.23,
"nome": "N03_IMG_3014__8.00.mp4"
},
{
"proxy": "N03_IMG_3014.mp4",
"original": "IMG_3014.mov",
"pasta": "Entrevistas VIP",
"ss": 15.0,
"d": 5.48,
"nome": "N03_IMG_3014__15.00.mp4"
},
{
"proxy": "39_20261107_210621000_iOS.mp4",
"original": "20261107_210621000_iOS.MOV",
"pasta": "Gravações",
"ss": 18.79,
"d": 9.38,
"nome": "39_20261107_210621000_iOS__18.79.mp4"
},
{
"proxy": "41_20261107_211033000_iOS.mp4",
"original": "20261107_211033000_iOS.MOV",
"pasta": "Gravações",
"ss": 9.41,
"d": 4.53,
"nome": "41_20261107_211033000_iOS__9.41.mp4"
},
{
"proxy": "N09_IMG_3038.mp4",
"original": "IMG_3038.mov",
"pasta": "Entrevistas VIP",
"ss": 508.8,
"d": 10.0,
"nome": "N09_IMG_3038__508.80.mp4"
},
{
"proxy": "N09_IMG_3038.mp4",
"original": "IMG_3038.mov",
"pasta": "Entrevistas VIP",
"ss": 565.75,
"d": 10.97,
"nome": "N09_IMG_3038__565.75.mp4"
},
{
"proxy": "N10_IMG_3042.mp4",
"original": "IMG_3042.mov",
"pasta": "Entrevistas VIP",
"ss": 10.14,
"d": 4.19,
"nome": "N10_IMG_3042__10.14.mp4"
}
]
'@ | ConvertFrom-Json
$ErrorActionPreference = "Continue"
$n = 0
foreach ($s in $seg) {
  $n++
  $src = Join-Path (Join-Path $raiz.FullName $pastas[$s.pasta]) $s.original
  if (-not (Test-Path $src)) { "FALTA  $($s.original)"; continue }
  $null = Get-Content -Path $src -TotalCount 1 -Encoding Byte   # força o download do OneDrive
  $dst = Join-Path $out $s.nome
  if ((Test-Path $dst) -and ((Get-Item $dst).Length -gt 200KB)) { "ja ok  $($s.nome)"; continue }
  $ss = [string]::Format([Globalization.CultureInfo]::InvariantCulture, "{0:0.00}", [double]$s.ss)
  $d  = [string]::Format([Globalization.CultureInfo]::InvariantCulture, "{0:0.00}", [double]$s.d)
  & cmd /c "ffmpeg -nostdin -y -loglevel error -ss $ss -i ""$src"" -t $d -c:v libx264 -preset medium -crf 17 -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -ar 48000 -movflags +faststart ""$dst"""
  if ((Get-Item $dst).Length -gt 95MB) {
    & cmd /c "ffmpeg -nostdin -y -loglevel error -ss $ss -i ""$src"" -t $d -c:v libx264 -preset medium -crf 21 -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -ar 48000 -movflags +faststart ""$dst"""
  }
  "ok  $($s.nome)  ($([math]::Round((Get-Item $dst).Length/1MB,1)) MB)"
  if ($n % 4 -eq 0) { git -C $repo add hires; git -C $repo commit -q -m "hires ate $n"; git -C $repo push -q }
}
git -C $repo add hires; git -C $repo commit -q -m "hires ($n trechos)"; git -C $repo push -q
"Pronto: $n trechos em 4K enviados para raphalanalves/malvora-entrevista-tmp/hires"
