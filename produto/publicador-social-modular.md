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
