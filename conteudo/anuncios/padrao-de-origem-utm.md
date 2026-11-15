# Padrão de marcação de origem (UTM) · Malvora (fase 0, 15/11/2026)

Todo link que leva ao portal leva a origem. O portal passa a guardar isso no cadastro na fase 1
(pedido ao Jão de 15/11). Até lá, o cupom de cada campanha identifica a origem.

| Parâmetro | Valores | Exemplo |
|---|---|---|
| `utm_source` | `instagram`, `facebook`, `whatsapp`, `email`, `indicacao` | instagram |
| `utm_medium` | `bio`, `direct`, `stories`, `reels`, `feed`, `anuncio` | anuncio |
| `utm_campaign` | nome curto da campanha, minúsculas e hífen | quero-cupom-1111 |
| `utm_content` | id do criativo: `v5-v2`, `outlook`, `entrevista-n1-ep01` | v5-v2 |

Regras:
1. Minúsculas, sem acento e sem espaço.
2. Um cupom por campanha (ex.: `QUEROCUPOM` = anúncio de 12/11); o cupom também conta como origem.
3. Links em uso:
   - Bio (bio.malvora.com.br): `?utm_source=instagram&utm_medium=bio&utm_campaign=perfil` (aplicado em 15/11).
   - Direct do cupom: link com `?cupom=QUEROCUPOM` (a resposta fixa do n8n não foi alterada; a ferramenta atual não
     edita linhas da tabela `ig_respostas_v4`).
   - Anúncio com destino ao portal (futuro): `?utm_source=instagram&utm_medium=anuncio&utm_campaign=<campanha>&utm_content=<criativo>`.
