# Instagram @malvora_hub · grupos de resposta automática (04/11/2026)

Fluxo: `Instagram - Respostas automáticas` (n8n `n7Co0LSMRhW1eZfo`), a cada 3 min. Tabela de regras: `ig_respostas_v3`.
Cada resposta sorteia uma das frases separadas por "||". A palavra-chave vale como palavra inteira, sem acento e sem maiúscula. A primeira regra que bate ganha.

## Como o fluxo decide (ordem)
1. **Comentário com palavra-chave** → resposta pública (+ direct, se a regra tiver).
2. **Comentário com "?" e sem palavra-chave** → não responde; avisa a equipe no WhatsApp.
3. **Comentário sem palavra-chave** (inclui só emoji) → sorteio genérico (grupo 12).
4. **Direct com palavra-chave** → direct fixo da regra.
5. **Direct sem palavra-chave** → IA (gpt-4.1-mini) com a base da Malvora; se não souber, avisa a equipe.
6. **Direct com mídia** → hoje vai para a IA como "[mídia]" (a IA não vê a mídia). *Proposta de troca abaixo.*

Limites: comentários de até 48 h nos 10 posts mais recentes; direct de até 23 h (janela de 24 h da Meta).

---

## Grupos

### 1. Lista VIP (até 10/11)
- **Palavras:** vip, lista, vaga, vagas · **Onde:** comentário e direct
- **Pública:** Te mandei o link no direct! / Mandei no seu direct 💚 / Olha seu direct, te mandei lá
- **Direct:** "Oi! A lista tem só 10 vagas. Quem entra recebe o acesso na noite do dia 9, antes de todo mundo, e paga metade do preço nos 3 primeiros meses. O cadastro é com a Malu, nossa assistente, no WhatsApp. Leva uns 2 minutos e ela já te passa o seu número na fila: wa.me/5511915074051?text=Quero entrar na lista VIP da Malvora"
- ⚠️ Não tem versão para depois de 10/11: a partir do lançamento, "vip" cai no genérico. Falta criar a versão pós-lançamento ("a lista fechou, agora é teste grátis").

### 2. IA (até 10/11)
- **Palavras:** ia · **Onde:** comentário (CTA dos Reels "comenta IA")
- **Pública:** Te mandei no direct! / Chamei você lá no direct 😉 / Olha seu direct 💚 / Te respondi no direct, dá uma olhada
- **Direct (2 versões):** explica que a Malvora responde o WhatsApp com os preços e horários e marca na agenda; abre 10/11; 10 vagas com metade do preço; link bio.malvora.com.br/lancamento; "Você trabalha com o quê?"

### 3. IA (depois de 10/11)
- Mesmo da 2, trocando a lista pelo "dá pra testar de graça, sem cartão: bio.malvora.com.br".

### 4. Aceso (sempre)
- **Palavras:** aceso · **Onde:** comentário (CTA do V7)
- **Pública:** Aí sim! 👏 / Isso aí, seu cliente agradece 😄 / Boa! Quem responde rápido sai na frente / Que bom! Continua assim 💚
- Sem direct (não vende para quem já está bem).

### 5. Apagado (até 10/11) e 6. Apagado (depois)
- **Palavras:** apagado · **Onde:** comentário
- **Pública:** Relaxa, quase todo mundo tá assim 😅 Te mandei uma ideia no direct / Acontece nas melhores famílias 😅 olha seu direct / Normal, viu? Te chamei no direct
- **Direct:** "Vi que o seu tá apagado 😅 é o mais comum, principalmente à noite e no fim de semana. É isso que a Malvora resolve…" + lista VIP (antes) ou teste grátis (depois).

### 7. Preço (até 10/11) e 8. Preço (depois)
- **Palavras:** preço, preco, valor, quanto custa, planos, plano · **Onde:** comentário e direct
- **Pública:** Te respondi no direct! / Mandei os valores no seu direct 💚 / Olha seu direct, te expliquei lá
- **Direct:** "Os planos começam em R$ 250 por mês, e você só adiciona o que fizer sentido…" + metade do preço na lista (antes) ou teste grátis (depois). "É pra qual tipo de negócio?"
- ⚠️ Confirmar se R$ 250 continua sendo o preço de entrada no lançamento.

### 9. Ansiedade (até 10/11) · NOVO 03/11
- **Palavras:** ansioso, ansiosa, ansiosos, não vejo a hora, contando os dias, já quero, tô esperando, esperando, chega logo
- **Pública:** Falta pouco! 10/11, à meia-noite 🚀 / Tá chegando, já já é dia 10 👀 / A gente também! Meia-noite do dia 10 💚 / Segura mais um pouquinho, falta pouco 😄 / Contagem regressiva ligada ⏳

### 10. Elogio (sempre) · NOVO 03/11
- **Palavras:** top, gênios, gênio, incrível, sensacional, demais, parabéns, show, brabo, braba, lindo, perfeito, maravilhoso, foda, sucesso
- **Pública:** Valeu! Ainda tem muita coisa vindo 💚 / Fico feliz que curtiu! Vem mais aí 👀 / Obrigado de verdade 🙌 / Aaah, valeu! 💜 / Que bom ler isso, obrigado! 💚
- ⚠️ "demais" pode pegar crítica ("caro demais"). Sai no próximo ajuste do fluxo.

### 11. Agradecimento (sempre) · NOVO 03/11
- **Palavras:** obrigado, obrigada, valeu, amei, adorei, gostei, curti
- **Pública:** A gente que agradece! 💚 / Que bom que gostou 😄 / Valeu por estar com a gente! / 💜 Obrigado por acompanhar

### 12. Genérico (sem palavra-chave, inclui só emoji)
- **Pública:** Valeu demais! 💚 / Obrigado! 🙌 / Que bom que curtiu! 💜 / Valeu pelo carinho! / Fica de olho que vem mais por aí 👀 / 💜💚
- ⚠️ É o que mais repete. Proposta: separar "só emoji" (responder com emoji variado) e não repetir a mesma frase para a mesma pessoa em 7 dias.

---

## Maturidade (resumo)

| Situação | Suporte hoje | Nota |
|---|---|---|
| Comentário com CTA (IA, aceso, apagado, VIP, preço) | ✅ completo, com versão antes/depois de 10/11 | 8/10 |
| Elogio, ansiedade, agradecimento | ✅ desde 03/11 | 7/10 |
| Só emoji | 🟡 genérico, repete | 4/10 |
| Pergunta nos comentários | 🟡 não responde, só avisa a equipe | 6/10 (seguro, mas lento) |
| Crítica / reclamação no comentário | 🔴 sem regra: pode cair no genérico com "Valeu!" | 2/10 |
| Direct em texto | ✅ IA com base e regras; encaminha o que não sabe | 8/10 |
| Direct com mídia | 🔴 responde sem ver | 2/10 → proposta abaixo |
| Spam / golpe / perfil falso nos comentários | 🔴 sem regra | 1/10 |
| Pós-lançamento | 🟡 IA, aceso, apagado e preço prontos; VIP sem versão | 6/10 |

## Proposta para mídia no direct (sem ver a mídia)
Varia pela quantidade de mídias seguidas da mesma pessoa. Sempre avisa a equipe no WhatsApp.

- **1ª mídia** (sorteia uma):
  - "Oi! Vi que você me mandou uma mídia, mas por aqui eu não consigo abrir 😕 Já passei pra equipe te responder. Se quiser mais rápido, me chama no WhatsApp que lá eu vejo foto e áudio: wa.me/5511915074051"
  - "Recebi aqui! Só que foto e áudio eu não consigo ver pelo direct. Já avisei a equipe, e se preferir, no WhatsApp eu consigo ver tudo e seguimos por lá: wa.me/5511915074051"
  - "Opa, chegou uma mídia que eu não consigo abrir por aqui. Já deixei com a equipe pra te responder. Se puder me contar em texto, eu já te ajudo agora 🙂"
- **2ª mídia seguida:** "Essa também não abriu por aqui 😅 A equipe já está sabendo e vai te responder. Se for mais fácil, me manda no WhatsApp: wa.me/5511915074051"
- **3ª em diante:** não responde de novo (evita parecer robô e a Meta ler como spam); só reforça o aviso para a equipe.
- **Figurinha ou reação:** não entra nessa regra; segue como emoji (resposta curta, sem link).

Por que fica dentro das regras da Meta: só responde quem escreveu primeiro, dentro da janela de 24 h, uma resposta por mídia, no máximo 2 seguidas, sem mensagem em massa e sem forçar link.
