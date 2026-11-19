// SMD build – injects smd-data.json into smd-template.html → web/PMS_SMD_Dashboard.html
// Zero dependencies (Node built-ins only). Usage: node smd/build.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const SMD = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(SMD, '..');
const WEB = path.join(SMD, 'web');
const OUT = path.join(WEB, 'PMS_SMD_Dashboard.html');

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
const html = tpl.replace('/*SMD_DATA*/', () => json);

fs.mkdirSync(WEB, { recursive: true });
fs.writeFileSync(OUT, html, 'utf8');
// 1×1 transparent PNG used by the page to detect "opened inside a checkout"
fs.writeFileSync(path.join(WEB, '.smd-anchor.png'), Buffer.from(
  'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=', 'base64'));

const kb = (fs.statSync(OUT).size / 1024).toFixed(1);
console.log(`SMD build OK → ${path.relative(ROOT, OUT)} (${kb} KB)`);
console.log(`Linked paths checked: ${paths.size}; broken: ${broken.length}`);
broken.forEach(p => console.log('  BROKEN LINK:', p));
if (fs.statSync(OUT).size > 2 * 1024 * 1024) console.log('WARNING: output exceeds 2 MB');
process.exitCode = broken.length ? 2 : 0;
