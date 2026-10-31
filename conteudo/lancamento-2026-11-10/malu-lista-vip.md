# Lista VIP pela Malu · configuração na empresa interna (contato@malvora.com.br)

Decidido em 31/10:
- O lead entra pela Malu no WhatsApp. O formulário da bio saiu.
- O cadastro fica na empresa interna da Malu: cliente + acompanhamento. Não cria conta para o lead.
- 10 vagas VIP. Duas já estão vendidas por fora, sem nome, e o contador da bio começa em "2 de 10".
- Quem passar das vagas vai para a lista de espera. No dia 09/11 há sorteio de até 2 vagas extras. Quem ficar na espera ganha 20% no 1º mês.
- Retomada do cadastro parado: 2 h e 24 h, e para por aí.
- Mudanças no portal só a partir de 01/11, por causa da cota de PR.

## 1. Texto pronto

Link que abre o WhatsApp da Malu já com a mensagem escrita (usado na bio, na página da lista e nas respostas do Instagram):

```
https://wa.me/5511915074051?text=Quero%20entrar%20na%20lista%20VIP%20da%20Malvora
```

Mensagem que aparece: **"Quero entrar na lista VIP da Malvora"**

Para legendas e Stories: "Manda 'VIP' no direct ou toca no link da bio. A Malu faz seu cadastro em 2 minutos."

## 2. Configuração no portal (empresa da Malu)

### 2.1 Módulo Acompanhamento
Ligar o módulo **Acompanhamento** (`demandas`) na empresa da Malu, se ainda não estiver.
Usar duas categorias:
- **Lista VIP**: as vagas confirmadas.
- **Lista de espera**: quem chega depois que as vagas acabam.

O número do acompanhamento é o número na fila que a Malu informa.
Atenção: a numeração é da empresa toda. Se a empresa da Malu já tiver outros acompanhamentos, o primeiro VIP não será o nº 1. Verificar antes; se for o caso, a Malu fala "seu número de cadastro" em vez de "posição".

### 2.2 Instruções extras da IA (Configurações › IA › Instruções extras)

Colar o texto abaixo (cabe no limite de 3.000 caracteres):

```
LISTA VIP DO LANÇAMENTO (até 10/11/2026, 00h)
Quando a pessoa pedir para entrar na lista VIP (ex.: "Quero entrar na lista VIP da Malvora"), faça o cadastro dela na própria conversa.

1. Agradeça em uma frase e explique: são 10 vagas; quem entra recebe o acesso na noite de 09/11, antes de todo mundo, e paga metade do preço nos 3 primeiros meses.
2. Pergunte UMA coisa por mensagem, nesta ordem, sem formulário e sem lista:
   - nome de quem fala
   - nome da empresa
   - tipo de negócio
   - cidade
   - quantas pessoas atendem clientes
   - e-mail para receber a confirmação
   - quem responde o WhatsApp da empresa hoje
   - qual sistema usa hoje para agenda e para receber pagamentos (pode ser "nenhum")
3. Com tudo respondido, abra um acompanhamento na categoria "Lista VIP" com o título "Lista VIP · <empresa>" e todas as respostas na descrição. Diga o número do cadastro e que a confirmação chega por e-mail.
4. Se a equipe tiver avisado que as vagas acabaram, use a categoria "Lista de espera" e explique: no dia 09/11 sorteamos até 2 vagas extras entre quem está na espera, e quem continuar na espera ganha 20% de desconto no primeiro mês.
5. Se a pessoa parar no meio, não insista na mesma conversa. Quando ela voltar, continue de onde parou, sem repetir as perguntas já respondidas.
6. Não prometa vaga antes de abrir o acompanhamento. Não diga código de cupom. Não fale de preço além de "a partir de R$ 250 por mês" e da condição da lista.
7. Escreva como alguém da equipe: frases curtas, no máximo 1 emoji, sem listas.
```

### 2.3 Perguntas frequentes (Conhecimento)

| Pergunta | Resposta |
|---|---|
| O que ganho na lista VIP? | Acesso na noite de 09/11, antes do lançamento, e metade do preço nos 3 primeiros meses. |
| Quantas vagas? | 10. Depois disso, lista de espera com sorteio de até 2 vagas extras em 09/11. |
| E quem fica na espera? | 20% de desconto no primeiro mês. |
| Preciso pagar agora? | Não. O cadastro é gratuito; a assinatura é feita a partir de 10/11. |
| Quanto custa? | A partir de R$ 250 por mês, com módulos opcionais. |
| Como recebo o acesso? | Por e-mail e aqui no WhatsApp, na noite de 09/11. |

### 2.4 Cupom da lista de espera (Equipe › Preços › Descontos)

| Campo | Valor |
|---|---|
| Código | `ESPERAVIP` |
| Desconto | 20% |
| Mensalidades | 1 (só a primeira) |
| Validade | até 30/11/2026 |
| Limite de usos | 50 (ajustar) |

O código vai por e-mail para quem está na espera. A Malu não fala o código na conversa.

### 2.5 E-mail de confirmação (até a melhoria de 01/11: manual, pelo acompanhamento › "E-mail ao cliente")

Assunto: `Sua vaga na lista VIP da Malvora · cadastro nº {número}`

```
Oi, {nome}!

Recebemos o cadastro da {empresa} na lista VIP da Malvora. Seu número é {número}.

O que vem agora:
- Na noite de 09/11 você recebe o acesso antecipado, por aqui e no WhatsApp.
- Nos 3 primeiros meses da assinatura, você paga metade do preço.

Qualquer dúvida, é só responder este e-mail ou chamar a Malu no WhatsApp.

Equipe Malvora
```

(Lista de espera: trocar o segundo parágrafo por "Você está na lista de espera, nº {número}. No dia 09/11 sorteamos até
2 vagas extras; se não for desta vez, você ganha 20% no primeiro mês com o cupom ESPERAVIP.")

### 2.6 Retomada do cadastro parado (até a melhoria de 01/11: manual)

Na tela de conversas, quem parou no meio recebe:
- **depois de 2 h:** "Oi, {nome}! Ficou faltando só um pouco do seu cadastro na lista VIP. Posso continuar de onde paramos?"
- **depois de 24 h:** "Oi! Só lembrando: as vagas da lista VIP estão acabando. Se quiser terminar o cadastro, é só me responder por aqui."

Depois da segunda mensagem, não insistir mais.

### 2.7 Contador da bio

Hoje o contador lê a tabela `lista_vip_lancamento` do n8n e já conta as 2 vendas diretas.
Cada VIP confirmado pela Malu precisa entrar nessa tabela (eu faço quando você avisar, ou automatizo em 01/11).

## 3. Melhorias no portal (a partir de 01/11)

Recursos gerais, que servem a todos os clientes e não só à Malvora:
1. **E-mail automático ao abrir acompanhamento** de uma categoria escolhida pela empresa, com modelo editável.
2. **Retomada de cadastro parado:** a IA marca a conversa como "cadastro pendente" com os campos que faltam; o portal
   manda as mensagens de retomada no tempo configurado (padrão 2 h e 24 h) e para depois disso.
3. **Webhook ao confirmar VIP**, para atualizar o contador da bio sozinho.

## 4. QA (roteiro de teste)

1. Tocar no botão da bio e conferir se o WhatsApp abre com a mensagem pronta.
2. Mandar a mensagem e responder às perguntas, uma por uma. A Malu não pode repetir pergunta.
3. Parar no meio, voltar depois e conferir se ela continua de onde parou.
4. Conferir no portal o acompanhamento "Lista VIP · {empresa}" com todas as respostas.
5. Mandar o e-mail de confirmação pelo acompanhamento e conferir se chegou.
6. Perguntar "quanto custa?" e "qual o cupom?": ela deve dar a faixa de preço e não dizer o código.
7. Pelo Instagram: mandar "VIP" no direct e conferir se o link da Malu chega.

## 5. Para rodar a configuração e o QA na sua máquina

Você faz o login no portal no navegador, com as suas credenciais e sem passá-las a ninguém. Depois, no terminal, abra o
Claude Code numa pasta qualquer e cole:

```
Abra o navegador (Playwright, modo visível) em https://portal.malvora.com.br e espere eu fazer o login na empresa
interna contato@malvora.com.br. Depois siga o arquivo malu-lista-vip.md (seções 2 e 4): ligue o módulo Acompanhamento,
crie as categorias "Lista VIP" e "Lista de espera", cole as instruções extras da IA, cadastre as perguntas frequentes e o
cupom ESPERAVIP. Antes de salvar cada tela, me mostre o que vai mudar e espere meu ok. No fim, rode o roteiro de QA e
me entregue um relatório com o que passou e o que falhou.
```
