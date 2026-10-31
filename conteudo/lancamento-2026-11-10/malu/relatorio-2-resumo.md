# Malu · lista VIP · configuração de 31/10 (resumo do relatório 2)

- Instruções extras gravadas no servidor (2.886 caracteres, iguais a `instrucoes-extras.txt`), valendo a partir de 01/11.
  A sugestão da revisão da IA foi recusada: vinha cortada e mudava a regra de passar para o Rapha.
- Perguntas frequentes (caminho A): respostas das nº 3, 18, 19, 21, 22 e 24 editadas; nº 20 e 23 sem mudança; nº 25 nova.
- Categorias "Lista VIP" e "Lista de espera": a IA cria no primeiro acompanhamento (não há tela de cadastro).
- Próximo acompanhamento esperado: nº 2.
- Cupom ESPERAVIP20: pendente (precisa da conta de equipe da plataforma).
- QA de conversa: 01/11, pelo celular.

## Problemas de tela para o time do portal (backlog)

1. **Perguntas frequentes:** o primeiro botão de envio de cada formulário é "Excluir"
   (`formaction=/configuracoes/perguntas/<id>/excluir`). Um Enter num campo pode apagar a pergunta. Corrigir: "Salvar"
   como primeiro botão, ou "Excluir" como `type="button"` com confirmação.
2. **IA e empresa:** depois de salvar, a tela diz ao mesmo tempo "A IA já usa as novas informações na próxima mensagem" e
   "a nova versão vale a partir de amanhã". Para os textos de instrução, mostrar só a segunda.
3. **IA e empresa:** o 1º "Salvar" só pede confirmação, mas ao recarregar a tela mostra o rascunho recuperado como se já
   estivesse salvo. Deixar claro que falta confirmar.
4. **Módulos:** a empresa interna aparece com o aviso "Você está no teste grátis".
5. **Plano:** "SAC e suporte técnico" está no nome do pacote, mas o módulo aparece como "disponível".
6. **Revisão da IA:** a sugestão pode vir cortada no fim do texto (perdeu o último parágrafo).

## Lembrete

As instruções só mudam 1 vez por dia e valem no dia seguinte. Para tirar a lista VIP depois do lançamento, salvar a
versão nova em **09/11** (vale em 10/11).
