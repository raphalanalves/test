# V5 v2 · Quantas mensagens até marcar (com a Carla)

- Animação: `v05v2.html` (tempos presos à fala da Carla, take B, acelerada 1,10x, entrando em 0,25 s).
- Voz: ElevenLabs, Carla (eleven_v4), take B. Texto no roteiro abaixo; "Malvôra" no texto da voz.
- Áudio: voz -15 LUFS + trilha `lancamento-2026-11-10/reel-o-que-faz/_audio/mus_a.mp3` (0,22, abaixa sob a voz,
  sobe no fim) + 3 efeitos: entrada (`marca/sfx-swell-transicao.wav`), rebobinar (`fita.wav`, 1,3 s) e marcado
  (`marca/sfx-chime.mp3`). Mix final -14 LUFS.
- Marca d'água: 84 px, 45%, canto superior direito, até o CTA (38,4 s). Logo oficial `simbolo-principal.png` no CTA.
- Render: `node render.js v05v2.html 44.9 saida.mp4 ../audio-v2.wav 1.5` e depois o overlay da marca d'água.

Roteiro: Quantas mensagens a sua cliente precisa mandar pra conseguir marcar um horário? No atendimento de sempre,
ela pergunta às nove da manhã… e a resposta chega três horas depois. Aí começa o vai e vem: que horas, com quem,
quanto fica. Foram catorze mensagens e quase quatro horas e meia pra marcar uma escova. Nesse meio-tempo, ela podia
ter fechado com outro salão. Agora, a mesma conversa com a Malvôra. A IA responde na hora, já com os horários livres
e o preço. A cliente escolhe, e pronto: marcado, com lembrete na véspera. Catorze mensagens contra quatro. Quatro
horas contra um minuto. Manda esse vídeo pra quem ainda deixa a cliente esperando três horas por uma resposta.
