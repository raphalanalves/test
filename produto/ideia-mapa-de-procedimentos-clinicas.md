# Ideia de produto · Mapa de procedimentos para clínicas (anotado em 19/10/2026)

Inspiração: [anúncio do planejador de injetáveis da Clínica Experts](https://www.instagram.com/p/DbGPLNuAwYq/),
publicado pela conta da @dra.mariliaborges (harmonização facial) em 22/07/2026.

**Status: pendência de produto.** Ainda não entra no roadmap do malvora-core; serve de base para a conversa no chat
"Contexto do chat modularizado".

## 1. O que o vídeo mostra

**Números:** 31,8 mil visualizações, 749 curtidas e 29 comentários em 39 s. É um **anúncio pago** (o Apify marca
como `ad`) rodando no perfil da profissional, no formato de parceria em que a marca impulsiona o post da criadora.

**A ferramenta, tela por tela:**
- **Ficha da paciente** à esquerda, com nome, idade e abas por área: Análise facial com IA, Anamnese, Capilar,
  Corporal, Depilação, Estética facial, Facial, Fotos e anexos e Injetáveis.
- **Lista de produtos** com uma cor para cada e o total somando ao lado: toxina botulínica (em U), preenchimento,
  bioestimulador, bioremodelador e skinbooster (em ml).
- **Mapa do rosto** em desenho. A profissional toca no ponto e escolhe a quantidade (0,25 / 0,5 / 1 ml ou unidades).
  Toxina vira ponto com etiqueta; preenchedor vira **vetor** (seta mostrando a direção da aplicação).
- **Histórico:** "o que eu usei na última vez e qual foi o resultado", para planejar o retorno.
- **Apresentar à paciente:** mostra o plano na tela antes de aplicar ("agrega ao meu trabalho").
- Cronômetro do atendimento no rodapé.

**O roteiro do anúncio** segue o gancho G4 ("existe um jeito melhor de planejar") no formato "como eu faço"
(IG10):
- abertura com a frase "Como eu planejo um procedimento facial";
- a profissional falando para a câmera;
- a tela da ferramenta em uso, com a caneta;
- fecho sorrindo: "planejamento é tudo".

Quem vende é a profissional, não a marca. Por isso não parece anúncio.

## 2. A versão da Malvora: o que a gente faz que eles não fazem

A Clínica Experts é um sistema de gestão de clínica. A Malvora já tem o que vem **antes e depois** do procedimento:
- WhatsApp com IA;
- agenda;
- lembrete da véspera;
- Fidelização (retorno e reativação);
- Financeiro com Pix.

O mapa entra como a peça do meio e liga tudo:

| Momento | O que acontece | Módulo que já existe |
|---|---|---|
| Antes | a IA marca a avaliação no WhatsApp e manda a anamnese para a paciente preencher (texto hoje; WhatsApp Flows no futuro) | Base, Agenda |
| Na consulta | a profissional marca os pontos, as quantidades e os produtos no mapa; o sistema soma os totais | **novo** |
| Na hora de fechar | o plano vira orçamento com o preço de cada produto; a cobrança sai no Pix pelo WhatsApp | Pagamento |
| Depois | a paciente recebe o resumo do plano no WhatsApp (só com o consentimento dela) | Base |
| Retorno | o tipo de produto define o próximo contato: revisão da toxina em ~15 dias e manutenção em alguns meses, com o intervalo ajustável pela clínica. A IA chama a paciente na data certa | Fidelização |
| Gestão | custo do produto usado × preço cobrado = margem por procedimento; produto mais usado; pacientes com manutenção vencida | Financeiro, Desempenho |

O argumento de venda: **o mapa lembra a paciente de voltar**. O retorno é onde a clínica de estética ganha dinheiro,
e a Malvora já sabe chamar o cliente no WhatsApp.

## 3. Escopo sugerido

**Primeira versão:**
- Mapa do rosto em SVG (frente) com pontos e vetores; produtos e cores cadastrados pela clínica; quantidade em U ou
  ml; totais por produto.
- Sessões por paciente, ligadas ao cliente e ao agendamento que já existem; abrir a sessão anterior ao lado.
- Lote e validade do produto em cada sessão (rastreabilidade).
- Retorno automático por tipo de produto → mensagem da IA no dia certo.
- Resumo para a paciente (PDF ou imagem) enviado pelo WhatsApp com um toque.

**Depois:**
- Perfil (lateral) e outras áreas: corporal e capilar.
- Fotos antes e depois com comparação lado a lado.
- Termo de consentimento assinado na tela.
- Estoque de produtos: frasco aberto, doses restantes, validade depois de aberto.
- Anamnese pelo WhatsApp Flows.
- Ditado por voz: a profissional fala e a IA preenche o mapa.

## 4. Cuidados (antes de construir)

- **Dado de saúde é dado sensível pela LGPD.** Precisa de base legal própria, acesso só para a equipe clínica,
  registro de quem viu e alterou (a auditoria do portal já existe), criptografia e um termo específico. O RLS por
  empresa que o core já usa ajuda, mas não basta sozinho.
- **Prontuário tem regra de guarda.** Para médicos (CFM) o prazo é longo, e biomédicos, dentistas e esteticistas têm
  conselhos diferentes. Confirmar com um advogado da área quanto tempo guardar e quem pode ver.
- **Fotos não ficam no portal nem no banco.** Mesmo caminho do módulo de conteúdo: armazenamento de objetos (R2 ou
  MinIO) com prefixo por empresa, link assinado e de curta duração, e regras mais rígidas por serem fotos de saúde.
- **A Malvora registra, não indica.** A ferramenta não sugere dose nem ponto. Quem decide é a profissional
  habilitada. A "análise facial com IA" do concorrente fica fora até termos clareza regulatória.
- **Mensagem de retorno** só para paciente que aceitou receber contato.

## 5. Perguntas em aberto

1. Vira um **módulo pago separado** ("Clínica" ou "Estética") ou um adicional do perfil de clínica?
2. Começar só por harmonização facial (injetáveis) ou já prever corporal e capilar?
3. Existe uma clínica parceira para testar e, depois, gravar o vídeo "como eu planejo" com a gente?
4. Qual o formato do resumo para a paciente: PDF, imagem no WhatsApp ou uma página com link?

## 6. Conteúdo (quando a ferramenta existir)

- Repetir o formato do anúncio com uma **profissional real de uma clínica cliente**: "Como eu planejo um
  procedimento facial", com o mapa em uso e a mensagem de retorno chegando no WhatsApp da paciente no fim.
- Gancho G4 ou G1: "Minha paciente voltou na data certa sem eu mandar mensagem."
- Antes disso, um carrossel para o segmento: "O que a sua paciente esquece entre uma aplicação e outra" (G5).
