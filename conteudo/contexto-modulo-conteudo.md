# Módulo Conteúdo · contexto para o chat "Contexto do chat modularizado"

Preparado em 09/10/2026 a partir da sessão "Malvora posts e roteiro semanal", onde montamos à mão, para a própria
@malvora_hub, o processo inteiro que agora vira módulo: pesquisa de referências, plano da semana, criação das peças,
revisão, aprovação e publicação automática no Instagram. Use este arquivo como ponto de partida; os caminhos citados
existem nos repositórios `raphalanalves/test` e `raphalanalves/malvora-core`.

---

## 1. A ideia em uma frase

Um módulo pago do portal em que o cliente da Malvora conversa com uma IA de conteúdo (chat para tomada de decisão),
que pesquisa o nicho dele, propõe a semana, cria as artes e os Reels com a marca dele, mostra tudo para aprovação e
publica no Instagram na hora marcada.

Código sugerido do módulo: `conteudo` (nome comercial a definir: "Conteúdo", "Redes sociais", "Marketing").

## 2. O que já foi provado na prática (piloto com a @malvora_hub)

| Etapa | Como fizemos | Onde está |
|---|---|---|
| Perfil de voz e marca | skill `ig-humanizer --mode profile` + 3 posts reais da conta | `test/.claude/references/voice-profile.md` |
| Plano semanal | skill `ig-content-planner` (pilares, formatos, horários, metas de salvamento/envio) | `test/conteudo/2026-10-semana-12-a-18-roteiro.md` |
| Pesquisa de referências | Apify: Reels mais vistos por termo, legendas completas, tamanho de hashtags (~US$ 0,30 no total) | `test/conteudo/referencias-2026-10-09.md` |
| Criação das peças | HTML + Playwright (PNG 1080×1350) e Reels animados quadro a quadro com ffmpeg (MP4 1080×1920) | `test/conteudo/2026-10-semana-12-18/_fonte/` (`render.js`, `reel-render.js`, `engine.js`, `base.css`, `logo.js`) |
| Revisão das peças | skills `ig-carousel-planner`, `ig-caption-writer`, `ig-humanizer`, `ig-hashtag-strategist` | `test/.claude/skills/`, `test/conteudo/2026-10-semana-12-18/legendas.md` |
| Tela de revisão | página com as artes, os Reels, a legenda e as hashtags de cada dia | https://claude.ai/artifact/KCVXCcPnBnoX2LaH3KvhDP |
| Publicação | n8n + API do Instagram (login do Instagram): fila, publicador a cada 10 min, comentário com hashtags, e-mail de aviso | n8n: `Instagram - Publicador da fila` (ht9Fx0lBKgXwJYOZ), tabela `instagram_fila` (cdCmmhJ4zljwEk4E) |
| Teste da API | criação de container de imagem, carrossel e Reel sem publicar: todos aceitos | n8n: `Instagram - Teste de mídia (não publica)` (syPyPImIumPuDE7V), `Instagram - Diagnóstico do token` (o4rBDmKaZOPMF12X) |

Aprendizados do piloto que viram regra do módulo:
- A API do Instagram aceita só JPG para imagem e precisa de uma **URL pública** para cada arquivo (não recebe upload direto).
- Reel pela API sai com o áudio do próprio arquivo: música em alta só pelo app. Locução própria resolve.
- O token de usuário do Instagram expira (60 dias) e cai se a senha mudar: o módulo precisa renovar e avisar.
- Hashtag de nicho (abaixo de 50 mil posts) é a que dá chance para conta pequena; tamanho medido no Apify.
- Pedido de comentário com palavra-chave ("comenta X") só funciona com entrega automática no direct.
- A logo precisa vir de arquivo oficial do cliente (no piloto usamos `malvora-core/docs/marca`).

## 3. Arquitetura proposta

```
Cliente ─► Portal (tela Conteúdo: chat + quadro da semana + revisão)
              │  (HMAC, mesmo padrão de Mod_Inteligencia_Perguntar)
              ▼
           n8n  Mod_Conteudo_Chat ──► IA (agente com ferramentas)
              │        ├─ pesquisar nicho / concorrente / hashtags ──► Apify (conta da Malvora)
              │        ├─ criar peça ───────────────────────────────► Serviço de render (Playwright + ffmpeg)
              │        ├─ salvar peça / plano ──────────────────────► Core (fn_conteudo_*)
              │        └─ agendar / publicar ───────────────────────► Mod_Conteudo_Publicar ──► API do Instagram
              ▼
     PostgreSQL (Core): só metadados, status, textos, custos, credenciais cifradas
     Armazenamento de objetos (S3 compatível): imagens, vídeos, logos
```

Decisões:
1. **O chat roda no n8n**, como o Inteligência: o portal manda a mensagem com a empresa da sessão, o n8n monta o contexto
   (marca, plano atual, últimas métricas) e chama a IA com ferramentas. Custo registrado por empresa
   (`ia_consumo_mensal`), com limite como o `0037_limite_ia`.
2. **As skills de Instagram viram o conhecimento do agente**: o conteúdo de `test/.claude/skills/ig-*` e
   `test/.claude/references/*` (fórmulas de gancho, regras de voz, regras anti-IA, arquitetura de carrossel,
   heurísticas do algoritmo, estratégia de hashtags) entra como blocos fixos do prompt (cacheáveis), e o perfil
   de voz passa a ser por empresa, no banco.
3. **Serviço de render próprio** (contêiner no mesmo Portainer): recebe um modelo + textos + marca da empresa e devolve
   PNG/JPG/MP4. É o que fizemos em `_fonte/`. Motivo: o Canva só preenche modelos de marca pela API nos planos
   Enterprise e exige que cada cliente conecte a conta dele; o render próprio garante a identidade de cada cliente
   sem depender disso. O Canva fica como **opcional** (seção 5).
4. **Publicação sai do n8n da Malvora** com o token do cliente, guardado cifrado em `tenant_credenciais`
   (mesmo padrão do Asaas e das agendas).

## 4. Onde guardar (resposta ao problema das mídias)

Concordo: mídia não fica no portal nem no banco. Proposta:

| O quê | Onde | Por quê |
|---|---|---|
| Imagens, vídeos, logos e capas | **armazenamento de objetos S3 compatível**, um prefixo por empresa (`tenants/<uuid>/conteudo/...`) | barato, feito para arquivo grande, gera URL pública temporária (assinada) que a API do Instagram consegue baixar |
| Textos, plano, status, agenda de publicação, IDs e links do Instagram, métricas | PostgreSQL do Core, tabelas `conteudo_*` com RLS por `tenant_id` | é dado de negócio, pequeno, precisa de regra e de auditoria |
| Histórico do chat | Core (`conteudo_mensagens`), resumido depois de N dias | dá contexto às próximas conversas sem guardar tudo para sempre |
| Tokens do Instagram e do Canva | `tenant_credenciais` (cifrado com a chave mestra) | o portal não lê; só o n8n |

Opções de armazenamento de objetos (escolher uma):
- **Cloudflare R2**: sem custo de saída de dados (importante, porque o Instagram baixa cada arquivo), URL assinada,
  regras de expiração. Boa escolha se o domínio já está na Cloudflare.
- **Backblaze B2**: barato e S3 compatível.
- **MinIO** no próprio servidor (Portainer): custo zero de serviço, mas o disco e o backup ficam com a Malvora.

Regra de vida dos arquivos (lifecycle):
- rascunho não aprovado: apaga em 30 dias;
- publicado: mantém só a capa em tamanho pequeno para o histórico e apaga o original em 30 a 60 dias (o Instagram já
  guarda a versão publicada);
- logos e modelos da marca: permanentes enquanto a empresa tiver o módulo.

Isso mantém o custo previsível e é coerente com a LGPD (prazo definido, apagar quando sai do módulo).

## 5. Conectores: de quem é cada conta

| Conector | Recomendação | Motivo |
|---|---|---|
| **Instagram** | **conta do cliente**, conectada por OAuth (login do Instagram) no portal | é o perfil dele que publica; token cifrado em `tenant_credenciais` |
| **Apify** | **conta da Malvora**, com custo medido por empresa e limite mensal | cliente não tem e não quer ter conta Apify; o custo é de centavos por pesquisa (~US$ 0,003 por post coletado); dá para cobrar dentro do módulo, como fazemos com a IA |
| **Canva** | **opcional, conta do cliente** (Canva Connect, OAuth) | serve para quem já tem modelos no Canva: a IA cria o design no Canva dele e exporta. Sem Canva, o render próprio faz tudo |
| **IA (texto)** | conta da Malvora (como hoje no Core) | já existe o controle de consumo por empresa |
| **Armazenamento** | conta da Malvora (um bucket, prefixo por empresa) | o cliente não precisa saber que existe |

## 6. Atenção: a Meta precisa aprovar o app antes de abrir para clientes

Hoje o app `MeuAppdeVendas` está em **modo de desenvolvimento** e publica só na conta que é testadora (a @malvora_hub).
Para publicar em contas de clientes:
- **Verificação da empresa** (Business Verification) na Meta;
- **App Review** das permissões `instagram_business_basic`, `instagram_business_content_publish`,
  `instagram_business_manage_comments` (comentário das hashtags) e, para a automação de direct, `instagram_business_manage_messages`;
- política de privacidade e termos públicos (o portal já tem termos), vídeo mostrando o uso de cada permissão;
- enquanto não aprova: piloto com clientes adicionados como **testadores do Instagram** no app (funciona, como fizemos).

Esse é o item de maior prazo (dias a semanas): vale começar em paralelo com o desenvolvimento.

## 7. Modelo de dados (rascunho para a migração)

- `conteudo_marca` (1 por empresa): perfil de voz (tom, bordões, palavras proibidas, regras), público, pilares e pesos,
  cores, fontes, chaves dos arquivos de logo, @ do Instagram, horários preferidos.
- `conteudo_planos`: semana, objetivo, meta de salvamentos + envios, status (proposto, aprovado).
- `conteudo_posts`: plano, tipo (IMAGE, CAROUSEL, REELS, STORY), pilar, fórmula do gancho, objetivo (salvar, enviar,
  comentar, seguir), legenda, primeiro comentário, publicar_em, status (rascunho, em_revisao, aprovado, publicando,
  publicado, erro), media_id e permalink do Instagram, erro, aprovado_por, aprovado_em.
- `conteudo_midias`: post, ordem, chave no armazenamento, tipo, tamanho, largura × altura, duração, expira_em.
- `conteudo_pesquisas`: termo/hashtag/perfil, resultado resumido (JSON), custo, criado_em (cache de 7 dias para não
  pagar duas vezes a mesma pesquisa).
- `conteudo_metricas`: post, alcance, visualizações, salvamentos, envios, comentários, curtidas, seguidores ganhos
  (API de insights do Instagram), coletado_em.
- `conteudo_mensagens`: histórico do chat (papel, texto, ações executadas).
- Consumo: Apify e render entram no consumo do módulo, por empresa, com limite mensal.

Funções no Core (regra de negócio no banco, como o resto do projeto): `fn_conteudo_salvar_post`,
`fn_conteudo_aprovar`, `fn_conteudo_fila` (próximo post vencido e aprovado, com trava para não publicar duas vezes),
`fn_conteudo_marcar_publicado`, `fn_conteudo_marcar_erro`.

## 8. Experiência no portal

Tela **Conteúdo** (seção nova no menu, exige o módulo `conteudo`):
- **Chat** à esquerda, para decidir: "o que posto essa semana?", "pesquisa o que está funcionando para barbearias",
  "faz um carrossel sobre faltas", "troca o gancho do post de quinta", "aprova terça e quinta".
- **Quadro da semana** à direita: um cartão por dia com a prévia (carrossel deslizável, Reel tocando), legenda,
  hashtags, objetivo e status. Botões: Aprovar, Pedir ajuste, Reagendar, Excluir.
- **Primeiro uso**: conectar o Instagram, enviar a logo, responder 5 perguntas (público, o que vende, tom, o que nunca
  dizer, objetivo) e a IA lê os últimos posts da conta para montar o perfil de voz.
- **Depois de publicar**: métricas do post no próprio cartão e um resumo semanal ("o que funcionou, o que mudar").
- Regra de ouro: **nada é publicado sem aprovação** de alguém da empresa com permissão (dono/gerente), e tudo fica
  na auditoria.

## 9. Testes na conta da Malvora (portal, raphael.alves@malvora.com.br)

Concordo com testar tudo na empresa Malvora dentro do portal:
1. Ativar o módulo `conteudo` só para a empresa Malvora (registro em `tenant_modulos`).
2. Conectar a @malvora_hub (já é testadora do app e o token funciona; hoje ele está na credencial `Insta Malvora` do n8n).
3. Migrar a fila do piloto (tabela `instagram_fila` do n8n) para `conteudo_posts` do Core, e o publicador
   `ht9Fx0lBKgXwJYOZ` para `Mod_Conteudo_Publicar` lendo do Core.
4. Subir o bucket (R2 ou MinIO) e o serviço de render.
5. Rodar a semana de 12 a 18/10 de ponta a ponta pelo portal, com aprovação pela tela.

## 10. Fases sugeridas

| Fase | Entrega | Depende de |
|---|---|---|
| 0 | Piloto interno (este chat): semana da Malvora publicada pelo n8n | aprovação dos posts |
| 1 | Módulo no portal só para a Malvora: chat, quadro, aprovação, render, armazenamento, publicação | bucket + serviço de render |
| 2 | 1 a 3 clientes piloto como testadores do app | Fase 1 |
| 3 | Abertura geral | App Review e verificação da Meta |
| 4 | Métricas e aprendizado semanal; automação de direct (palavra-chave → resposta) | permissões de mensagens |

## 11. Perguntas em aberto para decidir

1. Armazenamento: R2, B2 ou MinIO?
2. IA do chat: manter OpenAI (como o Core) ou usar Claude para a escrita das peças (melhor no texto em português e nas
   regras de voz)? Pode ser misto: classificação barata em um, escrita no outro.
3. Preço do módulo e franquia (posts por mês, pesquisas por mês, minutos de render).
4. Canva entra na Fase 1 ou fica para depois?
5. Locução (como a do Sergio) entra como serviço da Malvora ou como upload do cliente?
