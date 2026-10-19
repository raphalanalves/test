# Formato "contador na tela" · referência WizeBot (anotado em 19/10/2026)

Referência: [@wizebot.com.br · WhatsApp Flows](https://www.instagram.com/p/Dei4HBVs4W6/) (15/10/2026).
É um **anúncio pago** (o Apify marca como `ad`): 599 visualizações orgânicas, 12 curtidas, 74 s. O alcance veio da
verba, então o que vale copiar é o formato e o roteiro, não o desempenho.

**Status: pendência.** Criar peças nesse formato depois da semana de 19 a 25/10.

## 1. O formato

- **Motion graphics, sem rosto.** Fundo azul em gradiente da marca, um celular no centro, narração com uma linha de
  legenda no topo e a palavra-chave em verde.
- **Um elemento fixo que conta.** O selo "Mensagens que você paga: 1, 2, 5..." fica em cima do celular e sobe a cada
  balão da conversa. Quando entra o Flow, ele volta para 1. É o que segura a atenção: o espectador acompanha o número.
- **Uma conversa só, montada ao vivo.** "Oi, queria um orçamento" → nome → serviço → endereço → data → confirmação.
  Cada pergunta é um balão novo e o contador sobe junto.
- **Uma imagem para a perda.** Uma grade de 12 avatares (Ana, Bruno, Carla...) em que vários vão apagando: "no meio
  desse caminho, muita gente some".
- **A virada em um cartão.** "WhatsApp Flows" aparece sozinho, e o celular mostra o formulário sendo preenchido.
- **O resultado em cartões.** "Atendimento completo" vai para a planilha ou para o sistema. Depois empilham 3
  segmentos: clínica (agendamento), loja (pedido) e prestador de serviço (orçamento).
- **Fecho.** Campo de comentário digitando "FLOWS", logo da marca, "30 dias de garantia".

## 2. O roteiro (ganchos que ele usa)

| Trecho | Conteúdo | Gancho |
|---|---|---|
| Abertura | notificação de um cliente: "Jonas, agora eu vou pagar pra responder cliente no WhatsApp?" | pergunta real do público (relatable) |
| Alívio | "Mas bem menos do que você imagina": 1.000 grátis por mês, depois R$ 0,035 | G3 (mito e desmentido) |
| Virada | "Não é isso que pesa": o contador sobe com o vaivém | G5 (guarda o que importa) |
| Solução | o Flow junta tudo numa tela e o contador volta para 1 | G2 (o caminho C) |
| Prova | 3 segmentos com o pedido completo | identificação por segmento |
| CTA | "Comenta FLOWS" + garantia | palavra-chave (só com automação de direct) |

## 3. O assunto quente por trás: a nova cobrança da Meta

Desde **1º/10/2026** a Meta cobra também as respostas dentro da janela de 24 h, com **1.000 mensagens grátis por mês
para cada número** e, depois, **R$ 0,035 por mensagem** no Brasil. Botconversa e WizeBot já estão usando isso para
vender Flows. Há conteúdo do setor nas duas linhas: o alarmista ("o WhatsApp vai cobrar tudo") e o desmentido
("o que é verdade e o que é alarmismo").

Ponto a decidir antes de a Malvora falar disso: hoje o WhatsApp dos clientes passa pela Evolution API. Se for o
conector Baileys (WhatsApp Web), essa cobrança não se aplica, mas a Malvora **não deve usar isso como argumento de
venda**: é uma conexão não oficial e a Meta pode bloquear o número. Falar do tema só depois de definir o caminho
oficial (ver `estudo-whatsapp-flows.md`).

## 4. Como a Malvora faz igual (com a nossa identidade)

O motor de animação que já temos (`alquimias-02-fim-6x1/_fonte/engine2.js`) dá conta: celular, balões, contador
(`data-count`) e legenda palavra por palavra. Precisa de dois componentes novos:
1. **Contador fixo** que sobe a cada evento do roteiro (selo no topo do celular, com o "pulse" a cada incremento).
2. **Grade de avatares** com apagamento em sequência.

Fundo #0E0E16 com o gradiente teal → violeta no lugar do azul, Bebas Neue e Inter, e o símbolo oficial no fecho.

Ideias de peças nesse formato:

| Peça | O que o contador conta | Gancho | Depende de |
|---|---|---|---|
| **"Quantas mensagens até marcar um horário?"** | mensagens trocadas até o cliente estar na agenda: 14 no atendimento comum × 3 com a IA da Malvora, que já oferece os horários livres | G1 | nada; dá pra fazer já |
| **"Quanto custa um cliente sem resposta?"** | conversas sem resposta no sábado × valor do ticket médio de um salão | G5 | ticket médio de um segmento com fonte |
| **"A falta que custa"** | horários vagos na semana somando em R$ | G1 | dado de falta com fonte (já temos São Vicente e Barts) |
| **"15 perguntas ou 1 tela"** (Flows) | mensagens pagas na conversa × no Flow | G2 | o recurso Flows existir e o preço oficial conferido |

A primeira não depende de nada novo e é a melhor candidata para o primeiro teste do formato.

## Fontes

- [Chat2Desk · Cobrança do WhatsApp API em outubro de 2026](https://chat2desk.com.br/blog/nova-cobranca-whatsapp-outubro-2026-mensagens-de-servico/)
- [Blip · Entenda a cobrança de mensagens de serviço](https://www.blip.ai/blog/inteligencia-conversacional/cobranca-mensagens-de-servico-meta/)
- [E-Commerce Brasil · Novo custo do WhatsApp](https://www.ecommercebrasil.com.br/artigos/novo-custo-do-whatsapp-o-que-muda-a-partir-de-outubro-e-como-reduzir-o-impacto)
- [Kiskadi · O que é verdade e o que é alarmismo](https://kiskadi.com/blog/whatsapp-cobranca-outubro-2026/)
