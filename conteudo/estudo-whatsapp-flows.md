# Estudo · WhatsApp Flows (anotado em 18/10/2026)

Ponto de partida: Reel da [@botconversa sobre Flows](https://www.instagram.com/reel/DeZGBYkxSbE/) (12/10/2026).
A Malvora ainda não tem esse recurso. Este documento guarda o estudo e a ideia de vídeo. **Não produzir o vídeo
antes de o recurso existir.**

## 1. O Reel de referência

Números no Apify: 31,8 mil reproduções, 516 curtidas, **362 comentários** e 90 segundos de vídeo com áudio original.
Os comentários são altos para o alcance porque a legenda pede "COMENTE FLOWS" e entrega o material no direct.

Roteiro, cena a cena (tirado dos quadros do vídeo):

| Momento | Tela | Ideia |
|---|---|---|
| Gancho | "POR MENSAGEM no WhatsApp?" + recibo da Meta "R$ 0,05 por mensagem" | o dono descobre que paga por mensagem |
| Problema | conversa da Carla; "cada mensagem que você manda pra a sua secretária ou o seu agente de IA" | o custo é o mesmo com gente ou com IA |
| Alívio | "as primeiras 1.000 mensagens do mês são DE GRAÇA"; "você NÃO VAI QUEBRAR" | tira o medo |
| Simulador | barra de 350 a 3.000 mensagens → "faixa de R$ 50 a 100" | número concreto |
| Virada | "Uma cotação simples são umas 10, 15 perguntas" → 11 mensagens = R$ 0,55 | onde o dinheiro escapa |
| Solução | "MENOS": conversa de 15 perguntas R$ 0,75 × 1 WhatsApp Flow R$ 0,05 | o Flow junta tudo em uma mensagem |
| Dor 2 | "coisinha por coisinha" (nome, CPF, endereço, horário...); "quando a sua equipe ESQUECE de continuar o atendimento" | conversa longa trava e morre |
| Prova | pedido completo da Mariana (bolo de chocolate, 2 kg, sáb 18/10, Vila Mari); "IMOBILIÁRIA já marca visita" | segmentos se reconhecem |
| CTA | "Comenta FLOWS que a gente te mostra como ativar" | palavra-chave → direct |

O que vale aproveitar: o simulador de custo, o "coisinha por coisinha" com as perguntas orbitando o celular,
os exemplos por segmento e a palavra-chave no comentário (que só faz sentido com a automação de direct no ar).

Cuidado: os números de custo do vídeo (R$ 0,05 por mensagem, 1.000 grátis) parecem ser **a tabela da própria
BotConversa** ou o modelo antigo da Meta. Desde 1º/07/2025 a Meta cobra por mensagem de modelo (template) entregue;
mensagens de atendimento dentro da janela de 24 h que o cliente abre são gratuitas. **Conferir a tabela oficial antes
de usar qualquer valor.**

## 2. O que é um WhatsApp Flow

Um formulário nativo, com telas, que abre dentro da conversa do WhatsApp. O cliente toca num botão, preenche campos
(texto, lista, data, opção, caixa de seleção) em uma ou várias telas e envia. A empresa recebe tudo de uma vez, já
estruturado.

Usos mais comuns:
- agendamento (serviço → profissional → dia → horário);
- pedido e orçamento (produto, quantidade, data, endereço);
- cadastro e pré-atendimento (nome, CPF, convênio, anamnese);
- pesquisa de satisfação e NPS;
- captação de lead em campanha (anúncio → Flow → CRM).

Como funciona por baixo:
- **Flow JSON**: descreve as telas e os campos. Monta-se no editor do WhatsApp Manager ou por API.
- **Dois tipos**:
  - Estático: as opções são fixas, e a resposta chega no webhook quando o cliente envia.
  - Com troca de dados (*data exchange*): a cada tela, o WhatsApp chama um endpoint nosso, criptografado, para buscar
    dados vivos. Exemplo: os horários livres da agenda daquele profissional. A Meta tem um exemplo pronto em Node.js
    de "Book an Appointment".
- **Envio**: como mensagem interativa dentro da janela de 24 h, ou como modelo aprovado para iniciar conversa.
- **Resposta**: chega no webhook como uma mensagem `nfm_reply`, com os campos em JSON.

## 3. Requisito técnico e o buraco na Malvora hoje

- Flows é recurso da **WhatsApp Business Platform (Cloud API oficial da Meta)**.
- O core da Malvora fala com o WhatsApp pela **Evolution API**. No conector Baileys (WhatsApp Web), nem botões
  interativos funcionam direito, e Flows não existe.
- A Evolution tem um conector para a Cloud API. **Não confirmei se ele repassa Flows** (envio e `nfm_reply`). Isso
  precisa de teste.

Caminhos possíveis:

| Caminho | Prós | Contras |
|---|---|---|
| A. Evolution + conector Cloud API | mantém a camada que o core já usa | suporte a Flows incerto; depende da Evolution acompanhar a Meta |
| B. Cloud API direta pelo n8n (HTTP + webhook) | suporte completo, documentação oficial | número do cliente migra para a API oficial (sai do app comum ou vira coexistência); outra integração a manter |
| C. Híbrido: Baileys para a conversa, Cloud API só para quem contratar Flows | não obriga todo cliente a migrar | dois caminhos no core |

Pontos a resolver antes de decidir:
1. O número do cliente pode continuar no WhatsApp Business do celular? A Meta tem o modo **coexistência** (app e API
   no mesmo número). Conferir os limites no Brasil.
2. O custo por cliente: modelos (marketing e utilidade) são pagos por mensagem; atendimento na janela é grátis. Fazer
   uma simulação com os volumes reais de um salão e de uma clínica.
3. A verificação do negócio no Meta Business Manager de cada cliente (o mesmo tema do App Review do módulo de
   conteúdo).
4. O endpoint de troca de dados: onde roda (n8n webhook + Code node para criptografia RSA/AES ou um serviço pequeno
   no core) e como acessa a agenda com RLS por tenant.

## 4. Onde Flows encaixa nos módulos da Malvora

| Módulo | Flow | Ganho |
|---|---|---|
| Base (agenda) | serviço → profissional → dia → horário com os horários livres em tempo real | a IA já marca na conversa; o Flow serve para quem prefere tocar em vez de digitar e para campanhas |
| Base (lembrete da véspera) | "confirmar / remarcar" abrindo as datas livres | remarcação em 2 toques |
| Pagamento | resumo do pedido + forma de pagamento → Pix na conversa | menos ida e volta antes da cobrança |
| Fidelidade | cadastro (nome, aniversário, preferências) | base limpa para campanhas |
| Reativação | "quer voltar?" com os horários da semana | taxa de resposta maior que texto puro |
| Relatório / pesquisa | NPS depois do atendimento | dado estruturado para o relatório |
| Segmentos com orçamento (confeitaria, imobiliária, oficina) | pedido ou visita com todos os campos | o caso do vídeo: 15 perguntas viram uma tela |

A melhor combinação para a Malvora é **a IA conversando e o Flow coletando**: a IA entende o pedido em texto livre e,
quando precisa de muitos campos, manda o Flow já preenchido com o que entendeu.

## 5. Próximos passos de pesquisa (sem prazo)

1. Abrir uma conta de teste na Cloud API com o app da Meta que já temos (MeuAppdeVendas) e um número de teste.
2. Montar um Flow estático de agendamento no WhatsApp Manager e receber a resposta num webhook do n8n.
3. Testar o conector Cloud API da Evolution com o mesmo Flow.
4. Simular o custo por mês para 3 perfis de cliente com a tabela oficial do Brasil.
5. Decidir o caminho (A, B ou C) e levar para o "Contexto do chat modularizado" como um possível módulo ou um recurso
   da base.

## 6. Ideia de vídeo para a Malvora (só quando o recurso existir)

Título de trabalho: **"15 perguntas ou 1 tela?"** · Reel 60-75 s · formato da série animada (motor do Fim da 6x1).

| Tempo | Tela | Fala |
|---|---|---|
| 0-3s | celular com 15 balões de pergunta caindo, um em cima do outro | "Quantas mensagens o seu cliente responde até conseguir fazer um pedido?" |
| 3-15s | as perguntas orbitam o celular: nome, sabor, tamanho, data, endereço... | "Nome. Sabor. Tamanho. Data. Endereço. Uma de cada vez." |
| 15-25s | conversa parada há 2 dias; badge "2" em vermelho | "No meio do caminho alguém some. Às vezes o cliente, às vezes a equipe." |
| 25-40s | o balão vira uma tela de formulário dentro do WhatsApp; os campos se preenchem | "Com o Flow, tudo isso vira uma tela só, dentro da própria conversa." |
| 40-55s | três segmentos passam: confeitaria (pedido), clínica (pré-consulta), imobiliária (visita) | exemplos por segmento, com o nome do negócio na tela |
| 55-65s | a IA da Malvora lê "quero um bolo pra sábado" e manda o Flow já com "sábado" marcado | "A IA entende o pedido e só pergunta o que falta." |
| 65-72s | cartela Malvora com o símbolo se completando | CTA único (link da bio ou palavra-chave, se a automação de direct estiver no ar) |

Regras:
- **Nenhum número de custo** sem a tabela oficial da Meta conferida na semana da publicação.
- Não copiar o visual da BotConversa (fundo claro, recibo da Meta); usar a identidade da Malvora.
- "Comenta FLOWS" só com a automação de direct entregando o material.

## Fontes

- [Meta · WhatsApp Flows (documentação)](https://developers.facebook.com/docs/whatsapp/flows)
- [Meta · Implementing the data exchange endpoint](https://developers.facebook.com/docs/whatsapp/flows/guides/implementingyourflowendpoint)
- [Meta · Pricing on the WhatsApp Business Platform](https://developers.facebook.com/docs/whatsapp/pricing)
- [360dialog · WhatsApp Flows](https://docs.360dialog.com/docs/messaging/interactive-messages/whatsapp-flows)
- [Evolution API · documentação](https://doc.evolution-api.com/)
