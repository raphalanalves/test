# Backlog de integrações · análise inicial (31/10/2026)

Objetivo: decidir quais ferramentas a Malvora passa a integrar ao longo de 2027, começando pelas que mais destravam venda
nos segmentos que estamos atacando (clínicas, estética, barbearias e salões) e pelas que os leads já perguntam.

Status desta análise: **inicial**. A disponibilidade de API e as condições de parceria de cada ferramenta precisam ser
confirmadas na documentação oficial e com o time comercial de cada uma antes de entrar no roadmap.

## 1. O que já integramos (fonte: portal, `_logo_integracao.html`)

| Área | Ferramentas |
|---|---|
| Atendimento | WhatsApp (Evolution), Instagram |
| Agenda | Google Agenda, Outlook, AppBarber |
| Cobrança | Asaas, Mercado Pago |
| Contratos | ZapSign, Autentique |
| Arquivos | Google Drive |
| Localização | Google Maps, Waze |
| Login | Google, Microsoft |
| IA | OpenAI, Claude (internas; não aparecem na comunicação, que fala em tecnologia própria) |

## 2. Sinais de demanda já vistos

- Simulação do direct (30/10): pergunta "Tem integração com o Trinks?". Hoje a IA encaminha para a equipe.
- Segmentos do catálogo com sistema de gestão próprio e forte (clínicas, salões, barbearias, odontologia): o dono já tem
  agenda em outro sistema e só troca se a Malvora conversar com ele.

## 3. Candidatas, por área

Critérios (1 a 3): **Demanda** (quantos clientes do nosso público usam), **Encaixe** (o quanto melhora o que a IA já faz),
**Esforço** (3 = fácil: API pública e documentada; 1 = difícil ou depende de parceria). Prioridade = soma.

### Agenda e gestão por segmento (maior impacto: a IA marca direto no sistema que o cliente já usa)

| Ferramenta | Segmento | Demanda | Encaixe | Esforço | Total | Observação |
|---|---|---|---|---|---|---|
| Trinks | Salões, estética, barbearias | 3 | 3 | ? | — | Já pedida por lead; verificar acesso à API (parceria?) |
| Booksy | Barbearias, salões | 2 | 3 | ? | — | Forte em barbearia; verificar API |
| Clinicorp | Odontologia | 2 | 3 | ? | — | Verificar API |
| Feegow / iClinic / Amplimed | Clínicas médicas | 2 | 3 | ? | — | Escolher 1 depois de ver qual os primeiros clientes usam |
| Doctoralia | Clínicas, consultórios | 2 | 2 | ? | — | Concorre em agendamento; avaliar se integra ou compete |
| Calendly / Cal.com | Serviços, consultoria | 1 | 2 | 3 | 6 | APIs públicas; bom para advocacia e consultoria |

### Pagamentos e financeiro

| Ferramenta | Demanda | Encaixe | Esforço | Total | Observação |
|---|---|---|---|---|---|---|
| InfinitePay | 3 | 2 | ? | — | Muito usada por barbearia e salão; verificar API de cobrança/Pix |
| PagBank (PagSeguro) | 2 | 2 | 3 | 7 | API pública de cobrança |
| Stone / Ton | 2 | 2 | ? | — | Verificar |
| Banco Inter / Cora (Pix e boleto) | 2 | 2 | 3 | 7 | APIs bancárias de Pix; exige conta PJ do cliente |
| Conta Azul / Omie / Bling | 2 | 2 | 3 | 7 | ERP: lançar a venda depois do pagamento |
| Nota fiscal (NFE.io, eNotas, Focus NFe) | 2 | 2 | 3 | 7 | Emitir NFS-e depois do pagamento |

### Captação e relacionamento

| Ferramenta | Demanda | Encaixe | Esforço | Total | Observação |
|---|---|---|---|---|---|---|
| Instagram Direct (atendimento pela IA) | 3 | 3 | 2 | 8 | Já fazemos para a Malvora; virar produto para o cliente |
| Facebook Messenger | 1 | 2 | 2 | 5 | Mesma base da API do Instagram |
| Google Perfil da Empresa (avaliações) | 3 | 3 | 2 | 8 | Pedido de avaliação depois do atendimento; já existe a chave "avaliacao_google" |
| Meta Lead Ads | 2 | 3 | 2 | 7 | Lead do anúncio cai direto na conversa da IA |
| RD Station / HubSpot / Pipedrive | 1 | 2 | 3 | 6 | CRM para empresas maiores (imobiliária, consultoria) |

### Operação e equipe

| Ferramenta | Demanda | Encaixe | Esforço | Total | Observação |
|---|---|---|---|---|---|---|
| Google Meet / Microsoft Teams (link de reunião na agenda) | 2 | 2 | 3 | 7 | "Reunião online" já aparece no site |
| Slack / Microsoft Teams (alertas para a equipe) | 1 | 2 | 3 | 6 | Alternativa ao alerta por WhatsApp |
| Google Sheets / Excel (importar e exportar) | 2 | 2 | 3 | 7 | Já existe o módulo de importar planilhas |
| iFood | 1 | 1 | 1 | 3 | Fora do nosso foco agora |

## 4. Proposta de ordem (para validar)

1. **1º tri/2027 (o que destrava venda já):** Google Perfil da Empresa (avaliações), Instagram Direct como produto,
   e uma agenda de segmento: **Trinks** se a API for acessível, senão Booksy.
2. **2º tri:** InfinitePay ou PagBank (cobrança), nota fiscal, Meta Lead Ads.
3. **2º semestre:** um sistema de clínica (o mais usado pelos clientes que entrarem), um ERP, CRM.

## 5. Próximos passos da análise

- [ ] Confirmar API e condições de parceria: Trinks, Booksy, InfinitePay, Clinicorp, Feegow.
- [ ] Perguntar aos 10 da lista VIP qual sistema de agenda e de pagamento usam (pode ir na mensagem de boas-vindas).
- [ ] Revisar com o João (CTO) o esforço real de cada uma no nosso stack (n8n + portal).
- [ ] Ver o que concorrentes diretos anunciam como integração.
- [ ] Atualizar a página da bio (órbita de logos) e a IA do direct quando uma integração nova entrar.
