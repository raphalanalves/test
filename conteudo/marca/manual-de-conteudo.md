# Manual de conteúdo da Malvora (Instagram)

Padrões que valem para toda peça. Mudança só com aprovação do Raphael.

## 1. Marca

| Item | Padrão | Arquivo |
|---|---|---|
| Logo principal | Símbolo do triângulo com nós (`simbolo-triangulo-fundo`), sem o fundo | `simbolo-principal.png` |
| Outras versões | Só quando o Raphael pedir | `../lancamento-2026-11-10/contagem-comecou` (histórico) |
| Não usar | O desenho em código de linhas grossas; o símbolo em quadrado escuro | — |
| Marca d'água em vídeo | Símbolo de 84 px, 45% de opacidade, canto superior direito (56 px da borda, 84 px do topo), o vídeo inteiro **menos** nas cenas em que a logo já aparece grande | `marca-dagua-video.png` |
| Marca d'água em imagem e carrossel | Símbolo de 64 px, 50%, canto inferior direito, fora da capa | `marca-dagua-imagem.png` |
| Assinatura | `@malvora_hub` só no fim dos vídeos (não o vídeo inteiro) | — |
| Cores | Fundo #0B0B13 / #0E0E16 · verde-água #00D4AA · violeta #7B68EE · texto #F2F3F7 · alerta #E5484D | — |
| Fontes | Títulos: Manrope 800 ou Bebas Neue · texto e legenda na tela: Inter / Manrope | — |
| Área segura dos Reels | Nada importante nos 250 px de baixo nem nos 140 px da direita (botões do Instagram) | — |

## 2. Voz e áudio

- Voz oficial: Amandoca, ElevenLabs Eleven v4, estabilidade 0.5, similaridade 0.8, sem marcações de tom.
- Pausa entre falas: ~0,25 s. A imagem acompanha a voz, não o contrário.
- Música de fundo sempre presente e baixa (≈12% da voz), abaixando quando a voz entra; sobe na abertura, nas viradas e no fim.
- Efeitos: só virada de cena, revelação e piada. Nada de sequência de tiques.
- Música em alta (inclusive em vídeos sérios): exportar a versão **sem música** e postar pelo app escolhendo a faixa.
  Riscos: a conta comercial só vê a biblioteca liberada para empresas; faixas fora dela podem ser silenciadas, e
  música comercial nunca entra em anúncio ou impulsionamento. Esses posts são manuais (a API não coloca música).
- Trilha própria (padrão dos posts automáticos): liberada para uso comercial, gerada para o clima de cada vídeo.

## 3. Tom

Empresa séria, que fala como gente. Uma "gracinha" (meme, humor) no máximo a cada 5 ou 6 posts, sempre ligada à
rotina de quem trabalha com agenda, nunca rindo do cliente do cliente.

## 4. Séries e numeração

- O número de um episódio é a **ordem em que ele é publicado**, não a ordem em que foi produzido.
- Uma série só ganha o próximo número depois que o anterior estiver no ar.
- Nome no arquivo e na tela: `Alquimias #N`. Até publicar, os projetos ficam sem número definitivo.
- Ordem atual das Alquimias (nenhuma publicada): #1 Alquimias 01, #2 Fim da 6x1 (a melhorar), #3 KLM.

## 5. Cada post tem

Formato principal e reaproveitamentos (Reels / Feed / Stories), objetivo (alcance, engajamento, captação),
CTA único e quem responde comentários e direct nas 2 h seguintes.

## Mosaico (posts que formam uma imagem só na grade)

A grade do perfil mostra cada post em 3:4. Um post 4:5 (1080x1350) perde cerca de 34 px de cada lado na grade, e entre
as colunas há um espaço de alguns pixels. Se a arte for cortada em três partes iguais, as linhas que passam de um post
para o outro (círculos, anéis, textos) aparecem quebradas na emenda. Foi o que aconteceu no mosaico de 31/10.

Regra:
1. Montar o painel com a largura que a grade mostra: 3 x 1012 px, mais 10 px por emenda (o espaço entre as colunas).
2. Cada post é recortado com 34 px de sobra de cada lado (1080 px no total), tirados do próprio painel.
3. Antes de agendar, gerar a prévia da grade (corte 3:4 + espaço entre colunas) e conferir as emendas ampliadas.
4. Evitar linha fina cruzando a emenda quase na horizontal; se cruzar, que seja perto do meio da altura.
5. Publicar da direita para a esquerda, um minuto entre cada um, e fixar os três na mesma ordem.

Ferramenta: `lancamento-2026-11-10/mosaico/_fonte/mosaico-v2.html` + `render-mosaico.js` (o recorte e a prévia
estão no script do commit de 02/11).
