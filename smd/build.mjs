// SMD build – injects smd-data.json and the token logs into smd-template.html → web/PMS_SMD_Dashboard.html (single dashboard, D-96)
// Zero dependencies (Node built-ins only). Usage: node smd/build.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const SMD = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(SMD, '..');
const WEB = path.join(SMD, 'web');
const OUT = path.join(WEB, 'PMS_SMD_Dashboard.html');
const TOKEN_LOG = path.join(ROOT, 'memory', 'usage', 'token-log.csv');
const SESSION_LOG = path.join(ROOT, 'memory', 'usage', 'session-readings.csv');

const data = JSON.parse(fs.readFileSync(path.join(SMD, 'smd-data.json'), 'utf8'));
const tpl = fs.readFileSync(path.join(SMD, 'smd-template.html'), 'utf8');

// 1. validate shape
const REQUIRED = ['meta', 'app', 'people', 'pipelines', 'artifacts', 'stories', 'reviews', 'findings', 'coverage',
  'decisions', 'activity', 'change_requests', 'risks', 'repo_files', 'changes_since_last', 'data_quality'];
const missing = REQUIRED.filter(k => !(k in data));
if (missing.length) { console.error('Schema error – missing keys:', missing.join(', ')); process.exit(1); }
if (!data.pipelines.length || !Array.isArray(data.pipelines[0].stages)) { console.error('Schema error – pipelines[0].stages'); process.exit(1); }
if (!tpl.includes('/*SMD_DATA*/')) { console.error('Template error – placeholder /*SMD_DATA*/ not found'); process.exit(1); }

// 2. check every linked path exists (relative to repo root)
const paths = new Set();
const add = p => { if (p && typeof p === 'string' && !p.startsWith('#')) paths.add(p); };
data.repo_files.forEach(f => add(f.path));
data.artifacts.forEach(a => { add(a.path); (a.files || []).forEach(f => add(f.path)); });
data.decisions.forEach(d => add(d.path));
data.reviews.forEach(r => add(r.path));
data.risks.forEach(r => add(r.path));
data.pipelines.forEach(p => p.stages.forEach(s => s.gate.criteria.forEach(c => add(c.evidence))));
const broken = [...paths].filter(p => !fs.existsSync(path.join(ROOT, p)));

// 3. inject (escape "</script" and U+2028/2029 so the JSON cannot break out of its script tag)
const json = JSON.stringify(data)
  .replace(/<\/(script)/gi, '<\\/$1')
  .split(String.fromCharCode(0x2028)).join('\\u2028')
  .split(String.fromCharCode(0x2029)).join('\\u2029');
// 3b. token utilization per stage › outcome (token-log.csv) and whole-session readings (session-readings.csv) – internal sections (PR-04, D-96)
function parseCsv(txt) {
  const rows = []; let row = [], cur = '', q = false;
  for (let i = 0; i < txt.length; i++) {
    const c = txt[i];
    if (q) { if (c === '"' && txt[i + 1] === '"') { cur += '"'; i++; } else if (c === '"') q = false; else cur += c; }
    else if (c === '"') q = true; else if (c === ',') { row.push(cur); cur = ''; }
    else if (c === '\n' || c === '\r') { if (c === '\r' && txt[i + 1] === '\n') i++; row.push(cur); cur = ''; if (row.some(v => v !== '')) rows.push(row); row = []; }
    else cur += c;
  }
  if (cur !== '' || row.length) { row.push(cur); rows.push(row); }
  const [h, ...body] = rows; return body.map(r => Object.fromEntries(h.map((k, i) => [k.trim(), (r[i] ?? '').trim()])));
}
let tokens = null;
if (fs.existsSync(TOKEN_LOG)) {
  const num = v => (v === '' || v == null ? null : Number(v));
  const eff = r => (num(r.input) || 0) + 2 * (num(r.cache_write) || 0) + 0.1 * (num(r.cache_read) || 0) + 5 * (num(r.output) || 0);
  const rows = parseCsv(fs.readFileSync(TOKEN_LOG, 'utf8'));
  const order = s => (s === 'X' ? 99 : Number(s));
  const stages = {};
  for (const r of rows) {
    const st = stages[r.stage] ??= { stage: r.stage, total: 0, effective: 0, requests: 0, outcomes: {} };
    const o = st.outcomes[r.outcome] ??= { outcome: r.outcome, module: r.module, total: 0, effective: 0, requests: 0, rows: 0, sources: new Set(), last: null };
    const t = num(r.total) ?? ((num(r.input) || 0) + (num(r.cache_write) || 0) + (num(r.cache_read) || 0) + (num(r.output) || 0));
    o.rows++; o.sources.add(r.source || 'measured'); if (!o.last || r.date > o.last) o.last = r.date;
    if (r.source !== 'not-recorded') { o.total += t; o.effective += eff(r); o.requests += num(r.requests) || 0; st.total += t; st.effective += eff(r); st.requests += num(r.requests) || 0; }
  }
  const list = Object.values(stages).sort((a, b) => order(a.stage) - order(b.stage)).map(s => ({ ...s, effective: Math.round(s.effective),
    outcomes: Object.values(s.outcomes).map(o => { const src = [...o.sources]; return { ...o, effective: Math.round(o.effective),
      source: src.length === 1 ? src[0] : src.filter(x => x !== 'not-recorded').join('+'), sources: undefined }; }) }));
  tokens = { built: data.meta.generated_at, total: list.reduce((t, s) => t + s.total, 0), effective: list.reduce((t, s) => t + s.effective, 0),
    measured_rows: rows.filter(r => r.source === 'measured').length, unrecorded_rows: rows.filter(r => r.source === 'not-recorded').length, stages: list, sessions: [] };
}
if (fs.existsSync(SESSION_LOG)) {
  const num = v => (v === '' || v == null ? null : Number(v));
  const eff = r => (num(r.input) || 0) + 2 * (num(r.cache_write) || 0) + 0.1 * (num(r.cache_read) || 0) + 5 * (num(r.output) || 0);
  const by = {};
  for (const r of parseCsv(fs.readFileSync(SESSION_LOG, 'utf8'))) {
    const s = by[r.session] ??= { session: r.session, readings: [] };
    s.readings.push({ date: r.date, checkpoint: r.checkpoint, requests: num(r.requests), input: num(r.input), cache_write: num(r.cache_write),
      cache_read: num(r.cache_read), output: num(r.output), total: num(r.total), effective: Math.round(eff(r)), source: r.source, ref: r.ref, note: r.note,
      split: r.instructions_pct === '' ? null : { instructions: num(r.instructions_pct), files: num(r.files_pct), documents: num(r.documents_pct), conversation: num(r.conversation_pct), other: num(r.other_pct) } });
  }
  tokens ??= { built: data.meta.generated_at, total: 0, effective: 0, measured_rows: 0, unrecorded_rows: 0, stages: [] };
  tokens.sessions = Object.values(by).map(s => ({ ...s, latest: s.readings[s.readings.length - 1] }));
}
const html = tpl.replace('/*SMD_DATA*/', () => json).replace('/*SMD_TOKENS*/', () => JSON.stringify(tokens).replace(/<\/(script)/gi, '<\\/$1'));

fs.mkdirSync(WEB, { recursive: true });
fs.writeFileSync(OUT, html, 'utf8');
// 1×1 transparent PNG used by the page to detect "opened inside a checkout"
fs.writeFileSync(path.join(WEB, '.smd-anchor.png'), Buffer.from(
  'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=', 'base64'));

const kb = (fs.statSync(OUT).size / 1024).toFixed(1);
console.log(`SMD build OK → ${path.relative(ROOT, OUT)} (${kb} KB)`);
if (tokens) console.log(`Token sections (internal – remove manually before sharing with the customer): ${tokens.measured_rows} measured, ${tokens.unrecorded_rows} not recorded outcome row(s); ${tokens.sessions.length} session(s) with readings`);
console.log(`Linked paths checked: ${paths.size}; broken: ${broken.length}`);
broken.forEach(p => console.log('  BROKEN LINK:', p));
if (fs.statSync(OUT).size > 2 * 1024 * 1024) console.log('WARNING: output exceeds 2 MB');
process.exitCode = broken.length ? 2 : 0;
