# Regras fixas

## 1. Segurança (não negociáveis)
- Nunca pedir nem colar token, chave ou senha no chat. Credenciais ficam só nas credenciais do n8n ou em variável de ambiente.
- Senhas do portal, da Meta e cartão: só a pessoa digita, no navegador.
- Nada de segredo, número de telefone ou endereço de webhook interno em arquivo enviado ao GitHub (este repositório é público).
- Nunca desligar a verificação de TLS.
- Nada é publicado no Instagram sem aprovação do Raphael (status `aprovado` na fila).

## 2. Marca
- Logo principal: símbolo do triângulo com fundo (`simbolo-principal.png`), salvo pedido contrário.
- Voz oficial (desde 02/11): Carla (ElevenLabs, voz 7eUAxNOneHxqfyRS77mW), Eleven v4, estabilidade 0.35, similaridade 0.8, estilo 0.4, sem tags. A Amandoca saiu.
- Pronúncia: "Malvôra". No texto enviado à voz, escrever "Malvôra"; na legenda e na tela, "Malvora".
- Abertura de Reel: o gancho em texto já aparece no primeiro quadro (sem fade), um som curto de entrada e a primeira fala em ~1 s.
- Nome do perfil: "Malvora • IA para empresas". Não nichar em "WhatsApp": a Malvora atende, agenda e cobra pela empresa.
- Toda legenda termina com: "Malvora Hub: A nova alquimia digital. 💚💜"
- O portal só aparece na comunicação a partir de 10/11/2026, 00h.

## 3. Conteúdo (resumo do manual)
- Marca d'água: vídeo 84 px, 45%, canto superior direito; imagem 64 px, canto inferior direito.
- "@malvora_hub" só no fim. SFX só quando essencial. Música própria por padrão; música em alta pelo app vale em post sério (post manual).
- Uma "gracinha" a cada 5–6 posts, no máximo. Numeração das séries pela ordem de publicação.
- Todo post diz: formato (Reels, Feed, Stories), objetivo (alcance, engajamento, captação, confiança), CTA e quem responde.
- Decisões de conteúdo passam pelas skills de Instagram (planner, carousel, caption, humanizer, hashtag, profile).
- Hashtags: 3 a 5, no primeiro comentário, sem nichar em WhatsApp.
- Mosaico: montar para a grade 3:4 (1012 px visíveis por post, 34 px de sobra de cada lado, 10 px por emenda) e
  conferir a prévia da grade antes de agendar. Post publicado não troca de imagem.

## 3b. Vídeo com IA (personagem 3D)
- Personagem fixo da Malvora: dono de negócio em 3D, polo verde-água e pin roxo do triângulo (referência em `conteudo/v13-chama-o-gerente/3d/personagem-3.png`).
- Gerar pela ElevenLabs (Kling 2.5 Turbo para vídeo; Nano Banana 2 para quadros 9:16). Sempre passar o custo antes; parar se o saldo ficar abaixo de 8.000 créditos antes da renovação (~26/11).
- Celular sempre parado na cena (a IA deforma objetos na mão). Textos, contador e marca entram na montagem.

## 4. Publicação automática
- Só pela API oficial da Meta, via n8n. Nada pelo app, navegador ou senha.
- Fila `instagram_fila`: só sai o que estiver `aprovado`; trava `publicando` evita post duplicado; primeiro comentário com as hashtags.
- Respeitar o limite de publicação da conta; erro repetido pausa a fila e avisa.
- Reel de teste (trial reel) pela API quando a conta permitir. Nunca publicar o mesmo Reel duas vezes.
- Palavra-chave às claras: na fala, na tela, na legenda e no texto alternativo. Nada de texto escondido.

## 5. Respostas automáticas
- Comentários com variações (nunca a mesma frase), agradecimento a comentário genérico, alerta para pergunta.
- Direct: IA com lista fechada do que sabe; o resto vai para a equipe. Sem cupom, sem prazo, sem promessa.
- Direct automático só para quem puxou conversa (janela de 24 h) ou comentou palavra-chave.
- Proibido: curtir, seguir ou comentar em massa por automação, mandar direct para quem não puxou conversa,
  contas falsas e grupos de engajamento. É o que derruba conta e, no produto, derrubaria o app de todos os clientes.

## 6. Anúncios
- Limite de gasto definido na conta de anúncios (hoje R$ 400 até 25/11). A automação nunca passa dele.
- Campanhas criadas pela API ficam pausadas até a primeira aprovação; depois rodam sozinhas dentro do teto.
- Pausar sozinho se o custo por conversa ou por cadastro passar do limite combinado.

## 7. Produto por cliente
- Cada cliente tem conta conectada, token, fila e limite próprios; um cliente nunca afeta outro.
- Para clientes, o n8n fala com o portal pela API interna, nunca direto no banco. A Malvora (piloto) pode usar o banco direto.

## 8. Comunicação
- Sempre que houver algo pendente, mandar um **mini relatório de pendências** (prioridade, o quê, quem, prazo) e
  atualizar `vault/pendencias.md`.
- Avisar no chat quando cada post for publicado, com o link.
- Quando o Claude do terminal (máquina do Raphael) pedir decisão, responder sempre com o texto pronto para colar, num bloco de código.
