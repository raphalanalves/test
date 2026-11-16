# Plano · Rodada 2 de anúncios · Salão de beleza e barbearia (rascunho para aprovação)

Skill: meta-ads-malvora. Base: leitura da rodada 1 (`../barbearia-cupom/leitura-2026-11-15.md`).
**Pré-requisito (bloqueante):** cupom visível no `/assinar` (pedido de alta prioridade ao Jão, 15/11). Sem isso, não
recarregar nem publicar.

## O que a rodada 1 ensinou
| Achado | Número | Decisão |
|---|---|---|
| Anúncio gera clique | CTR 2,22% | manter a oferta (cupom) e o destino (direct) |
| Stories é o posicionamento mais barato | R$ 4,63 por conversa (Feed R$ 16,02) | Stories primeiro; Feed fora |
| Reels quase não gera clique | CTR 0,42% | Reels só com criativo de 15–20 s |
| 45–54 anos converte mais barato | R$ 4,20 por conversa | 25–54; 55+ fora |
| Ninguém disse o ramo | 0 de 4 | mensagem pronta já com o ramo |
| Funil quebrado no portal | 0 contas | consertar antes (pedido ao Jão) |
| Criativo genérico | 5,7 s de 39 s assistidos | um criativo por nicho, dor nos 3 primeiros segundos |

## Estrutura
| Item | Salão de beleza | Barbearia |
|---|---|---|
| Conjunto | 1 conjunto só para salão | 1 conjunto só para barbearia |
| Criativo | Corte de 15–20 s do **V5 v2** ("14 mensagens e 4h28 pra marcar uma escova"), com a oferta na tela | Corte de 15–20 s da **Entrevista VIP Barbearia Nº1** (só depois da aprovação do Pablo) ou do anúncio barbearia 38 s reeditado |
| Mensagem pronta | `Tenho um salão e quero o cupom` | `Tenho uma barbearia e quero o cupom` |
| Público | São Paulo + 50 km · 25–54 · interesse salão de beleza/estética + administradores de página comercial | São Paulo + 50 km · 25–54 · interesse barbearia/barbeiro + administradores de página comercial |
| Posicionamentos | Instagram Stories e Reels | Instagram Stories e Reels |
| Verba | R$ 10/dia | R$ 10/dia |
| Duração | 5 dias, sem mexer nos 3 primeiros | 5 dias |
| Corte de sangria | R$ 30 no conjunto sem conta criada → pausar (com o ok do Rapha) | igual |

Total: R$ 100 em 5 dias (recarga do pré-pago pelo Rapha).

## Funil depois do clique
1. Direct: a regra `quero_cupom` manda o link (já testada; agora lê todas as mensagens novas).
2. Portal: `/assinar?cupom=QUEROCUPOM` mostrando o desconto (pedido ao Jão).
3. Acompanhamento em até 24 h: proposta de segunda mensagem automática, 3 h depois do cupom, perguntando se conseguiu
   criar a conta e oferecendo ajuda (fluxo em produção: só com de→para e ok do Rapha).

## Medição
Custo por **conta criada** (meta inicial: até R$ 50 por conta, conta nova sem histórico). Leitura no 3º e no 5º dia:
Gerenciador × `ig_interacoes` × contas e usos do cupom no portal.

## Riscos
- Entrevista VIP ainda sem aprovação do cliente: não usar em anúncio antes.
- Verba pequena: 5 dias dão uma leitura inicial, não definitiva.
- Interesse "barbearia/salão" pega cliente final; o filtro é a mensagem pronta e a oferta para dono.

---

## Atualização 16/11 · oferta única LANCAMENTO50 e preços em ,90 (aprovada pelo Rapha)
**Oferta:** cupom `LANCAMENTO50`: 50% nas 3 primeiras mensalidades, ao contratar até 10/12/2026, sem limite de usos.
O QUEROCUPOM sai dos anúncios. Direct: a regra nova `cupom_lancamento50` (ordem 4) responde "quero cupom",
"lancamento50" e "cupom de desconto" com o link `portal.malvora.com.br/assinar?cupom=LANCAMENTO50` (vale até 10/12; depois
volta a valer a do QUEROCUPOM, até 31/12).

**Antes de publicar (bloqueia):**
1. Preços em ,90 e Contratos a R$ 49,00 trocados em Equipe › Preços (o cartão final diz "a partir de R$ 249,90/mês").
2. Develop subida para a main (PR #421: cupom visível no /assinar e tela enxuta; PR #423: Desempenho por faixa).
3. "Aprovado" do Rapha para publicar e recarga de R$ 100.

### Criativos (novos)
| Conjunto | Arquivo | Duração | O que mudou |
|---|---|---|---|
| Salão e estética | `anuncio-salao-lancamento50.mp4` | 22,6 s | Cartão final novo (oferta e "mande QUERO CUPOM no direct"), no lugar de "Fale com a Malu" |
| Barbearia | `anuncio-barbearia-lancamento50.mp4` | 29,6 s | Corte até "Funciona junto com o AppBarber" + cartão final novo com a fala da Carla: "Cria sua conta grátis, sem cartão. E manda quero cupom no direct: cinquenta por cento de desconto nas três primeiras mensalidades." (sai o "comenta QUERO CUPOM… 50% no primeiro mês") |

Loudness -14 LUFS; transcrição conferida. A barbearia passou de 20 s (a regra pede 15–20 s): o trecho do AppBarber é o
argumento mais forte para esse público.

### Textos do anúncio
**Salão e estética**
- Texto principal: Meia-noite e meia, a cliente pede horário. Quem responde? A Malvora coloca uma IA no WhatsApp do seu salão: responde na hora, com os seus preços, e marca no horário livre. Teste grátis, sem cartão. Mande "quero cupom" no direct e ganhe 50% nas 3 primeiras mensalidades quando contratar (cupom LANCAMENTO50, até 10/12).
- Título: Teste grátis, sem cartão
- Mensagem pronta do direct: `Quero cupom · tenho um salão`

**Barbearia**
- Texto principal: No meio do corte, o WhatsApp não para. A Malvora coloca uma IA no WhatsApp da sua barbearia: responde na hora, com os seus preços, marca na agenda e lembra o cliente na véspera. Funciona junto com o AppBarber. Teste grátis, sem cartão. Mande "quero cupom" no direct: 50% nas 3 primeiras mensalidades quando contratar (cupom LANCAMENTO50, até 10/12).
- Título: Teste grátis, sem cartão
- Mensagem pronta do direct: `Quero cupom · tenho uma barbearia`

A mensagem pronta começa com "Quero cupom" de propósito: é o que a automação do direct reconhece, e o resto diz o ramo.

### Prompt para o T1 (só rascunho; não publicar)
> No Gerenciador de Anúncios da conta da Malvora (1079254947829364): duplique a campanha "Mensagens · Salão e barbearia · QUERO CUPOM" e renomeie para "Mensagens · Rodada 2 · LANCAMENTO50". Deixe a campanha **pausada**. Crie 2 conjuntos, cada um com R$ 10/dia, São Paulo + 50 km, 25 a 54 anos, posicionamentos só Instagram Stories e Reels, destino Direct do Instagram:
> 1. "Salão e estética": interesses salão de beleza, estética, cabeleireiro + administradores de página comercial; vídeo `conteudo/anuncios/rodada-2-salao-barbearia/anuncio-salao-lancamento50.mp4` (repositório raphalanalves/test, faça git pull); textos e mensagem pronta da seção "Textos do anúncio" do `plano.md`.
> 2. "Barbearia": interesses barbearia, barbeiro + administradores de página comercial; vídeo `anuncio-barbearia-lancamento50.mp4`; textos e mensagem pronta da barbearia.
> Não publique, não ative e não mude orçamento de nada. Não use cartão nem senha. No fim, mande prints da campanha e dos 2 conjuntos em rascunho e me diga se a Meta apontou algum problema de política.
