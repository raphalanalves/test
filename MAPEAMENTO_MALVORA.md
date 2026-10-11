# Malvora: como o portal está construído, o antes e o depois, e as pendências

Levantamento de 11/10/2026. Base: `malvora-core` (`main` 671b316, o antigo), `malvora-core-portal` (`develop`
2524aa5, o novo) e o n8n de produção (199 workflows lidos pelo MCP). Nada foi alterado para fazer este levantamento.

---

## 1. A regra do jogo do portal novo

O que o Pietro descreveu, confirmado no código:

| | Portal antigo (`malvora-core`) | Portal novo (`malvora-core-portal`) |
|---|---|---|
| Onde fica a regra de negócio | No banco: funções `fn_*` (52 diferentes chamadas pelas telas) e 30 gatilhos | **No Python**, em `portal/malvora_app/services/*` |
| Funções e gatilhos no banco | Sim | **Nenhum.** O banco só guarda dados, com RLS por empresa |
| Como o n8n chega nos dados | Nó Postgres direto no banco (`fn_*` e SQL) | **Só pela API** `/api/core/*` com `X-Malvora-Token` (47 rotas) |
| Estrutura do banco | Migrações SQL `0001`–`0048` | Models SQLAlchemy + Alembic (`portal/migrations`) |
| Banco | PostgreSQL | **Continua PostgreSQL** (o mesmo esquema de tabelas) |

**Atenção a um ponto da explicação:** o portal novo **ainda grava no PostgreSQL**. O que mudou é *quem decide*: antes a
tela chamava `SELECT fn_portal_responder(...)` e o banco aplicava a regra; agora a tela chama
`conversa_svc.responder(...)` e o Python aplica a regra e grava. Não existe mais "chamar o Postgres para fazer a regra".

### Como os dados circulam hoje

```
Tela do portal ──leitura (SQL via psycopg: db.core / db.portal / db.equipe)──────────► PostgreSQL (RLS)
Tela do portal ──ação com regra──► services/*.py ──(SQLAlchemy)──────────────────────► PostgreSQL
n8n ──HTTP /api/core/* (token)──► api_core.py ──► services/*.py ──(SQLAlchemy)──────► PostgreSQL
                                                    └─► efeitos.py (o que eram os gatilhos)
```

### Regras para não mudar o jogo de novo (proposta, para combinarmos com o Pietro)

1. **Toda regra de negócio fica em `services/`.** Tela e `api_core` só recebem a entrada e chamam o serviço.
2. **Nada de `fn_*`, gatilho ou view com regra no banco.** Mudança de estrutura só por revisão Alembic.
3. **O n8n não acessa o banco.** Nenhum nó Postgres novo; só HTTP para `/api/core` (o último que sobrou é a memória da IA).
4. **Efeitos colaterais** (aviso, contrato, cópia por e-mail, histórico de preço) vivem em `services/efeitos.py`, chamados por quem grava.
5. **Código novo usa os models (ORM).** Hoje convivem três jeitos de falar com o banco (abaixo); o código novo não deve criar um quarto.

### Como o código fala com o banco hoje (contagem real)

| Camada | Jeito | Quantidade |
|---|---|---|
| Telas (`*.py` na raiz do app) | SQL escrito à mão via psycopg (`db.core()`, `db.portal()`, `db.equipe()`) | ~310 chamadas em 36 arquivos; 23 telas ainda fazem INSERT/UPDATE/DELETE direto |
| Serviços (`services/*.py`) | SQLAlchemy, mas com SQL escrito à mão (`text(...)`) | ~350 trechos em 20 arquivos |
| `services/efeitos.py` | ORM de verdade (models) | 28 |

Ou seja: a regra saiu do banco, mas o acesso ainda é majoritariamente SQL à mão. Não é errado, mas é o motivo de o
código novo precisar de um padrão (item 5 acima).

---

## 2. Portal: antes × agora

- **As telas são as mesmas.** As 127 rotas de tela do antigo existem no novo, com os mesmos arquivos e templates
  (só 1 template diferente). 22 arquivos de tela estão idênticos; o `db.py` (três conexões psycopg) é idêntico.
- **O que mudou nas telas:** onde a tela chamava uma `fn_*`, agora chama um serviço. Ex.: `telas.py` trocou
  `fn_portal_responder` por `conversa_svc.responder` e `fn_atendimento_devolver_em` por `conversa_svc.devolver_em`.
- **O que é novo:** `api_core.py` (47 rotas para o n8n), `services/` (20 serviços), `models/` (6 arquivos),
  `security.py`, `secrets.py` (cofre AES-GCM), `site.py` (landing em `/`, painel em `/painel`, commit 2524aa5).
- **O que ficou para trás:** os testes. O antigo tinha 287 testes de tela; o novo tem 15 no `develop` (+4 na PR #6).

---

## 3. n8n: antes × agora

O n8n tem 199 workflows. Os do portal Malvora estão em três gerações:

- **Geração 1 (antes do "Modularizado")**: soltos na raiz, usam outro banco (`Postgres_Malvora_Clientes`).
- **Geração 2 ("Modularizado", o portal antigo)**: pasta `Modularizado/*`, nós Postgres no banco do portal. **Desligados.**
- **Geração 3 (portal novo)**: pasta nova (`yx2iYq9acFdCJSwI`), só chamam `/api/core`. **Ligados.**

### 3.1 Os 18 que têm as duas versões (mesmo nome)

| Workflow | Geração 2 (antigo, desligado) | Geração 3 (novo, ligado) | Diferença que importa |
|---|---|---|---|
| Mod_Core_Principal | `BGNmCT9R4F1Yvcnl` (Core) | `5JKStm5bBKbosCum` | ainda usa memória Postgres no novo |
| Mod_Core_Acoes | `ZhNOTWpmMNwhrle8` (Core) | `3i8BpsOjisSyXyL2` | — |
| Mod_Core_Guardrails | `WMjf9AbCWl26Wb9O` (Core) | `12048yKXaEEEVuqG` | — |
| Mod_Core_ConsumoIA | `wd0jQvRO54Nlx6gt` (Consumo IA) | `3FJJXDUcw5tvUDxj` | fuso America/New_York no novo |
| Mod_Agenda_Acoes | `d0idNsUKfSCYlIrC` (Agendamento) | `yHfqgCxI8YzZGQht` | **novo não tem "Webhook: Portal"** |
| Mod_Agenda_Conexao | `2GR7Bb3e4DINRFrv` (Agendamento) | `Xyayrzc5Yym6iUTR` | — |
| Mod_Agenda_Sync | `O796ieDkSx6mkCwz` (Agendamento) | `t4lWVUV21wd0DcxX` | — |
| Mod_Pagto_Acoes | `07rT3qPXBex37KBe` (Pagamento) | `rh1KhuAJRZEZf0lU` | **novo não tem "Webhook: Portal"** |
| Mod_Pagto_ConfigurarConta | `8Pz4frrUFP2NNOhW` (Pagamento) | `oks95cGL40PKskkB` | — |
| Mod_Pagto_WebhookAsaas | `FD1078olt7WZQMXV` (Pagamento) | `NMWMDbAZml9OwRkT` | — |
| Mod_Envio_Processador | `3JNJY2ZMajZy10UI` (Envios) | `P1Ds9kaeiwXZtoR6` | **novo não tem "Webhook: Enviar Agora"** |
| Mod_Lembr_Agendamento | `dCB8ZEbbsokkHFwb` (Lembrete) | `JBlsB02xIi37EKld` | — |
| Mod_Lembr_Pagamento | `o5iqpBpWDpsmZ6tt` (Lembrete) | `79NSdojeFrnFhYUu` | — |
| Mod_Relac_Acoes | `aZTT4VPZYp42caD2` (NPS) | `42aenU7PPZmC5sr9` | — |
| Mod_Relac_Rotinas | `DIWNu6nBm4Pagz9N` (NPS) | `RYGmsvTTXLIPBGsp` | — |
| Mod_Relat_Gerar | `LAe727LBOUmEvR1H` (Relatórios) | `MiYOdP3RnSdaWUPr` | — |
| Mod_Relat_Agendados | — | `xyKlukS9tj5gSANl` | só existe na geração 3 |
| Mod_Util_ResetContato | — | `IpMTZ3Zh4tem4RdZ` | só existe na geração 3 |

### 3.2 Os 7 que só existem na geração 2 (portal novo depende deles e eles estão desligados)

| Workflow | ID (desligado) | O que quebra no portal | Já tem endpoint na API? |
|---|---|---|---|
| Mod_WhatsApp_Conexao | `hhSuw3XvccMefofW` | Configurações › WhatsApp (QR code) e início do teste grátis | sim (`/whatsapp/conexao/*`) |
| Mod_Pagto_ContaPortal | `UBHvgpcCXwsPqs4r` | Configurações › Pagamentos (conectar Asaas) | sim (`/pagamento/conta/*`) |
| Mod_Contratos | `juINRKTQHJ8UUesA` | Configurações › Contratos (ZapSign/Autentique) e envio | **não** |
| Mod_Malvora_Assinatura | `ykwYSenhAQUw7v8R` | Cobrança da assinatura Malvora | **não** |
| Mod_Inteligencia_Perguntar | `r8QTFXCsv1JRl5RV` | "Perguntar à IA" no portal | **não** |
| Mod_Inteligencia_Classificar | `0zWbhG7lpLPKpxRN` | Qualidade das respostas da IA | **não** |
| Mod_Agenda_Ocupacao | `y1C7iYImoGrherKD` | Horários ocupados na agenda externa não bloqueiam slots | **não** |

O código deles está no repositório em `n8n/sdk/*.js`, ainda com nós Postgres (credencial "Modularizado").

### 3.3 Geração 1 que ainda roda e dá erro a cada 10 minutos

| Workflow | ID | Erro |
|---|---|---|
| Agendamento | `T0QIcuEghe8j4B7T` | `function fone_normalizado(text) does not exist` (banco antigo `Postgres_Malvora_Clientes`) |
| Sincronização - Agenda Externa | `ShaXOeS0MdzSBn58` | `invalid_grant`: a conexão Google de um cliente foi revogada |

Ambos são anteriores ao portal. Precisa decidir se algum cliente ainda depende deles; se não, desligar.

---

## 4. Renomear os workflows (aplicado em 11/10: 43 workflows; os ligados continuam ligados)

Hoje 16 pares têm **o mesmo nome**. Proposta, com prefixo no começo para ordenar na lista do n8n:

| Geração | Novo nome | Exemplo |
|---|---|---|
| 3 (portal novo, API) | `[API] <nome>` | `[API] Mod_Core_Principal` |
| 2 (portal antigo, SQL) | `[LEGADO-SQL] <nome>` | `[LEGADO-SQL] Mod_Core_Principal` |
| 2 sem versão nova (os 7 de 3.2) | `[PENDENTE-SQL] <nome>` | `[PENDENTE-SQL] Mod_WhatsApp_Conexao` |
| 1 (pré-portal) | `[GEN1] <nome>` | `[GEN1] Agendamento` |

Por que é seguro: os workflows se chamam por **ID**, não por nome (Execute Workflow e ferramentas da IA usam o ID;
o `Mod_Core_ConsumoIA` lista IDs). Renomear não muda webhook, gatilho nem execução. O que precisa acompanhar:
o `docs/RUNBOOK.md` e os nomes nos JSON de `n8n/workflows/` (o campo `name`), para o Git continuar batendo.

---

## 5. Pendências (consolidado)

Legenda de prioridade: 🔴 bloqueia cliente · 🟠 risco/segurança · 🟡 dívida técnica.

### Portal sem função
| # | Pendência | Prioridade | Depende de |
|---|---|---|---|
| 1 | WhatsApp não conecta pelo portal (sem teste grátis para cliente novo) | 🔴 | converter `Mod_WhatsApp_Conexao` para a API + `PORTAL_WHATSAPP_WEBHOOK_URL` e `PORTAL_ENVIO_WEBHOOK_TOKEN` |
| 2 | Asaas não conecta pelo portal | 🔴 | converter `Mod_Pagto_ContaPortal` + `PORTAL_ASAAS_CONTA_WEBHOOK_URL` |
| 3 | Contratos (ZapSign/Autentique) | 🔴 | endpoints de contratos na API + converter `Mod_Contratos` |
| 4 | Agendar/cobrar pela conversa do portal | 🔴 | portal chamar `services.agenda`/`services.pagamento` direto (sem n8n), ou recriar "Webhook: Portal" |
| 5 | "Enviar agora" (resposta do portal sai em até 1 min, não na hora) | 🟡 | chamar o processador direto ou recriar o webhook |
| 6 | Assinatura Malvora (cobrança do cliente) | 🔴 | API + converter `Mod_Malvora_Assinatura` |
| 7 | Perguntar à IA / qualidade das respostas | 🟡 | `services/ia.py` chamar a OpenAI direto ou converter os 2 workflows |
| 8 | Ocupação da agenda externa | 🟠 | API + converter `Mod_Agenda_Ocupacao` (sem ele pode marcar horário em cima de compromisso do Google/Outlook) |
| 9 | Remarcar com outro profissional (regressão do #78) | 🟡 | portar a migração 0047 para `services/agenda.py` |

### Em andamento
| # | Pendência | Prioridade | Situação |
|---|---|---|---|
| 10 | PR #6: falha da API aparece no n8n, senha nos formulários, reset só para números de teste, 6 endpoints que davam 500 | 🟠 | aberta, CI verde; depois do merge: `RESET_NUMEROS_PERMITIDOS`, credencial Basic Auth e atualizar os 18 workflows |

### Banco e segurança
| # | Pendência | Prioridade |
|---|---|---|
| 11 | `app.is_platform` pode ser ligado pelo próprio `malvora_app` (contorna o RLS) → papel separado | 🟠 |
| 12 | 25 índices que existiam no antigo e não foram recriados | 🟡 (🟠 com 200 empresas) |
| 13 | `0001` gerada por `create_all` (não congelada): coluna nova quebra banco novo | 🟡 |
| 14 | `Webhook Evolution` sem autenticação (mensagem falsa entra como cliente) | 🟠 |
| 15 | Execuções do n8n guardam `client_secret` do Google e tokens em texto → ocultar dados das execuções e trocar o segredo | 🟠 |
| 16 | `Mod_Core_Principal` ainda usa nó Postgres para a memória da IA | 🟡 |

### n8n legado e outros
| # | Pendência | Prioridade |
|---|---|---|
| 17 | Geração 1 dando erro a cada 10 min (`Agendamento`, `Sincronização - Agenda Externa`) → confirmar e desligar | 🟡 |
| 18 | Renomear workflows (seção 4) | 🟡 |
| 19 | "Bertiolli": aviso das 09h quebra todo dia (JSON montado com texto) e a chave da Evolution está escrita no nó | 🟠 |
| 20 | `Mod_Core_ConsumoIA` com fuso America/New_York e DNS público para chamar o próprio n8n | 🟡 |

### Qualidade
| # | Pendência | Prioridade |
|---|---|---|
| 21 | Testes: 19 hoje × 287 no antigo; rodar como `malvora_app` (RLS testado) e como `malvora_owner` nas migrações | 🟡 |
| 22 | Padronizar acesso ao banco no código novo (ORM) e corrigir o comentário obsoleto do `db.py` (fala de `fn_equipe_*`) | 🟡 |
| 23 | RUNBOOK: tirar `pgp_sym_encrypt`, menções a `db/` e `reset_contato.sql`, descrever Docker/GHCR/Portainer | 🟡 |

### Ordem sugerida
1. Merge da PR #6 (fecha 10 e deixa erro aparecer no n8n antes de mexer no resto).
2. Itens 1 e 2 (WhatsApp e Asaas: a API já existe, é converter o workflow).
3. Item 4 e 5 (ações da conversa direto nos serviços, sem n8n: segue a regra do jogo).
4. Itens 3, 6 e 8 (precisam de endpoint novo).
5. Renomear (18) e desligar a geração 1 (17), com o Pietro de acordo.
6. Segurança (11, 14, 15) e índices (12) antes de crescer o número de empresas.
