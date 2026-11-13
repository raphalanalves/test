---
name: video-entrevista-malvora
description: Planejar, gravar e editar entrevistas com clientes da Malvora (série "Entrevistas VIP"/"Clientes Malvora"), com duas câmeras, sem a voz de quem pergunta, pergunta repetida na resposta ou em texto na tela, cortes em preto e branco para falhas e momentos engraçados, abertura e fechamento com a logo do cliente (e a nossa no fim), e cortes derivados (teasers, vídeo de integrações). Usa fluxo de proxies, sincronização por áudio e edição pelo texto (transcrição com tempo por palavra). Use quando o assunto for entrevista, depoimento ou case em vídeo de cliente. Não é para Reels de roteiro próprio (use ig-content-planner e estruturas-de-retencao).
---

# Entrevistas com clientes · Malvora

A entrevista é o pilar **Prova** (`../../references/pilares-de-conteudo-que-vendem.md`): o cliente real contando
o antes e o depois. Nada é publicado sem a autorização por escrito do cliente e sem ele ver o corte final.

## 1. Antes de gravar (checklist para a próxima)
- **Autorização por escrito** para nome, imagem e logo (a Barbearia Numero 1 já autorizou).
- **Roteiro de perguntas na ordem da história:** quem é você e a barbearia → como era antes → o que mudou com a Malvora → um momento marcante → para quem você recomenda. 6 a 8 perguntas, abertas ("como era…", "me conta de quando…").
- **Combinar com o entrevistado:** repetir a pergunta na resposta ("O que mudou depois da Malvora foi…"), olhar para quem pergunta (não para a câmera), não falar junto com o entrevistador.
- **Duas câmeras do mesmo lado (regra dos 180°):** câmera A aberta (plano médio) e câmera B fechada (rosto), em alturas diferentes. Mesmo modo (vertical ou horizontal), 30 fps, luz de janela ou de frente.
- **Áudio:** microfone de lapela por entrevistado (o celular sozinho pega eco). 10 s de silêncio da sala no início (para limpar ruído).
- **Palma no início de cada bloco** (sincronização fácil) e uma tomada por pergunta.
- **B-roll** (imagens de cobertura): fachada, letreiro, cadeira, máquina, corte acontecendo, cliente rindo, celular com WhatsApp (sem logo do WhatsApp em destaque), mãos trabalhando. 5 s parado cada.

## 2. Fluxo de edição (moderno, sem refazer trabalho)
1. **Proxies:** o PC gera cópias leves com `ops/preparar-entrevista.ps1` e envia para o repositório privado temporário. Original nunca sai do SharePoint.
2. **Inventário e continuidade:** manifesto com aparelho, hora de criação e duração; ordenar por hora e agrupar por câmera (aparelho).
3. **Sincronizar as câmeras pelo áudio** (correlação cruzada da onda sonora), não no olho. Registrar o deslocamento de cada par.
4. **Transcrição com tempo por palavra** (faster-whisper). Marcar quem fala (entrevistado 1, entrevistado 2, entrevistador).
5. **Edição pelo texto (paper edit):** montar a lista de trechos por pergunta a partir da transcrição: o que entra, o que sai, o que vai para o bloco de erros, o que vai para o vídeo de integrações (AppBarber).
6. **Montagem (EDL):** decidir câmera A ou B por trecho e gerar a lista de decisões. Render final no PC, sobre os originais, com o mesmo roteiro de cortes (o servidor só trabalha nos proxies).
7. **Revisão:** Rapha aprova → cliente aprova → publicar em collab.
8. **Limpeza:** apagar proxies e o repositório temporário ao final.

## 3. Regras de edição
1. **A voz de quem pergunta nunca aparece.** Cortar todos os trechos do entrevistador.
2. **Toda resposta tem que se explicar sozinha.** Se o entrevistado não repetiu a pergunta, entra a pergunta em texto na tela (cartão de 1,5 a 2 s, frase curta, ex.: "Como era antes da Malvora?").
3. **Estrutura fixa:**
   - Abertura (5–8 s): logo do cliente + imagens da barbearia (fachada, ambiente).
   - Apresentação: cada entrevistado se apresenta, com nome e função na parte de baixo da tela.
   - Blocos por pergunta, na ordem do roteiro: os dois respondendo a mesma pergunta, alternando trechos.
   - Fechamento (5–8 s): imagens da barbearia + logo do cliente e logo da Malvora lado a lado.
4. **Duas câmeras:** trocar de câmera na troca de frase ou de ideia, nunca no meio da palavra. Fechada (B) para emoção e frase forte; aberta (A) para contexto. Pelo menos 3 s em cada plano.
5. **Com uma câmera só:** zoom digital leve (110–120%) na troca de frase, para esconder o corte.
6. **Transições leves:** corte seco na maior parte; dissolve curto (6–10 quadros) entre blocos; cortes J/L (o som da próxima fala entra antes da imagem) para fluir.
7. **Erros e frases engraçadas:** viram inserções em **preto e branco**, curtas (1–4 s), com um som leve, entre blocos ou no final (erros de gravação). Nunca expor o entrevistado de forma constrangedora; na dúvida, fica de fora.
8. **Integrações (AppBarber e outras):** tudo o que falar disso sai da entrevista principal e vai para a lista do **vídeo de integrações** (feito depois).
9. **Áudio:** redução de ruído leve, voz em -14 LUFS (padrão de redes), música baixa por baixo da fala (-18 a -20 dB) e subindo só na abertura e no fechamento.
10. **Legenda** queimada, em português, frases curtas, palavra-chave destacada; nada de logo do WhatsApp.
11. **Cor:** igualar as duas câmeras (exposição, temperatura) antes de cortar.
12. **Nada inventado:** número, resultado e frase são do cliente, sem edição que mude o sentido.

## 4. Formatos e derivados
| Peça | Formato | Duração | Uso |
|---|---|---|---|
| Entrevista completa | 9:16 (Reels, collab) e, se gravado horizontal, 16:9 (YouTube) | 2–4 min | Prova principal |
| Teasers | 9:16 | 30–45 s cada (1 pergunta forte) | Reels da semana, anúncio |
| Erros de gravação | 9:16 | 15–30 s | Story/Reel leve |
| Integrações (AppBarber) | 9:16 | 45–60 s | Vídeo à parte |
| Frases | Carrossel ou Story | 3–5 cartões | Feed/Stories |

## 5. Checklist antes de aprovar
- [ ] Nenhum trecho com a voz de quem pergunta?
- [ ] Toda resposta se entende sozinha (pergunta repetida ou em texto)?
- [ ] Abertura com a logo do cliente e fechamento com as duas logos?
- [ ] Integrações fora da entrevista principal?
- [ ] Trocas de câmera na troca de frase, sem pulo?
- [ ] Áudio limpo e no mesmo volume do começo ao fim?
- [ ] Legenda revisada (nomes, termos)?
- [ ] Autorização do cliente e aprovação do corte final?

## 6. Padrão da série "Entrevistas VIP" (aprovado pelo Rapha em 13/11/2026, Ep. 01 Barbearia Nº1)
Formato: **um vídeo só, vertical, 1min30 a 1min40**, animado (não documentário), em collab com o cliente.

**Estrutura fixa**
1. **Gancho (0–2 s):** a frase mais forte do cliente, com cara de prévia (cor reduzida + vinheta + etiqueta "JÁ JÁ NO VÍDEO"). Não usar preto e branco aqui (é o efeito dos bastidores).
2. **Vinheta padrão (3,2 s):** `vinheta.py <ep> "<cliente>" <logo.png> <saida> [largura]` (símbolo Malvora, "CLIENTES MALVORA", "ENTREVISTAS VIP", "Ep. NN · Cliente", logo do cliente; swell + chime baixo, sem "pop").
3. **Carla (intro, ~13 s)** sobre cenas estáveis do cliente: lançamento, o que o cliente usa da Malvora (só o que contratou de verdade), que foi um convite. Etiquetas: "LANÇAMENTO · ENTREVISTA" e "@cliente × @malvora_hub".
4. **Entrevista (~55–60 s):** apresentação de cada um (nome · função, ex.: "barbeiro e dono"), dor → perda real → com a Malvora → frase de fechamento. Frases completas. Pergunta na tela (cartão roxo no topo) quando a resposta não se explica sozinha.
5. **Bastidores (~4 s):** 1–2 falhas engraçadas em P&B com etiqueta "BASTIDORES".
6. **Carla (fechamento, ~18 s)** sobre cenas do cliente: suporte do time, "agora é acompanhar junto cada resultado" (nunca prometer resultado não medido), teaser da **parte 2**, "teste grátis, sem cartão, link na bio" → cartão final com as duas logos e os dois @.

**Regras técnicas aprendidas**
- **Enquadramento pelo rosto** (detecção automática): olhos ~1/3 da altura, plano médio (zoom ~1,35) e close (~1,75) alternando; câmera lateral recortada (1,55–1,9). Nada de zoom central (sobra teto).
- **Legenda abaixo do queixo** (faixa 68–74% da altura), 2–3 palavras, palavra falada em verde-água #00D4AA e palavras-chave em violeta #7B68EE; nunca sobrepor o nome na tela. Revisar "barbeira/barbaria → barbearia", "Nº1".
- **Cortes:** troca a cada ~2,5 s entre câmeras/zoom, só em pausa entre palavras. **Conferir a folga depois da última palavra** de cada fala: se a próxima palavra vem colada (< 0,1 s), escolher outra frase ou terminar no vale de energia com fade de 0,1 s.
- **Voz:** limpeza + EQ (corte 85 Hz, -2 dB em 220 Hz, +2,5 dB em 3,2 kHz), compressor 3:1, de-esser; acelerar no máximo 5%. Volume final -14 LUFS.
- **Efeitos:** nada de whoosh/pop (soam como "tapa"). Usar `conteudo/marca/sfx-swell-transicao.wav` entrando 0,7 s antes da troca de bloco, pico ~25 dB abaixo da voz.
- **Trilha** com ducking automático (sidechain) sob a voz. Atenção: o `loudnorm` sai em 192 kHz; sempre `aresample=48000` depois (senão o áudio encurta e dessincroniza).
- **Montagem sincronizada:** vídeo e áudio em peças separadas, contadas em quadros (sem acumular atraso).
- **Cenas de apoio:** medir o tremor e usar as mais estáveis; estabilizar (prévia: deshake; final: vidstab em 2 passadas, aproveitando a folga do 4K).
- **Final em 4K:** a prévia é feita nos proxies; depois `ops/recortar-4k.ps1` recorta só os trechos usados dos originais (com 1 s de folga) e o render final sai em 1080×1920 com os mesmos cortes, enquadramentos e cor.
