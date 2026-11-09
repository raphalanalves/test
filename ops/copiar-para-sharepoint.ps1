# Copia os posts do GitHub para a pasta do SharePoint "Malvora Marketing" sincronizada pelo OneDrive.
# Uso: powershell -ExecutionPolicy Bypass -File copiar-para-sharepoint.ps1
$ErrorActionPreference = "Stop"
$base = "https://raw.githubusercontent.com/raphalanalves/test/master/conteudo"
$raiz = Get-ChildItem $env:USERPROFILE -Directory -Recurse -Depth 2 -ErrorAction SilentlyContinue |
  Where-Object { $_.Name -like "Malvora Marketing*Documentos*" -or $_.Name -like "Documentos*Malvora Marketing*" } | Select-Object -First 1
if (-not $raiz) { throw "Pasta sincronizada do Malvora Marketing não encontrada. Clique em Sincronizar na biblioteca Documentos do site." }
$ig = Join-Path $raiz.FullName "Instagram"
$itens = @(
  @{ pasta = "02 Aprovados e agendados\2026-11-09 09h Story contagem"; arquivos = @("stories-lancamento/story-contagem-09-11.jpg") },
  @{ pasta = "02 Aprovados e agendados\2026-11-10 00h05 Reel V15 Tres buracos"; arquivos = @("v15-tres-buracos/v15-tres-buracos.mp4") },
  @{ pasta = "02 Aprovados e agendados\2026-11-10 12h Carrossel 30 negocios"; arquivos = (1..7 | ForEach-Object { "lancamento-2026-11-10/carrossel-30-negocios/c30-0$_.jpg" }) },
  @{ pasta = "02 Aprovados e agendados\2026-11-11 19h Reel V16 Qual IA"; arquivos = @("v16-qual-ia/v16-qual-ia.mp4") },
  @{ pasta = "02 Aprovados e agendados\2026-11-10 18h Reel O que a Malvora faz"; arquivos = @("lancamento-2026-11-10/reel-o-que-faz/reel-o-que-a-malvora-faz.mp4") },
  @{ pasta = "01 Aguardando aprovação\Carrossel 10 segundos"; arquivos = (1..7 | ForEach-Object { "lancamento-2026-11-10/carrossel-10-segundos/c10-0$_.jpg" }) + @("lancamento-2026-11-10/carrossel-10-segundos/legenda.txt") },
  @{ pasta = "01 Aguardando aprovação\Anuncio salao 00h38"; arquivos = @("anuncios/salao-00h38/anuncio-0038-salao.mp4") },
  @{ pasta = "01 Aguardando aprovação\Por dentro da Malvora (previa)"; arquivos = @("portal-por-dentro/reels/previa-sem-voz.mp4") }
)
foreach ($i in $itens) {
  $destino = Join-Path $ig $i.pasta
  New-Item -ItemType Directory -Force -Path $destino | Out-Null
  foreach ($a in $i.arquivos) {
    $arq = Join-Path $destino (Split-Path $a -Leaf)
    Invoke-WebRequest -Uri "$base/$a" -OutFile $arq -UseBasicParsing
    "{0,8:N0} KB  {1}" -f ((Get-Item $arq).Length / 1KB), $arq
  }
}
"Pronto. Confira no SharePoint em alguns minutos (o OneDrive envia sozinho)."
