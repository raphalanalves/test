# Revisão geral dos vídeos · 30/10/2026

Antes de mexer nas legendas: o que existe, o que falta, onde cada peça vai (Reels, Feed, Stories), o que buscamos com
ela e quem precisa estar pronto para responder.

## 1. O que os dados do nicho mostram (ig-audience-insights, 30/10)

Amostra: 117 Reels de #clinicadeestetica, #barbearia, #automacaowhatsapp, #agendamento e #inteligenciaartificial.
Perfil @malvora_hub: 836 seguidores, 3 posts, conta comercial, sem destaques.

| Recorte | Reels | Reproduções (mediana) |
|---|---|---|
| Até 15 s | 35 | 86,7 mil |
| 15 a 30 s | 21 | 43,9 mil |
| 30 a 60 s | 26 | 49,0 mil |
| Mais de 60 s | 35 | 38,9 mil |
| Com música da biblioteca | 40 | 72,4 mil |
| Só áudio original | 75 | 44,6 mil |
| Humor / meme (😂, "meme" na legenda) | 25 | 85,3 mil |
| Demais | 92 | 52,5 mil |

O que se repete entre os que mais rodam:
- **Curto ganha alcance.** Até 15 s tem quase o dobro da mediana dos de 60 s ou mais. Vídeo longo funciona quando
  ensina algo (os de IA com 100 s+ têm muito envio), não para anunciar.
- **Música da biblioteca ajuda**, mas não há uma música dominante no nicho: cada post usa uma diferente.
- **A "gracinha" funciona no nosso público.** Memes de agenda ("cliente que não gosta de agendar", "aviso foi dado")
  passam de 1 milhão de reproduções em contas de beleza. Bom para crescer, com moderação, como você disse.

## 2. Política de áudio (vale para todos os vídeos daqui em diante)

1. **A voz manda.** Música de fundo baixinha (em torno de 12% do volume da voz), abaixando sozinha quando a Amandoca
   fala e subindo só na abertura, nas viradas e no final.
2. **Efeitos só onde fazem sentido:** uma virada por cena, o momento da revelação e a piada. Saem as sequências de
   tique, plim e batida que estão em quase todos os vídeos.
3. **Música "mais escutada": um limite importante.** A @malvora_hub é conta comercial. No Instagram, conta comercial
   só pode usar a coleção de músicas liberadas para empresas; os sucessos do momento podem ser silenciados ou derrubar
   o alcance, e postar pela API (o publicador do n8n) não permite escolher música da biblioteca. Caminhos:
   - **A (recomendado, padrão):** trilha própria e liberada para uso comercial, já mixada no vídeo. Pode ser gerada pela
     ElevenLabs (Eleven Music, mesmo plano que já temos; preciso adicionar uma rota no n8n) no clima de cada vídeo.
     Funciona com o publicador automático.
   - **B (para as "gracinhas"):** exporto o vídeo sem música e você posta pelo app escolhendo um áudio em alta da
     biblioteca comercial, no volume baixo. Nesses posts a publicação é manual.

## 3. Inventário e decisão por vídeo

Legenda das colunas: **Onde** = superfícies (o primeiro é o principal). **Objetivo** = alcance, engajamento,
captação. **Interação** = o que o público vai fazer e quem responde.

### Prontos (só ajustar o áudio)

| Vídeo | Duração | Onde | Objetivo | Interação | O que fazer |
|---|---|---|---|---|---|
| Vinheta da logo (raios) | 10 s | Reels + Stories (corte de 6 s) | Alcance, curiosidade | Nenhuma | Manter os estalos (são o efeito); só música grave de fundo |
| Revelação da logo | 21 s | Reels + Stories + post fixado | Captação (lista VIP) | Perguntas no direct sobre a lista e o desconto | Trocar a trilha sintetizada por música própria |
| V7 Hexágonos | 45 s | Reels | Engajamento (comentário "aceso ou apagado") + captação VIP | Comentários; responder com o link da bio | Tirar tiques e plins; música de fundo |
| V15 Três buracos | 49 s | Reels (D0) + carrossel no Feed | Captação (portal em 10/11) | Direct com dúvidas de preço e plano | Música de fundo; deixar só a virada dos buracos |
| V16 Qual IA escolher | 67 s | Reels | Captação + autoridade | **Comentário "IA" pede resposta** | Cortar para ~45 s (o nicho mostra queda acima de 60 s); música |
| V14 Cliente ligando (clínica e barbearia) | 18 s cada | Reels | Alcance (identificação) | Pouca | Revisar: as palavras entram no ritmo da batida, então aqui a música é parte da peça |
| V5 Quantas mensagens | 25 s | Reels | Engajamento (comentário com o número) | Comentários | Revisar o áudio com a nova regra |

### Precisam ser refeitos

| Vídeo | Duração | Onde | Objetivo | O que falta |
|---|---|---|---|---|
| V13 Chama o gerente | 25 s | Reels | Alcance pela "gracinha" | Voz da Amandoca + uma segunda voz (o gerente); áudio em alta pelo app (caminho B) |
| Alquimias #3 (KLM) | 52 s | Reels | Autoridade | Narração da Amandoca (hoje é voz-guia) |
| Alquimias #1 | 72 s | Reels | Autoridade | Narração da Amandoca; avaliar cortar para menos de 60 s |
| Alquimias #2 · Fim da 6x1 | 73 s | Reels | Alcance | Narração; **decidir se entra**: o tema é polêmico para uma marca séria no lançamento |

### A produzir

| Peça | Onde | Objetivo | Data sugerida |
|---|---|---|---|
| Revelação dos 50% (só lista VIP) | Reels curto + Stories + post fixado | Captação | 06/11 |
| Fundadores: "Amanhã." | Reels + Stories | Confiança, seguidores | 09/11 (precisa de gravação; sem ela, versão animada) |
| Carrossel "Pronta para 30 tipos de negócio" | Feed | Salvamentos e identificação | 04/11 |
| Carrossel "Três buracos no caixa" (versão do V15) | Feed | Salvamentos | após 10/11 |
| Stories diários (contagem, enquete, bastidores) | Stories | Relacionamento | todos os dias |

### Já existentes e fora do calendário atual

- `2026-10-semana-12-18/`: Reels "23:47" e "Lembrete da véspera", 3 carrosséis (plataforma, mitos, método) e uma imagem.
  Preciso saber se já foram postados (o perfil mostra 3 posts).
- Descartados por você: teaser "papel rasga", POV, "áudio vazado", "contagem começou" e "logo em locais".

## 4. Preparação para responder

| Gatilho | Onde chega | Resposta | Quem |
|---|---|---|---|
| "IA" nos comentários (V16) | Comentários → direct | Mensagem pronta no direct + link (lista VIP até 10/11, portal depois) | Automação no n8n (a fazer) ou alguém da equipe |
| "Aceso" / "apagado" (V7) | Comentários | Resposta curta e simpática, puxando para a lista VIP | Equipe |
| Lista VIP, desconto, acesso antecipado | Direct e WhatsApp | Banco de respostas (FAQ que já combinamos) | Equipe + boas-vindas automáticas já no ar |
| Preço e planos (a partir de 10/11) | Direct | Link do portal + teste grátis | Equipe |

Antes do primeiro post com CTA, vale definir quem olha comentários e direct, e em quais horários (sugestão: até 2 h depois
de cada post, que é quando o alcance se decide).

## 5. Próximos passos sugeridos

1. Você valida a política de áudio (A como padrão, B para as gracinhas).
2. Eu monto a rota da Eleven Music no n8n e refaço o áudio dos prontos, nesta ordem: vinheta, revelação, V7, V15, V16 (com o corte), V14, V5.
3. Refaço V13 e Alquimias #3 com a Amandoca.
4. Produzo os 50%, o carrossel dos 30 negócios e os Stories.
5. Voltamos às legendas e à fila.
