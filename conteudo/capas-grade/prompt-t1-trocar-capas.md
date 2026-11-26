# Prompt para o T1: trocar as capas dos Reels no Instagram (Chrome)

```
Você vai trocar a CAPA de 12 Reels do perfil https://www.instagram.com/malvora_hub/ no Chrome, onde a conta já está logada.

Regras de segurança:
- Não digite senha nem código 2FA. Se pedir login, pare e me peça.
- Só troque a capa. Não altere legenda, local, marcações, áudio nem configurações; não arquive nem apague nada.
- Faça um Reel por vez e confira na grade antes de passar para o próximo.
- Não troque a capa de: "Bastidores de uma tarde de gravação" (DfnIbZJFGaT) e "O 40º quanto custa?" (DfcWP48HKeU).
- Se o Instagram no navegador não tiver a opção de editar a capa de um Reel já publicado, PARE e me avise. Não tente outro jeito.

Passo 1: baixe as capas para a pasta ~/Downloads/capas-malvora:
mkdir -p ~/Downloads/capas-malvora && cd ~/Downloads/capas-malvora
curl -sLO https://raw.githubusercontent.com/raphalanalves/test/master/conteudo/capas-grade/capa-2026-10-31-DfLSf4bDzoA.jpg
curl -sLO https://raw.githubusercontent.com/raphalanalves/test/master/conteudo/capas-grade/capa-2026-11-01-DfN3Ws9CFIR.jpg
curl -sLO https://raw.githubusercontent.com/raphalanalves/test/master/conteudo/capas-grade/capa-2026-11-03-DfSzIefAm98.jpg
curl -sLO https://raw.githubusercontent.com/raphalanalves/test/master/conteudo/capas-grade/capa-2026-11-04-DfUuubfEprD.jpg
curl -sLO https://raw.githubusercontent.com/raphalanalves/test/master/conteudo/capas-grade/capa-2026-11-06-DfaobfdDBQn.jpg
curl -sLO https://raw.githubusercontent.com/raphalanalves/test/master/conteudo/capas-grade/capa-2026-11-08-Dffx-E0ETqn.jpg
curl -sLO https://raw.githubusercontent.com/raphalanalves/test/master/conteudo/capas-grade/capa-2026-11-10a-Dfi5q4wjATD.jpg
curl -sLO https://raw.githubusercontent.com/raphalanalves/test/master/conteudo/capas-grade/capa-2026-11-10b-Dfj25RJEdD9.jpg
curl -sLO https://raw.githubusercontent.com/raphalanalves/test/master/conteudo/capas-grade/capa-2026-11-10c-Dfk0sViiURg.jpg
curl -sLO https://raw.githubusercontent.com/raphalanalves/test/master/conteudo/capas-grade/capa-2026-11-11b-Dfngbp4mbXn.jpg
curl -sLO https://raw.githubusercontent.com/raphalanalves/test/master/conteudo/capas-grade/capa-2026-11-14a-DfuerJRJdF_.jpg
curl -sLO https://raw.githubusercontent.com/raphalanalves/test/master/conteudo/capas-grade/capa-2026-11-14b-DfvOvT1EuiX.jpg
ls | wc -l   (tem que dar 12)

Passo 2: para cada arquivo, o código no fim do nome é o Reel: capa-<data>-<CÓDIGO>.jpg → https://www.instagram.com/reel/<CÓDIGO>/
1. Abra o link do Reel no Chrome.
2. Menu ⋯ › Editar (ou "Editar capa", se aparecer).
3. Escolha "Enviar da galeria/computador" (não escolha um quadro do vídeo) e selecione o arquivo certo.
4. Se pedir o recorte da grade (perfil), deixe centralizado, sem zoom.
5. Salve/Concluir e confira na grade do perfil.

Passo 3: relatório no fim, uma linha por Reel: código, trocada (sim/não), observação. E a confirmação:
"Nenhuma legenda, áudio ou post foi alterado além das capas."
```
