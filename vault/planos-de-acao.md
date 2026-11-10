# Planos de ação

## 1. Lançamento (10/11/2026, 00h)
- Calendário: `conteudo/plano-postagens-31-10-a-15-11.md`.
- 09/11: trocar as instruções da Malu e as perguntas frequentes (2, 3, 18 a 24) para os textos pós-lançamento;
  salvar em 09/11 para valer em 10/11 (lembrete agendado).
- 10/11 00h05: V15 Três buracos (fixado). 12h: carrossel "30 tipos de negócio" em collab com parceiro.

## 2. Lista VIP
- 10 vagas, 2 vendidas por fora (anônimas). Entrada pela Malu no WhatsApp com texto pronto.
- Malu pré-cadastra como acompanhamento e passa o número. Retomada do cadastro parado em 2 h e 24 h.
- Lista de espera: sorteio de até 2 vagas em 09/11; quem ficar na espera ganha 20% no 1º mês (cupom ESPERAVIP).
- Contador da bio lê a tabela `lista_vip_lancamento`; cada VIP confirmado entra nela.

## 3. Tráfego pago (R$ 400 até 25/11, depois cerca de R$ 1.000 por mês)
| Período | Campanha | Por dia | Total |
|---|---|---|---|
| 04–09/11 | Clique para WhatsApp (Malu), Reel da revelação: completar a lista VIP | R$ 15 | R$ 90 |
| 10–16/11 | Lançamento: V15 levando ao portal, mais anúncio para quem já viu nossos Reels | R$ 30 | R$ 210 |
| 17–25/11 | Só público quente (viu Reels ou visitou o perfil) | R$ 11 | R$ 99 |

A partir de 26/11: 60% gente nova (venda), 25% público quente, 15% impulsionar o melhor post orgânico da semana.

Configuração na Meta (uma vez, com a pessoa digitando login, cartão e códigos): portfólio com página e Instagram,
conta de anúncios BRL e fuso de São Paulo, limite de gasto, WhatsApp da Malu vinculado à página, pixel do portal,
credencial de anúncios direto no n8n. Depois disso o n8n cria e acompanha as campanhas.

Risco a decidir: a Malu roda por integração não oficial do WhatsApp; com volume de anúncio, avaliar a API oficial.

## 4. Portal (a partir de 01/11)
- E-mail automático ao abrir acompanhamento; retomada de cadastro parado; contador da bio automático.
- Corrigir o botão "Excluir" que aparece como primeiro botão nas perguntas frequentes e os outros problemas de tela.
- Ensinar a IA do direct que o cliente não precisa trocar de número (conexão por QR code).

## 5. Publicador social por cliente
Ver `produto/publicador-social-modular.md`. Agora: Reel de teste e prévia de mosaico no piloto da Malvora,
anúncios com teto. Depois do lançamento: API interna do portal, primeiro cliente piloto, revisão do app na Meta.

## 6. Integrações 2027
Ver `produto/backlog-integracoes.md` (InfinitePay, lojas de carros, Google, Microsoft, agendas de segmento).

## Ideia do time (03/11): "Nossos valores"
- Ideia: post "Nossos valores", com a Malvora deixando claro que não é sobre tirar pessoas do trabalho; a IA cuida do repetitivo e a equipe cuida do que precisa de gente. Depois vira um destaque "Valores" no perfil.
- O carrossel da semana toca nesse ponto, mas não é o tema dele.
- Quando: depois do lançamento (semana de 16/11), para não competir com a reta final. Formato sugerido: carrossel de 5 a 6 telas + versão em story para o destaque.
- Status: ideia aprovada pelo Rapha, ainda sem produção.
- Ampliado (03/11): o destaque "Valores" tem mais de um valor, um story por valor. Proposta (o Rapha valida cada um antes de produzir; nada aqui é promessa comercial ainda):
  1. Gente no centro: a IA tira o repetitivo, não as pessoas.
  2. Transparência: preço claro, a IA diz que é assistente virtual e chama a equipe quando precisa.
  3. O dado é do cliente: privacidade e LGPD, a empresa decide o que a IA sabe.
  4. Simples de verdade: o dono configura sem técnico.
  5. Respeito ao tempo do cliente final: resposta na hora, a qualquer hora.
  6. Feito para o pequeno e médio negócio brasileiro.
  7. A gente evolui junto: as sugestões dos clientes viram função no portal.
- Formato: carrossel-manifesto (capa + 1 tela por valor + fecho) e 7 stories que ficam no destaque.

## Ideia do time (04/11): posts com dados do mercado
- Ideia: posts com números do mercado. Exemplo do time: "apenas 1% das barbearias tem os processos automatizados; quem contratar sai na frente".
- **Regra:** só publicar número com fonte verificável (pesquisa, Sebrae, IBGE, relatório de mercado), com a fonte citada no post. Se não houver fonte para o número, usar a pergunta em vez do dado ("quantas barbearias você conhece que respondem o WhatsApp às 23h?").
- Formato sugerido: carrossel "dado + o que isso significa + como sair na frente", uma série por segmento (barbearia, clínica, estética).
- Quando: criação na sexta, 06/11; a data de divulgação fica para depois. Nada é feito antes.
- Status: ideia aprovada pelo Rapha, aguardando a sexta.

## 09/11 · Série "Clientes Malvora" (entrevistas em collab)
- Ideia do Rapha: divulgar as empresas que aderiram por meio de entrevistas gravadas (modelo da Barbearia Numero 1).
- 1 post por semana, em collab com o perfil da empresa. Claude edita os vídeos de divulgação. Começa depois de criarmos o SharePoint de mídias (semana de 16/11).
- Só com autorização escrita da empresa para nome e imagem (resposta "SIM, pode divulgar").
- Primeira: Barbearia Numero 1 (gravação feita; falta receber os vídeos como documento ou Drive).

## 10/11 · Reel "Afinal, o que a Malvora faz?" (par do carrossel 30 negócios)
- Ideia do Rapha (09/11). Produzir em 10/11; publicar junto ou logo depois do carrossel das 12h.
- Roteiro base (Carla): "Afinal, o que a Malvora faz e quem ela atende?". Ela lista 3 ou 4 segmentos com calma (ex.: clínica, salão, barbearia, loja de carros), depois o áudio acelera passando por vários outros, termina com uma respiração ou risada da Carla e fecha com "…e até o seu negócio". Final: "São mais de 30 segmentos prontos. O seu não está na lista? Entra no portal e ajusta do seu jeito."
- Antes de gravar: conferir no portal a quantidade real de segmentos prontos e se a empresa de segmento fora da lista consegue se configurar sozinha (sem número inventado).
- Visual: nomes dos segmentos em corte rápido, sincronizados com a fala; gancho escrito no quadro 0; voz a partir de ~1 s.

## 09/11 · SharePoint de mídias e publicador (validado)
- Site privado "Malvora Marketing" (/sites/malvora-marketing), criado pelo terminal no SharePoint admin center. Pastas e envio dos arquivos: Claude, via Microsoft 365 (conta raphael.alves).
- Pastas da biblioteca: Instagram/01-Aguardando-aprovacao, 02-Aprovados-agendados, 03-Publicados/AAAA-MM, 04-Arquivados; Brutos/Entrevistas/<empresa>, Brutos/Gravacoes; Marca.
- Publicador: o Instagram só aceita mídia por URL pública e o link do SharePoint não serve (abre página, não o arquivo). Desenho: n8n lê o arquivo no SharePoint (app no Entra só com acesso a este site) → copia para o Azure Blob privado com link temporário (SAS de 1 h) → publica → move para 03-Publicados.
- Ordem: 1) site e pastas agora; 2) cópia dos posts; 3) depois de 10/11: app no Entra, Blob, de→para do publicador e teste; 4) só então deixar o repositório privado (as URLs raw param de funcionar).
- Publicador não muda na noite do lançamento.

## 09/11 · Gravações da Barbearia Numero 1 (bastidores) · PAUSADO
- 32 vídeos de 07/11 em SharePoint › Brutos/Gravações (~1,7 GB). Uso duplo: corte rápido de bastidores ("um dia de gravação com cliente VIP") e material de apoio da entrevista completa.
- Análise pausada a pedido do Rapha: ele vai selecionar cada vídeo e dizer o que fazer. Script pronto: ops/analisar-gravacoes.ps1 (folhas de contato + resumo, sem alterar originais; requer ffmpeg no PC).
- Para editar: os vídeos precisam chegar ao Claude por link temporário (Azure Blob), junto da migração do publicador.

## 10/11 · Estrutura do SharePoint (Malvora Marketing › Documentos)
- 01 Conteúdo orgânico: Instagram (01 Aguardando aprovação · 02 Aprovados e agendados · 03 Publicados · 04 Arquivados) e Séries (Alquimias · Entrevistas VIP · Bastidores · Tutoriais do portal · Por dentro da Malvora).
- 02 Campanhas pagas: Barbearias · Salões e estética · Clínicas e odontologia · Institucional (todos os segmentos). Novo segmento = nova pasta.
- 03 Brutos e gravações: Gravações · Entrevistas · Vozes · Acervo do git (09-11-2026).
- 04 Marca. 05 Referências e estudos (Concorrentes · Formatos e técnicas). 06 Planejamento e relatórios (Calendário editorial · Relatórios de desempenho · Roteiros).
- Script ops/copiar-para-sharepoint.ps1 já usa os caminhos novos.
