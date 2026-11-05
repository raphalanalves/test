# Publicador social da Malvora · visão do produto (02/11/2026)

Hoje a Malvora é o piloto em produção: posts, primeiro comentário e respostas no Instagram rodam sozinhos pelo n8n, com
a identidade da marca. Este documento descreve como isso vira um módulo do portal, separado por cliente, sem que um
cliente afete o outro. Não é para executar tudo agora: o foco até 16/11 é o lançamento da Malvora.

## 1. Princípios

1. **Só API oficial da Meta.** Nada de automação pelo app, navegador ou senha do cliente. O que a API não faz, o
   produto não faz.
2. **Sem engajamento artificial.** O publicador não curte, não segue, não comenta em perfis de terceiros e não manda
   direct para quem não puxou conversa. Isso é o que derruba conta e, num produto com um app só para todos os clientes,
   derrubaria o app de todo mundo.
3. **O alcance vem de recursos oficiais e de conteúdo:** Reel de teste (trial reel), collab, horário, palavra-chave na
   fala, na tela, na legenda e no texto alternativo, resposta rápida a comentário e direct, anúncio.
4. **Separação por cliente (tenant):** cada cliente tem a própria conta conectada, o próprio token, a própria fila e o
   próprio limite. Uma falha ou um bloqueio num cliente não para os outros.
5. **O portal é o dono dos dados do cliente.** O n8n lê e grava pelo portal (API interna), nunca direto no banco.
   Exceção: a própria Malvora, que hoje usa as tabelas do n8n e migra para o portal quando o módulo existir.
6. **Sem interação humana na operação.** O humano aprova regras uma vez (identidade, temas proibidos, teto de gasto) e
   pode revisar quando quiser; o dia a dia é automático.

## 2. Módulos

| Módulo | O que faz | Onde roda |
|---|---|---|
| Conexão | O cliente conecta o Instagram (e a página do Facebook) pelo login oficial da Meta; o portal guarda o token criptografado e renova antes de vencer | Portal |
| Identidade | Voz, cores, logo, marca d'água, assinatura, palavras proibidas, segmentos | Portal (cadastro) |
| Calendário | Plano semanal por pilar e objetivo (alcance, engajamento, captação, confiança) | Portal + IA |
| Produção | Gera imagem, carrossel e Reel com a identidade (modelos HTML, voz, música, legenda) | Workers (fila) |
| Revisão | Checagens automáticas antes de publicar: prévia da grade (mosaico), tamanho, legenda, hashtags, termos proibidos | Worker |
| Publicador | Publica no horário pela API, primeiro comentário, Reel de teste quando fizer sentido, registra o link | n8n por tenant |
| Respostas | Comentários e direct com variação e escalonamento para humano | n8n por tenant |
| Anúncios | Cria campanha pela API de Marketing dentro do teto de gasto aprovado pelo cliente; pausa sozinho se o custo passar do limite | n8n + portal |
| Relatório | Alcance, salvamentos, envios, seguidores, leads, custo por lead; sugestões para a semana seguinte | Portal |

## 3. Fluxo de dados

```
Portal (tenant, identidade, calendário, tokens)
   │  API interna (por tenant_id, com chave de serviço)
   ▼
n8n: Publicador / Respostas / Anúncios  ──►  Graph API (Instagram, Facebook, Marketing)
   ▲                                              │
   └──────── webhooks da Meta ◄───────────────────┘
             (roteados pelo id da conta do Instagram → tenant)
```

- Fila de publicação por tenant, com trava (status `publicando`) para não publicar duas vezes.
- Antes de publicar, consultar o limite de publicação da conta (`content_publishing_limit`) e respeitar.
- Backoff em erro 4xx/5xx; três falhas seguidas pausam a fila daquele tenant e avisam a equipe.
- Logs por tenant; nenhum token aparece em log.

## 4. O que a Meta exige para virar produto

- App da Malvora com verificação da empresa (Business Verification).
- Revisão do app (App Review) com acesso avançado para: publicação de conteúdo, comentários, mensagens do Instagram,
  páginas e anúncios (permissões `instagram_business_*`, `pages_*`, `ads_management`/`ads_read`).
- Política de privacidade e exclusão de dados do usuário (já existe a página na bio).
- Direct automático só dentro da janela de 24 h aberta pela pessoa (ou palavra-chave em comentário).

## 5. Ordem sugerida

1. **Agora (piloto Malvora):** Reel de teste pela API no publicador, prévia automática de grade para mosaico,
   anúncios da Malvora com teto de gasto.
2. **Depois do lançamento:** API interna do portal (tenant, identidade, fila) e o publicador lendo dela.
3. **Primeiro cliente piloto:** conexão pelo login oficial, fila e respostas separadas, relatório.
4. **Escala:** revisão do app na Meta, módulo de anúncios para clientes, cobrança do módulo no portal.

## 6. Perfil verificado (Meta Verified) como recurso do módulo · estudo de 03/11/2026

A Malvora assina em 04/11 (R$ 59,90/mês no Brasil, 7 dias grátis) e é o piloto. O que chegar de fato no app é registrado
aqui antes de virar função para os clientes.

**O que a assinatura costuma trazer (varia por país e por plano; confirmar no app da Malvora):**
- Selo de verificado no Instagram e no Facebook.
- Proteção ativa contra perfis que imitam a marca.
- Suporte com pessoa (chat/e-mail; nos planos maiores, mais rápido e por ligação).
- Nos planos de empresa acima do básico: mais destaque na busca e nas recomendações, links clicáveis em Reels (2 a 4 por
  mês), mais endereços e perfis em destaque.

**O que é só pelo app (não tem API):** assinar, o selo, os links em Reels e o suporte. O produto não automatiza nada disso:
orienta e acompanha.

**Como vira módulo para os clientes (proposta, depois do piloto):**
1. Checklist de elegibilidade no portal: conta comercial, autenticação em duas etapas, nome e foto definitivos,
   histórico de posts, documento do responsável, dados da empresa iguais aos do CNPJ.
2. Status do selo por cliente (sem selo, em análise, verificado, perdido) e aviso antes de uma mudança de nome ou foto,
   que pode tirar o selo.
3. Respostas: a IA avisa a equipe quando um perfil parecido com o do cliente aparece nos comentários ou nas menções
   (suspeita de golpe), para o cliente denunciar pela proteção da assinatura.
4. Calendário: se o plano tiver links em Reels, o calendário reserva os do mês para os posts de captação e lembra o
   cliente de pôr o link pelo app.
5. Relatório: alcance e seguidores antes e depois do selo (o piloto da Malvora vira o caso de referência).

## 7. Base de conhecimento do módulo Anúncios (05/11/2026)
O módulo "Anúncios" para clientes nasce das regras de `.claude/skills/meta-ads-malvora` (objetivo por fase, nicho,
filtro de lead, criativo, verba, leitura até o cadastro), apoiadas por `ad-creative`, `paid-ads` e pelas referências do
`claude-ads` (auditoria Meta, verba, conversões, compliance). Tudo é de licença MIT, revisado e listado em
`.claude/skills/TERCEIROS.md`. Para o produto: rascunho por padrão, teto de gasto aprovado pelo cliente, pausa só com
regra aprovada, Conversions API para o evento de conversão do portal e relatório de custo por cadastro.
