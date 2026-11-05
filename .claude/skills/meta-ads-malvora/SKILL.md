---
name: meta-ads-malvora
description: "Planejar, revisar e ler campanhas pagas da Malvora na Meta (Instagram e Facebook) com as regras do time: objetivo certo por fase (pré-lançamento, lançamento, venda), público por nicho, filtro de lead antes do WhatsApp, checklist do criativo, orçamento e leitura de resultados até o cadastro e a venda. Gera o plano da campanha, o texto do anúncio, o texto pronto do WhatsApp e o prompt para o terminal montar no Gerenciador de Anúncios. Use para criar, trocar, pausar, escalar ou analisar qualquer anúncio da Malvora ou de clientes. Não é para post orgânico (use as skills ig-*)."
---

# Meta Ads · Malvora

O tráfego pago serve para **trazer quem paga**, não quem conversa. Esta skill fecha a lacuna das skills `ig-*`, que só
cuidam do orgânico. Toda campanha passa pelos 6 passos abaixo, e nada vai ao ar sem a aprovação do Rapha.

## Regras fixas (aprendidas em 04–05/11/2026)
1. **Objetivo segue a fase, não o volume.** "Conversas" barata atrai curioso: 8 leads, 1 cadastro, vários sem saber
   o que é a Malvora.
   | Fase | Objetivo | Otimiza para | Destino |
   |---|---|---|---|
   | Pré-lançamento (lista VIP) | Cadastros (formulário instantâneo com pergunta de filtro) ou Mensagens **com filtro** | Lead qualificado | Formulário ou WhatsApp da Malu (…4051) |
   | Lançamento e venda | Vendas | Evento do pixel "iniciou teste" ou "assinou" no portal | Página do teste grátis |
   | Remarketing | Vendas | Mesmo evento | Quem viu 50%+ dos Reels, visitou o perfil ou o site |
   Sem o evento de conversão no portal, a Meta otimiza às cegas: pedir ao Jão o pixel com "iniciou teste".
2. **Um nicho por campanha.** Com verba pequena (até ~R$ 30 por dia), um segmento só; o anúncio fala com ele ("seu
   salão…"). Ordem de teste: salão e estética → barbearia (AppBarber) → clínicas.
3. **Filtrar antes de atender:**
   - texto pronto do WhatsApp com o nicho ("Tenho um salão e quero entender a Malvora");
   - no formulário, a pergunta "Você tem um negócio que atende clientes pelo WhatsApp?";
   - a primeira mensagem da Malu confirma o negócio.
4. **O criativo mostra dor, solução e para quem, nos 3 primeiros segundos.** Vídeo de marca (revelação de logo) não
   vende. Os melhores são os que já performaram no orgânico (alcance, compartilhamentos e salvamentos). Duração de 15
   a 20 s, legenda na tela, preço ou oferta visível, chamada única.
5. **Público.** Idade de 25 a 60; interesses do nicho + empreendedorismo + "administradores de página comercial";
   excluir menores de 24. Depois de 20 cadastros reais, público semelhante (1%) aos cadastrados.
6. **Orçamento.** Não mexer nos 3 primeiros dias (fase de aprendizado). Escalar no máximo 20% a cada 3 dias. Pausar
   anúncio com CPC acima de 2x a média ou sem cadastro depois de R$ 50 gastos no nicho.
7. **Medir até o fim do funil.** O número que vale é **custo por cadastro qualificado** (e, depois, por assinatura),
   não custo por conversa. Cruzar Gerenciador × conversas no portal × Lista VIP no Acompanhamento.
8. **Políticas da Meta.** Nada de promessa de resultado garantido ("dobre suas vendas"), nada de "você" com atributo
   pessoal ("você está falido?"), antes e depois só com prova, sem marca de terceiros. Categoria especial não se aplica.
9. **Não queimar vaga.** Na lista VIP (10 vagas), lead sem perfil não deve entrar: filtro primeiro.
10. **Segurança.** O terminal só lê e monta como rascunho. Publicar, pausar e mudar orçamento só com o "aprovado" do
    Rapha. Nada de cartão, senha ou token no chat.

## Passos
1. **Fase e meta:** pré-lançamento, lançamento ou venda; meta em cadastros ou assinaturas e verba disponível (conferir
   o saldo).
2. **Nicho e público** (regras 2 e 5): o segmento e o porquê, com dados do orgânico quando houver.
3. **Criativo** (regra 4): escolher o vídeo, definir o corte (início, meio, fim) e o texto na tela. Passar o texto do
   anúncio por `ig-humanizer`.
4. **Funil** (regra 3): texto pronto do WhatsApp ou formulário, e conferir se a Malu está pronta (teste de outro
   número com o roteiro do nicho).
5. **Plano para aprovação:** tabela com objetivo, público, criativo, textos, verba e datas, mais os riscos. Esperar o
   "aprovado".
6. **Prompt para o terminal:** montar no Gerenciador de Anúncios como rascunho, conferir, publicar só com o ok, e
   prints antes e depois.

## Leitura de resultados (a cada 2–3 dias)
| Métrica | Bom | Atenção |
|---|---|---|
| CTR no link | > 1,5% | < 0,8%: trocar criativo |
| Custo por conversa | < R$ 5 | > R$ 10 |
| Conversa → cadastro | > 40% | < 20%: problema no filtro ou na Malu, não no anúncio |
| Frequência (7 dias) | < 2,5 | > 3: público cansado, trocar criativo |
Sempre fechar com: o que manter, o que trocar e o que pausar.

## Para clientes (futuro módulo "Anúncios")
As mesmas regras viram o padrão do módulo de anúncios do portal (`produto/publicador-social-modular.md`): teto de gasto
aprovado pelo cliente, pausa automática por custo alto e relatório de custo por cadastro.
