const cfg = $('Configuração').first().json;
const agora = Date.now();
const resp = $('Ler respostas').all().map(i => i.json)
  .filter(r => r && r.palavras && r.ativo !== false && (!r.valida_de || Date.parse(r.valida_de) <= agora) && (!r.valida_ate || Date.parse(r.valida_ate) > agora))
  .sort((a, b) => (Number(a.ordem) || 0) - (Number(b.ordem) || 0));
const hist = $('Ler histórico').all().map(i => i.json).filter(h => h && h.status !== 'simulado');
const feitos = new Set(hist.map(h => h.item_id).filter(Boolean));
const norm = s => String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
const limpa = s => ' ' + norm(s).replace(/[^a-z0-9 ]/g, ' ').replace(/\s+/g, ' ').trim() + ' ';
const palavrasDe = s => limpa(s).trim().split(' ').filter(Boolean);
const grupo = g => resp.find(r => r.grupo === g);
const especial = p => String(p).trim().startsWith('#') || String(p).trim() === '*';
const NEG = /(^| )(nao|nunca|nada|nem|jamais)( |$)/;
function achar(texto, onde) {
  const t = limpa(texto), n = palavrasDe(texto).length;
  for (const r of resp) {
    if (especial(r.palavras) || !String(r.onde || '').includes(onde)) continue;
    if (r.max_palavras && n > Number(r.max_palavras)) continue;
    for (const p of String(r.palavras).split(',').map(x => limpa(x).trim()).filter(Boolean)) {
      if (t.includes(' ' + p + ' ')) return r;
    }
  }
  return null;
}
// frases já usadas para esta pessoa nos últimos 7 dias (não repetir)
function usadas(user) {
  const s = new Set();
  for (const h of hist) {
    if (h.usuario !== user) continue;
    const quando = Date.parse(h.createdAt || '') || agora;
    if (agora - quando > 7 * 864e5) continue;
    if (h.resposta_publica) s.add(h.resposta_publica.trim());
    if (h.resposta_direct) s.add(h.resposta_direct.trim());
  }
  return s;
}
const usadasAgora = {};
function pick(opcoes, user) {
  const v = String(opcoes || '').split('||').map(x => x.trim()).filter(Boolean);
  if (!v.length) return '';
  const ja = usadas(user); for (const x of (usadasAgora[user] || [])) ja.add(x);
  const livres = v.filter(x => !ja.has(x));
  const esc = (livres.length ? livres : v)[Math.floor(Math.random() * (livres.length ? livres.length : v.length))];
  (usadasAgora[user] = usadasAgora[user] || []).push(esc);
  return esc;
}
const soEmoji = s => !!String(s || '').trim() && norm(s).replace(/[^a-z0-9]/g, '') === '';
const saida = [];
const alerta = (base, titulo) => saida.push({ ...base, acao: 'alerta', resposta_publica: '', resposta_direct: '', aviso: titulo + '\n@' + base.usuario + ': ' + base.texto + '\n\nResponda pelo app.' });
// comentários dos posts recentes (até 48 h)
for (const m of ($('Buscar comentários').first().json.data || [])) {
  for (const c of ((m.comments && m.comments.data) || [])) {
    const user = (c.from && c.from.username) || c.username || '';
    if (feitos.has(c.id) || user === cfg.minha_conta) continue;
    if (agora - Date.parse(c.timestamp) > 48 * 3600e3) continue;
    const base = { item_id: c.id, usuario: user, texto: c.text };
    const txt = String(c.text || '');
    if (soEmoji(txt)) {
      const triste = /[😢😭😞😔😡🤬👎💔]/u.test(txt), risada = /[😂🤣😅😆]/u.test(txt);
      if (triste && !risada) { alerta({ ...base, tipo: 'comentario_sensivel' }, '⚠️ Comentário que pode ser negativo no Instagram'); continue; }
      const g = grupo(risada ? 'emoji_risada' : 'emoji') || grupo('generico');
      if (g) saida.push({ ...base, acao: 'comentario', tipo: 'comentario_emoji', resposta_publica: pick(g.resposta_publica, user), resposta_direct: '' });
      continue;
    }
    const r = achar(txt, 'comentario');
    const temNeg = NEG.test(limpa(txt));
    if (r && r.acao === 'equipe') { alerta({ ...base, tipo: 'comentario_critica' }, '⚠️ Crítica ou reclamação nos comentários do Instagram'); continue; }
    if (temNeg && (!r || r.positivo)) { alerta({ ...base, tipo: 'comentario_negacao' }, '⚠️ Comentário com "não" no Instagram (pode ser negativo)'); continue; }
    if (r) { saida.push({ ...base, acao: 'comentario', tipo: 'comentario', resposta_publica: pick(r.resposta_publica, user), resposta_direct: pick(r.resposta_direct, user) }); continue; }
    if (/\?/.test(txt)) { alerta({ ...base, tipo: 'comentario_pergunta' }, '💬 Pergunta nos comentários do Instagram'); continue; }
    const g = grupo('generico');
    if (g) saida.push({ ...base, acao: 'comentario', tipo: 'comentario_geral', resposta_publica: pick(g.resposta_publica, user), resposta_direct: '' });
  }
}
// direct: última mensagem de cada conversa, se for do cliente e dentro de 24 h
for (const cv of ($('Buscar direct').first().json.data || [])) {
  const msgs = (cv.messages && cv.messages.data) || [];
  const ult = msgs[0];
  if (!ult || !ult.from || ult.from.id === cfg.ig_id || ult.from.username === cfg.minha_conta) continue;
  if (feitos.has(ult.id) || agora - Date.parse(ult.created_time) > 23 * 3600e3) continue;
  const user = ult.from.username || '';
  const texto = ult.message || '[mídia]';
  const base = { item_id: ult.id, usuario: user, texto, recipient_id: ult.from.id, resposta_publica: '' };
  const figurinha = !ult.message && /sticker|like_heart|reaction/i.test(JSON.stringify(ult.attachments || ult.sticker || ''));
  if (figurinha || (ult.message && soEmoji(ult.message))) {
    const g = grupo('direct_emoji');
    if (g) { saida.push({ ...base, tipo: 'direct', acao: 'direct_fixo', resposta_direct: pick(g.resposta_direct, user) }); continue; }
  }
  if (!ult.message) {
    // mídia: conta quantas mídias desta pessoa já tratamos nas últimas 24 h
    const n = hist.filter(h => h.usuario === user && h.tipo === 'direct_midia' && agora - (Date.parse(h.createdAt || '') || agora) < 24 * 3600e3).length;
    const aviso = { ...base, tipo: 'direct_midia_aviso', acao: 'alerta', resposta_direct: '', aviso: '📎 Mídia no direct do Instagram (' + (n + 1) + 'ª seguida)\n@' + user + ' mandou foto, áudio ou vídeo. A IA não consegue ver.\n\nResponda pelo app.' };
    const g = grupo(n === 0 ? 'midia_1' : 'midia_2');
    if (n <= 1 && g) saida.push({ ...base, tipo: 'direct_midia', acao: 'direct_fixo', resposta_direct: pick(g.resposta_direct, user) });
    saida.push(aviso);
    continue;
  }
  const historico = msgs.slice().reverse().map(x => (x.from && x.from.id === cfg.ig_id ? 'Malvora: ' : 'Cliente: ') + (x.message || '[mídia]')).join('\n');
  const r = achar(texto, 'direct');
  if (r && r.acao !== 'equipe' && r.resposta_direct) saida.push({ ...base, tipo: 'direct', acao: 'direct_fixo', resposta_direct: pick(r.resposta_direct, user) });
  else saida.push({ ...base, tipo: 'direct', acao: 'direct_ia', resposta_direct: '', ia_body: { model: cfg.modelo_ia, temperature: 0.3, response_format: { type: 'json_object' }, messages: [ { role: 'system', content: cfg.prompt_ia.replace('{{FASE}}', agora < Date.parse('2026-11-10T03:00:00Z') ? cfg.fase_antes : cfg.fase_depois) }, { role: 'user', content: 'Conversa (mais antiga primeiro):\n' + historico + '\n\nResponda à última mensagem do cliente.' } ] } });
}
return saida.map(j => ({ json: { ...j, modo_teste: cfg.modo_teste, ig_id: cfg.ig_id, alerta_numero: cfg.alerta, instancia: cfg.instancia } }));
