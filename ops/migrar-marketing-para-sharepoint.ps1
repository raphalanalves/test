# Etapa 1 da migração: COPIA o material de marketing do GitHub para o SharePoint "Malvora Marketing" (pasta sincronizada pelo OneDrive).
# Não apaga nada no GitHub nem no SharePoint. Arquivos que já existem no destino são mantidos (não sobrescreve).
# Uso: powershell -ExecutionPolicy Bypass -File migrar-marketing-para-sharepoint.ps1
$ErrorActionPreference = "Stop"
$raiz = Get-ChildItem $env:USERPROFILE -Directory -Recurse -Depth 2 -ErrorAction SilentlyContinue |
  Where-Object { $_.Name -like "Malvora Marketing*Documentos*" } | Select-Object -First 1
if (-not $raiz) { throw "Pasta sincronizada do Malvora Marketing não encontrada." }
$R = $raiz.FullName
$tmp = Join-Path $env:TEMP "malvora-git"
$zip = Join-Path $env:TEMP "malvora-git.zip"
"Baixando o repositório (cerca de 500 MB)..."
Invoke-WebRequest -Uri "https://codeload.github.com/raphalanalves/test/zip/refs/heads/master" -OutFile $zip -UseBasicParsing
if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force }
Expand-Archive -Path $zip -DestinationPath $tmp
$C = Join-Path (Get-ChildItem $tmp -Directory | Select-Object -First 1).FullName "conteudo"
$copiados = 0; $mantidos = 0
function Copiar($origem, $destinoPasta) {
  New-Item -ItemType Directory -Force -Path $destinoPasta | Out-Null
  $alvo = Join-Path $destinoPasta (Split-Path $origem -Leaf)
  if (Test-Path $alvo) { $script:mantidos++ } else { Copy-Item $origem $alvo; $script:copiados++ }
}
function CopiarPasta($origemPasta, $destinoPasta) {
  Get-ChildItem $origemPasta -Recurse -File | Where-Object { $_.FullName -notmatch '\\_fonte\\' } | ForEach-Object {
    $rel = $_.DirectoryName.Substring($origemPasta.Length).TrimStart('\')
    Copiar $_.FullName (Join-Path $destinoPasta $rel)
  }
}
# 1) Publicados, um post por pasta, com o link
$publicados = @(
  @{ pasta = "2026-10\2026-10-31 20h00 Vinheta da logo"; link = "https://www.instagram.com/reel/DfLSf4bDzoA/"; arquivos = @("lancamento-2026-11-10/vinheta-logo/vinheta-logo.mp4") }
  @{ pasta = "2026-10\2026-10-31 20h05 Mosaico 3 de 3 (direita)"; link = "https://www.instagram.com/p/DfLTC63keI8/"; arquivos = @("lancamento-2026-11-10/mosaico/tile-3-direita.jpg") }
  @{ pasta = "2026-10\2026-10-31 20h06 Mosaico 2 de 3 (centro)"; link = "https://www.instagram.com/p/DfLTKPvEXT6/"; arquivos = @("lancamento-2026-11-10/mosaico/tile-2-centro.jpg") }
  @{ pasta = "2026-10\2026-10-31 20h07 Mosaico 1 de 3 (esquerda)"; link = "https://www.instagram.com/p/DfLTRg6EV8_/"; arquivos = @("lancamento-2026-11-10/mosaico/tile-1-esquerda.jpg") }
  @{ pasta = "2026-11\2026-11-01 20h00 Reel Revelacao da logo"; link = "https://www.instagram.com/reel/DfN3Ws9CFIR/"; arquivos = @("lancamento-2026-11-10/revelacao-logo/revelacao-logo.mp4") }
  @{ pasta = "2026-11\2026-11-02 18h00 Carrossel Quem respondeu"; link = "https://www.instagram.com/p/DfQOVqMn_2r/"; arquivos = @("2026-10-semana-12-18/v2/carrossel-01-quem-respondeu-01.jpg", "2026-10-semana-12-18/v2/carrossel-01-quem-respondeu-02.jpg", "2026-10-semana-12-18/v2/carrossel-01-quem-respondeu-03.jpg", "2026-10-semana-12-18/v2/carrossel-01-quem-respondeu-04.jpg", "2026-10-semana-12-18/v2/carrossel-01-quem-respondeu-05.jpg", "2026-10-semana-12-18/v2/carrossel-01-quem-respondeu-06.jpg") }
  @{ pasta = "2026-11\2026-11-03 09h00 Story contagem 7 dias"; link = "https://www.instagram.com/stories/malvora_hub/4022230478983637825"; arquivos = @("stories-lancamento/story-contagem-03-11.jpg") }
  @{ pasta = "2026-11\2026-11-03 18h00 Reel V7 Hexagonos"; link = "https://www.instagram.com/reel/DfSzIefAm98/"; arquivos = @("v07-hexagonos/v07-hexagonos-carla.mp4") }
  @{ pasta = "2026-11\2026-11-04 09h00 Story contagem 6 dias"; link = "https://www.instagram.com/stories/malvora_hub/4022955254849071205"; arquivos = @("stories-lancamento/story-contagem-04-11.jpg") }
  @{ pasta = "2026-11\2026-11-04 12h00 Reel 00h38"; link = "https://www.instagram.com/reel/DfUuubfEprD/"; arquivos = @("2026-10-semana-12-18/reel-01-0038.mp4") }
  @{ pasta = "2026-11\2026-11-05 09h00 Story contagem 5 dias"; link = "https://www.instagram.com/stories/malvora_hub/4023680029682674043"; arquivos = @("stories-lancamento/story-contagem-05-11.jpg") }
  @{ pasta = "2026-11\2026-11-05 12h00 Carrossel 4 mitos"; link = "https://www.instagram.com/p/DfXThvaESON/"; arquivos = @("2026-10-semana-12-18/v2/carrossel-02-mitos-01.jpg", "2026-10-semana-12-18/v2/carrossel-02-mitos-02.jpg", "2026-10-semana-12-18/v2/carrossel-02-mitos-03.jpg", "2026-10-semana-12-18/v2/carrossel-02-mitos-04.jpg", "2026-10-semana-12-18/v2/carrossel-02-mitos-05.jpg", "2026-10-semana-12-18/v2/carrossel-02-mitos-06.jpg") }
  @{ pasta = "2026-11\2026-11-06 09h00 Story contagem 4 dias"; link = "https://www.instagram.com/stories/malvora_hub/4024404813391420307"; arquivos = @("stories-lancamento/story-contagem-06-11.jpg") }
  @{ pasta = "2026-11\2026-11-06 19h00 Reel Revelacao dos 50"; link = "https://www.instagram.com/reel/DfaobfdDBQn/"; arquivos = @("lancamento-2026-11-10/revelacao-50/revelacao-50.mp4") }
  @{ pasta = "2026-11\2026-11-07 09h00 Story contagem 3 dias"; link = "https://www.instagram.com/stories/malvora_hub/4025129585171617683"; arquivos = @("stories-lancamento/story-contagem-07-11.jpg") }
  @{ pasta = "2026-11\2026-11-07 11h00 Reel V13 Quanto custa 40"; link = "https://www.instagram.com/reel/DfcWP48HKeU/"; arquivos = @("v13-chama-o-gerente/v13-quanto-custa-40.mp4") }
  @{ pasta = "2026-11\2026-11-08 09h00 Story contagem 2 dias"; link = "https://www.instagram.com/stories/malvora_hub/4025854359837431832"; arquivos = @("stories-lancamento/story-contagem-08-11.jpg") }
  @{ pasta = "2026-11\2026-11-08 19h00 Reel Alquimias 1"; link = "https://www.instagram.com/reel/Dffx-E0ETqn/"; arquivos = @("alquimias-01/alquimias-01-carla.mp4") }
)
foreach ($p in $publicados) {
  $dest = Join-Path $R ("Instagram\03 Publicados\" + $p.pasta)
  foreach ($a in $p.arquivos) { Copiar (Join-Path $C ($a -replace '/','\')) $dest }
  $l = Join-Path $dest "link.txt"; if (-not (Test-Path $l)) { $p.link | Set-Content -Path $l -Encoding UTF8 }
}
"Publicados: ok"
# 2) Marca, anúncios e vozes
foreach ($m in @("marca","perfil","destaques")) { if (Test-Path (Join-Path $C $m)) { CopiarPasta (Join-Path $C $m) (Join-Path $R "Marca\$m") } }
$me = Join-Path (Split-Path $C) "marca-email"; if (Test-Path $me) { CopiarPasta $me (Join-Path $R "Marca\e-mail") }
if (Test-Path (Join-Path $C "anuncios")) { CopiarPasta (Join-Path $C "anuncios") (Join-Path $R "Anúncios") }
foreach ($v in @("vozes-teste","vozes-teste-v4","vozes-amostras")) { if (Test-Path (Join-Path $C $v)) { CopiarPasta (Join-Path $C $v) (Join-Path $R "Brutos\Vozes\$v") } }
"Marca, anúncios e vozes: ok"
# 3) Acervo completo do git (cópia de segurança de tudo, sem os arquivos-fonte)
CopiarPasta $C (Join-Path $R "Brutos\Acervo do git (09-11-2026)")
"Acervo: ok"
Remove-Item $zip -Force; Remove-Item $tmp -Recurse -Force
"Pronto. Copiados: $copiados · já existiam (mantidos): $mantidos. O OneDrive envia ao SharePoint em segundo plano."
