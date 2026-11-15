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
