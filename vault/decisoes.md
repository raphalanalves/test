# Registro de decisões

| Data | Decisão |
|---|---|
| 31/10 | Lista VIP pela Malu no WhatsApp (sem formulário); pré-cadastro como acompanhamento; sorteio de 2 vagas em 09/11; 20% para a lista de espera |
| 31/10 | Mosaico publicado junto, da direita para a esquerda, às 20h05–20h07 |
| 01/11 | Revelação da logo + lista VIP publicada (Reel fixado) |
| 02/11 | Carrossel "Quem respondeu?" refeito (slide da simulação, sem nichar em WhatsApp) e aprovado para as 18h |
| 02/11 | Mosaico já publicado fica como está (post publicado não troca imagem); regra de grade 3:4 vale daqui pra frente |
| 02/11 | Perfil: descrição nova sem foco em WhatsApp; título da bio "Sua empresa atende, agenda e cobra sozinha" |
| 02/11 | Tráfego pago: teto de R$ 400 até 25/11; depois cerca de R$ 1.000 por mês |
| 02/11 | Sem técnicas ocultas de engajamento; alcance por recursos oficiais (Reel de teste, collab, anúncios) |
| 02/11 | Publicador social vira módulo do portal, separado por cliente, via API interna |
| 02/11 | Mini relatório de pendências sempre que algo ficar pendente; tudo registrado neste vault |
| 02/11 | Voz oficial passa a ser a Carla (versão mais animada); V7 refeita com ela, para 03/11 às 18h |
| 02/11 | Recarga pré-paga de R$ 81 na conta de anúncios (saldo ≈ R$ 94,07); conta do teto de R$ 400 até 25/11: R$ 81 usados, faltam R$ 319 |
| 02/11 | V7: pronúncia "Malvôra" corrigida e abertura com gancho visível no 1º quadro ("Qual das duas fica com o cliente?") e fala em 1 s |
| 02/11 | Erro no cadastro VIP: a IA gerou byte nulo (\u0000) no título e a API do portal deu 500. Corrigido no n8n (Mod_Demandas_Acoes limpa caracteres de controle); correção central no portal sugerida como tarefa |

## 03/11 · Malu não agenda nada; suporte só por chamado no portal
- Até o lançamento (10/11): nenhum serviço ativo para agendar. A Malu tira dúvidas e faz o cadastro na lista VIP.
- Depois do lançamento: suporte só pelo portal, abrindo chamado. A Malvora **não** oferece suporte por reunião. Por enquanto quem responde é uma pessoa da equipe.
- Texto pós-lançamento da Malu atualizado (`instrucoes-extras-pos-lancamento-base.txt`).

## 04/11 · Respostas do Instagram v4 publicadas (23h43)
- Fluxo `Instagram - Respostas automáticas` (n7Co0LSMRhW1eZfo) lê `ig_respostas_v4` (RCKz1ou9W0VykX74); a v3 fica de cópia. Antes e depois mostrados e aprovados pelo Rapha.
- Novo:
  - críticas, negação e 😢 vão para a equipe;
  - agradecimento, gostou e elogio separados;
  - IA só com até 3 palavras;
  - emoji com emoji;
  - mídia no direct: 1ª e 2ª respondidas, depois só aviso;
  - não repete a frase para a mesma pessoa em 7 dias;
  - VIP tem versão para depois de 10/11.
- Teste: 24 casos simulados (código e casos em `vault/instagram-respostas-v4/`), todos ok. Primeira execução real às 02:45 UTC, com sucesso.
- Para voltar atrás: restaurar a versão anterior no histórico do n8n.

## 05/11 · Malu: cadastro VIP curto (instruções extras v4) aplicado
- Motivo: 8 leads da campanha (04–05/11), só 1 cadastro. Os leads paravam no cadastro de 8 perguntas e no "Confirma?" a mais.
- Agora o cadastro tem 3 perguntas (nome e sobrenome, e-mail, empresa e ramo). Abre o cadastro na hora, sem confirmação, e as perguntas de qualificação ficam opcionais, depois do cadastro. "ok" não conta como resposta, o e-mail da pessoa não é repetido e ela nunca diz "avisei a equipe".
- Aplicado pelo acesso da equipe (2.913 caracteres; os outros campos não mudaram). Arquivo: `conteudo/lancamento-2026-11-10/malu/instrucoes-extras-v4.txt`.
- Medir: taxa de cadastro dos próximos leads (antes: 1 de 8).

## 14/11 · Direct do Instagram: lê todas as mensagens novas e respeita o cupom já enviado
- Motivo: @nanniunhasofc (anúncio QUERO CUPOM) mandou "Quero cupom · meu negócio é:" e, 9 s depois, "Manicure". O fluxo só lia a última mensagem, não mandou o cupom e a IA disse que ia "confirmar com a equipe". O Raphael mandou o cupom à mão.
- Agora (fluxo `n7Co0LSMRhW1eZfo`, aprovado pelo Raphael): a palavra-chave vale em qualquer mensagem nova desde a nossa última resposta; texto sem letras do nosso alfabeto (spam, outro idioma) só é registrado, sem resposta (status `ignorado`); prompt: cupom já enviado vale (não encaminha), exemplo do ramo depois do cupom, sem "quantos horários por dia".
- Testes: 11 casos da lógica rodados localmente e 8 conversas no simulador (`dvsTG8XjoEzd9k6L`, prompt atualizado igual ao da produção).
- Contatos manuais: só a manicure (feito pelo Raphael); os demais ficam sem resposta, a pedido dele.
