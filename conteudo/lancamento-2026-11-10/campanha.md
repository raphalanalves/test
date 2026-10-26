# Campanha de lançamento · Malvora · 10/11/2026

Proposta de 26/10/2026. Início: quarta 28/10 (D-13). Lançamento: terça 10/11 (D0).
Prévia da página com a contagem: https://claude.ai/artifact/4KoJJRcjkxHVvrKiTHTnDL (arquivo `pagina-contagem.html`,
para virar bio.malvora.com.br/lancamento).

## 1. O que engaja em lançamentos (Apify, 26/10/2026)

Amostra: 147 Reels de #embreve, #lancamento, #comingsoon, #contagemregressiva e #prelancamento, mais leitura dos que
mais tiveram comentários e envios.

| Padrão | Exemplo | O que aconteceu |
|---|---|---|
| **Adivinha o que vem** (spoiler com pista) | @brasilparkshopping: "Se você já reconheceu, comente" | comentário vira palpite; 100 comentários em 24 mil views |
| **"A espera está chegando ao fim"** + acompanhar cada novidade | @shoppingjardimguadalupe (novo cinema) | 1.156 comentários e 5.350 envios em 150 mil views |
| **Bastidores / primeira mão** | @shooloongkansaopaulo ("o que estamos preparando") | 8 mil envios em 174 mil views |
| **Pré-cadastro com data** ("pré-save, link na bio") | @alinyfernandesgoncalves | **14.719 envios** em 41 mil views: a data + o link fazem a pessoa mandar pra alguém |
| **Revelação curta e forte** | @buqcare ("Apresentamos o Imbakt") | 8.086 comentários; peça de 40 s, uma promessa só |
| **Contagem com número grande** | #contagemregressiva: vídeos de 9 a 15 s com o número na tela | maiores taxas de envio da amostra (ex.: 3.438 envios em 167 mil) |

Lições para a Malvora:
1. **Data e um único destino** (lista VIP) em todo post. É o que gera envio.
2. **Uma revelação por dia**: cada post mostra uma parte do que chega (agenda, Pix, lembrete, IA).
3. **Jogo de palpite** nos Stories e num carrossel desfocado: comentário é o sinal que mais pesa para alcance.
4. **Vídeos curtos de contagem** (10 a 15 s) intercalados com os vídeos narrados.
5. **Rosto humano**: os 4 fundadores aparecendo perto do lançamento dão confiança a uma marca nova.

## 2. O que a Malvora oferece (site, bio e portal)

- **Base:** IA no WhatsApp com o nome da empresa (responde em segundos, passa para a equipe), agendamento por
  profissional, lembretes, avisos, portal com conversas, clientes (ficha, quadro), perguntas frequentes, contratos.
- **Módulos:** Pagamento (Pix, boleto e cartão pelo Asaas, R$ 79), Fidelização/Relacionamento (retorno,
  reativação, NPS, aniversário, R$ 79), Relatório (WhatsApp e e-mail, R$ 49), Inteligência (Desempenho, funil,
  motivo de não fechar, +25% do plano), Importar planilhas.
- **Planos do site:** Essencial, Crescimento (mais escolhido) e Completo; a partir de R$ 250/mês; teste grátis de
  150 mensagens ou 24 h; sem cartão.
- **Segmentos:** 29 no catálogo (barbearia, salão, clínica médica, odontologia, estética, tatuagem, ótica,
  cosméticos, advocacia, pet, academia, imobiliária, restaurante, escola, oficina, eventos, contabilidade, moda,
  terapias, veículos, serviços domésticos, seguros, hotelaria, turismo, infoprodutos, creators, coworking, papelaria,
  outros). O site fala em "30 tipos de negócio".
- **Integrações:** WhatsApp, Asaas, Google Agenda, Outlook, e-mail, planilhas, reunião online.
- **Serviços (bio):** consultoria, automações e diagnóstico ("Receba seu diagnóstico").
- **Equipe:** Pietro Costa (CEO), Raphael Alves (COO), João Luz (CTO), Nycole Novais (CAIO).

## 2b. Atualização de 26/10 (decisões do Raphael)

- **Lista VIP só com 10 empresas** e link divulgado **a partir de 01/11**. De 28 a 31/10 os posts criam expectativa
  sem link.
- **50% off só para quem entrar na lista VIP** (e assinar até o lançamento). Sugestão: 50% nos 3 primeiros meses,
  em qualquer plano, para dar peso à vaga sem comprometer a margem do ano todo. A decidir.
- **Lançamento 10/11 às 00h.** Acesso antecipado da lista em 09/11 à noite: aprovado.
- **Portal controlado só pelos links** (nenhum post cita o portal até 10/11).
- **Bio:** página nova no visual do portal, links antigos redirecionados para a home até o lançamento
  (repositório `bio-links`, branch `pre-lancamento`, aguardando aprovação para ir ao ar).
- **Voz:** a referência é a voz do ChatGPT. Proposta: OpenAI TTS (`gpt-4o-mini-tts`), mesma família de vozes, com
  instruções de tom. Precisa da chave da OpenAI como credencial no n8n ou segredo do ambiente.
- **Confiança na comunicação:** LGPD, login com Google e Microsoft, dados separados por empresa, e integrações
  (WhatsApp, Asaas, Mercado Pago, ZapSign, Autentique, Google Agenda, Outlook, Google Drive, AppBarber).

## 3. O problema do link do portal (e a proposta)

Hoje **malvora.com.br redireciona para portal.malvora.com.br**, que já tem "Começar teste grátis" e "Assinar".
Qualquer post que leve ao site deixa a pessoa assinar antes de 10/11 (e sem a condição de lançamento).

Proposta:
1. **Até 10/11, todo CTA aponta para bio.malvora.com.br/lancamento** (contagem + lista VIP). O link da bio do
   Instagram muda para essa página na quarta 28/10. Nenhum post cita o portal.
2. **Modo pré-lançamento no portal** (ajuste pequeno no malvora-core, a combinar com o Pietro): até a data, os
   botões "Assinar" e "Teste grátis" da página inicial viram "Entrar na lista VIP". O login de quem já é cliente
   continua igual.
3. **Lista VIP com vantagem real:** quem entra recebe no WhatsApp, no dia 09/11 à noite, o link de acesso
   antecipado (abre algumas horas antes para eles). Isso transforma a lista em motivo de envio ("entra aí que
   abre antes").
4. **Lista VIP no n8n:** o formulário da página grava numa tabela (nome, WhatsApp, segmento, origem) e responde
   na hora pelo WhatsApp da Malvora confirmando a vaga. Em 10/11, um disparo avisa todo mundo.

## 4. Calendário (D-13 a D0)

Legenda: ✅ peça já pronta · 🎙 precisa de narração · 🆕 a produzir.

| Dia | Feed | Stories |
|---|---|---|
| Qua 28/10 · D-13 | 🆕 Reel teaser "o papel rasga" (V12) + troca do link da bio | contagem regressiva oficial (figurinha) apontando para 10/11 |
| Qui 29/10 · D-12 | 🆕 Carrossel manifesto "Em 10/11 sua empresa passa a atender sozinha" | enquete: "Quantas mensagens você deixa sem resposta no fim de semana?" |
| Sex 30/10 · D-11 | ✅ Reel V14 "Cliente ligando" (clínica) com legenda de lançamento | bastidores do portal (tela desfocada) |
| Sáb 31/10 · D-10 | 🆕 Reel curto contagem "10" (banner, V11): "amanhã abre a lista. Só 10 vagas." | quiz: "Qual destes a IA faz?" |
| Dom 01/11 · D-9 | 🆕 **Abertura da lista VIP**: Reel + post fixado "10 vagas, 50% off" com o link da bio | contador de vagas ao vivo |
| Seg 02/11 · D-8 | ✅🎙 Reel V7 "Hexágonos" | repost dos palpites |
| Ter 03/11 · D-7 | ✅ Reel V14 (barbearia) + contagem "7" | figurinha de contagem |
| Qua 04/11 · D-6 | 🆕 Carrossel "Pronta para 30 tipos de negócio" (identificação por segmento) | enquete por segmento |
| Qui 05/11 · D-5 | ✅🎙 Alquimias #3 (KLM) | — |
| Sex 06/11 · D-4 | 🆕 Revelação **50% off em novembro** (Reel curto + post fixado) | contagem + link VIP |
| Sáb 07/11 · D-3 | ✅🎙 Reel V13 "Chama o gerente" | bastidores |
| Dom 08/11 · D-2 | ✅ Reel V5 "Quantas mensagens" | "Lista VIP abre antes: amanhã" |
| Seg 09/11 · D-1 | 🆕 Reel dos 4 fundadores: "Amanhã." | contagem final; às 20h acesso antecipado para a lista |
| Ter 10/11 · D0 | 🆕 Reel revelação (V12 parte 2: o celular mostra a IA atendendo) + carrossel completo + link do portal liberado | dia inteiro de Stories, respostas ao vivo |

Ajustes na fila do n8n: o V14 clínica (27/10) vai para 30/10, o V14 barbearia fica em 03/11 e o V5 sai de 10/11 para
08/11. Tudo continua `aguardando_legenda` até a sua aprovação.

## 5. Vozes

As narrações atuais usam uma voz-guia simples. Para a campanha, a proposta é uma voz de IA de primeira linha em
português do Brasil, com a mesma voz em todos os vídeos (vira a "voz da Malvora"). Caminho recomendado:
**ElevenLabs** (voz da biblioteca ou clonada com autorização). Preciso:
- saber qual é a "voz do gato" que você citou (link de um vídeo com ela), para escolher igual ou superior;
- a chave da API cadastrada como credencial no n8n ou como segredo do ambiente (nunca no chat).
Com isso eu refaço as narrações do V7, Alquimias #3, V13, Alquimias #1 e Fim da 6x1 e gero amostras para você
escolher antes.

## 6. Automação

Com a sua aprovação de cada peça, eu preencho a legenda na `instagram_fila`, marco `aprovado` e ligo o
"Publicador da fila" do n8n (hoje desligado). Ele publica no horário, comenta as hashtags e te avisa por e-mail.

## 7. Decisões pendentes

1. Os 50% valem por quanto tempo (1ª mensalidade, 3 meses, 12 meses)? E para todos os planos?
2. Lançamento às 00h ou em outro horário de 10/11?
3. Modo pré-lançamento no portal: fazemos (com o Pietro) ou só controlamos pelos links?
4. Acesso antecipado para a lista VIP em 09/11: sim ou não?
5. Qual é a "voz do gato" e a ferramenta de voz.
6. Aprovar o calendário para eu produzir as peças 🆕 a partir de quarta.

## 8. Crescimento do perfil (atualização de 26/10)

O objetivo da campanha é trazer seguidores novos, não só anunciar. Técnicas aplicadas em todas as peças:
- **Laço aberto:** cada post termina numa pergunta sem resposta ("Quem respondeu tudo isso?") que só se fecha em 10/11, e o pedido é **seguir** para descobrir.
- **POV e cenas reais do dia a dia** do dono (tela do celular, notificações) em vez de animação abstrata: parece conteúdo de criador, não anúncio.
- **Série numerada** ("faltam 13", "faltam 10"...): quem vê um quer ver o próximo; o perfil vira a série.
- **Reels de teste** (Trial Reels do Instagram): mostram o Reel só para quem não segue, ideal para conta pequena; usar nas peças de gancho forte.
- **Collab posts** com 1 ou 2 clientes/parceiros em 10/11: o post aparece nos dois perfis.
- **Stories diários** com figurinha de contagem regressiva (quem ativa recebe o aviso) e enquetes/quiz.
- **Ritmo legível:** cada informação fica na tela tempo suficiente para ler (mínimo de 3 a 4 s por frase), vídeos de 15 a 25 s.
