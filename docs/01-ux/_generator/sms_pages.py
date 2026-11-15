from base import shell

COMMON = r"""
const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], DOW = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
const sh = iso => { const d = new Date(iso + 'T00:00:00'); return DOW[d.getDay()] + ' ' + String(d.getDate()).padStart(2, '0') + ' ' + MON[d.getMonth()]; };
const inr = n => '₹ ' + n.toLocaleString('en-IN', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
const STC = { 'Generated': 'generated', 'Manager Approved': 'mgrapproved', 'Accepted': 'accepted', 'Disputed': 'disputed', 'Voided': 'voided' };
const badge = s => '<span class="badge b-' + STC[s] + '">' + s + '</span>';
"""

# ---------------------------------------------------------------- SCR-SMS-01
S01_HEAD = r"""<div><h1>Salary</h1><p class="lead">Your daily wages, calculated automatically from approved attendance.</p></div>"""

S01_BODY = r"""
<div class="tabs" data-roles="manager"><a href="scr-sms-01-my-salary.html" class="on">My salary</a><a href="scr-sms-02-team-review.html">Team<span class="count">3</span></a></div>
<div class="grid g4" style="margin-bottom:16px">
  <div class="card tile"><div class="k">Earned in period</div><div class="v" id="tE"></div><div class="s">Accepted + manager approved</div></div>
  <div class="card tile"><div class="k">To review</div><div class="v" id="tR" style="color:var(--primary)"></div><div class="s" id="tRs"></div></div>
  <div class="card tile"><div class="k">Waiting for manager</div><div class="v" id="tG"></div><div class="s">Generated, not yet approved</div></div>
  <div class="card tile"><div class="k">Disputed</div><div class="v" id="tD" style="color:var(--danger)"></div><div class="s">With your manager</div></div>
</div>
<div class="toolbar">
  <input class="in" type="date" id="fFrom" value="2026-11-01" style="width:170px" aria-label="From date"><span class="muted">to</span>
  <input class="in" type="date" id="fTo" value="2026-11-16" style="width:170px" aria-label="To date">
  <label class="small" style="display:inline-flex;gap:6px;align-items:center"><input type="checkbox" id="showV"> Show voided</label>
  <span class="small muted" style="margin-left:auto">Rate: ₹ 250.00 / hour</span>
</div>
<div class="bulk" id="bulk"><b id="selCount">0 selected</b><button class="btn primary sm" id="bulkAccept">Accept selected</button><button class="btn sm" id="bulkClear">Clear</button><span class="small muted">Dispute one at a time — a remark is required.</span></div>
<div class="tbl-wrap"><table class="t"><thead><tr><th style="width:36px"><input type="checkbox" id="all" aria-label="Select all records to review"></th><th>Date</th><th>Attendance</th><th class="num">Hours</th><th class="num">Rate (₹/h)</th><th class="num">Amount</th><th>Status</th><th>Notes</th><th class="act">Actions</th></tr></thead>
<tbody id="rows"></tbody><tfoot><tr><td></td><td colspan="4" style="padding:11px 12px;font-weight:600">Total earned in period (excl. voided, disputed, generated)</td><td class="num" id="tot" style="padding:11px 12px;font-weight:600"></td><td colspan="3"></td></tr></tfoot></table></div>
"""

S01_MODAL = r"""
<div class="modal-bg" id="dModal" role="dialog" aria-modal="true" aria-labelledby="dT"><div class="modal"><h2 id="dT">Dispute salary record</h2><p class="small muted" id="dWhat" style="margin-top:-6px"></p>
  <div class="alert info" style="margin-bottom:16px">Your manager will review it. If the attendance was wrong, they reopen it so you can correct it; this record is then voided and a new one is generated.</div>
  <div class="field"><label for="dText" class="req">What is wrong?</label><textarea class="in" id="dText" placeholder="e.g. I left at 17:00, not 18:00."></textarea><div class="err-text" id="dErr" hidden>A remark is required to dispute.</div></div>
  <div class="actions"><button class="btn" id="dNo">Cancel</button><button class="btn danger" id="dYes">Dispute</button></div></div></div>
"""

S01_SCRIPT = COMMON + r"""
const $ = id => document.getElementById(id);
const S = [
  { id: 1, d: '2026-11-02', f: '09:00', t: '17:30', h: 8.5, r: 250, st: 'Accepted' },
  { id: 2, d: '2026-11-03', f: '09:00', t: '18:00', h: 9.0, r: 250, st: 'Voided', note: 'Attendance reopened after dispute (05 Nov). Replaced by the record below.' },
  { id: 3, d: '2026-11-03', f: '09:00', t: '17:00', h: 8.0, r: 250, st: 'Accepted', note: 'Regenerated after correction' },
  { id: 4, d: '2026-11-09', f: '09:00', t: '18:00', h: 9.0, r: 250, st: 'Manager Approved' },
  { id: 5, d: '2026-11-10', f: '09:30', t: '17:30', h: 8.0, r: 250, st: 'Manager Approved' },
  { id: 6, d: '2026-11-11', f: '09:00', t: '17:00', h: 8.0, r: 250, st: 'Manager Approved' }
];
function render() {
  const fr = $('fFrom').value, to = $('fTo').value, sv = $('showV').checked;
  const inP = S.filter(s => s.d >= fr && s.d <= to);
  const rows = inP.filter(s => sv || s.st !== 'Voided').sort((a, b) => b.d.localeCompare(a.d) || a.id - b.id);
  $('rows').innerHTML = rows.map(s => { const v = s.st === 'Voided', rev = s.st === 'Manager Approved';
    return '<tr data-id="' + s.id + '"' + (v ? ' style="color:var(--text-3)"' : '') + '><td>' + (rev ? '<input type="checkbox" class="sel" aria-label="Select ' + sh(s.d) + '">' : '') + '</td>' +
    '<td style="white-space:nowrap;font-weight:500">' + sh(s.d) + '</td><td>' + s.f + '–' + s.t + '</td><td class="num">' + s.h.toFixed(2) + '</td><td class="num">' + s.r.toFixed(2) + '</td>' +
    '<td class="num"' + (v ? ' style="text-decoration:line-through"' : '') + '>' + inr(s.h * s.r) + '</td><td>' + badge(s.st) + '</td><td class="small" style="max-width:240px">' + (s.note || (s.rm ? 'Your remark: "' + s.rm + '"' : '<span class="muted">—</span>')) + '</td><td class="act">' +
    (rev ? '<button class="btn primary sm" data-a="ok">Accept</button><button class="btn danger sm" data-a="dp">Dispute</button>' : '<span class="muted small">—</span>') + '</td></tr>'; }).join('');
  const sum = st => inP.filter(s => st.includes(s.st)).reduce((n, s) => n + s.h * s.r, 0), cnt = st => inP.filter(s => s.st === st).length;
  $('tE').textContent = inr(sum(['Accepted', 'Manager Approved'])); $('tot').textContent = inr(sum(['Accepted', 'Manager Approved']));
  $('tR').textContent = cnt('Manager Approved'); $('tRs').textContent = inr(sum(['Manager Approved'])) + ' to accept or dispute';
  $('tG').textContent = cnt('Generated'); $('tD').textContent = cnt('Disputed');
  $('all').checked = false; sync();
}
function sync() { const n = document.querySelectorAll('.sel:checked').length; $('selCount').textContent = n + ' selected'; $('bulk').classList.toggle('show', n > 0); }
['fFrom', 'fTo', 'showV'].forEach(i => $(i).addEventListener('input', render));
$('all').onchange = e => { document.querySelectorAll('.sel').forEach(c => c.checked = e.target.checked); sync(); };
$('rows').addEventListener('change', e => { if (e.target.classList.contains('sel')) sync(); });
$('bulkClear').onclick = () => { document.querySelectorAll('.sel').forEach(c => c.checked = false); sync(); };
$('bulkAccept').onclick = () => { const ids = [...document.querySelectorAll('.sel:checked')].map(c => +c.closest('tr').dataset.id); ids.forEach(id => S.find(s => s.id === id).st = 'Accepted'); render(); toast(ids.length + ' salary record(s) accepted.'); };
let cur;
$('rows').addEventListener('click', e => { const b = e.target.closest('button[data-a]'); if (!b) return; cur = S.find(s => s.id === +b.closest('tr').dataset.id);
  if (b.dataset.a === 'ok') { cur.st = 'Accepted'; render(); toast('Salary for ' + sh(cur.d) + ' accepted.'); }
  else { $('dWhat').textContent = sh(cur.d) + ' · ' + cur.f + '–' + cur.t + ' · ' + cur.h.toFixed(2) + ' h × ₹ ' + cur.r + ' = ' + inr(cur.h * cur.r); $('dText').value = ''; $('dErr').hidden = true; $('dModal').classList.add('open'); $('dText').focus(); } });
$('dNo').onclick = () => $('dModal').classList.remove('open');
$('dYes').onclick = () => { if (!$('dText').value.trim()) { $('dErr').hidden = false; return; } $('dModal').classList.remove('open'); cur.st = 'Disputed'; cur.rm = $('dText').value.trim(); render(); toast('Dispute sent to Rahul Mehta.'); };
render();
"""


def s01():
    return shell("SCR-SMS-01", "My salary", "salary", "My work / Salary", S01_HEAD, S01_BODY, S01_SCRIPT,
                 roles=("employee", "manager"), default="employee", modal=S01_MODAL)


# ---------------------------------------------------------------- SCR-SMS-02
S02_HEAD = r"""<div><h1>Team salary</h1><p class="lead">Approve your team's generated wages and resolve disputes.</p></div>"""

S02_BODY = r"""
<div class="tabs"><a href="scr-sms-01-my-salary.html">My salary</a><a href="#" class="on">Team</a></div>
<div class="tabs" id="sub" style="border-bottom:0;margin-bottom:8px"><a href="#" class="on" data-t="pending">Needs action<span class="count" id="cP"></span></a><a href="#" data-t="all">All records</a></div>
<div class="toolbar">
  <select class="in" id="fEmp" style="width:220px" aria-label="Employee"><option value="">All team members</option><option>Anita Sharma</option><option>Vikram Singh</option><option>Neha Gupta</option><option>Arjun Rao</option></select>
  <input class="in" type="date" id="fFrom" value="2026-11-01" style="width:170px" aria-label="From date"><span class="muted">to</span>
  <input class="in" type="date" id="fTo" value="2026-11-16" style="width:170px" aria-label="To date">
  <label class="small" style="display:inline-flex;gap:6px;align-items:center"><input type="checkbox" id="showV"> Show voided</label>
</div>
<div class="bulk" id="bulk"><b id="selCount">0 selected</b><button class="btn primary sm" id="bulkApprove">Approve selected</button><button class="btn sm" id="bulkClear">Clear</button><span class="small muted">Generated records can only be approved. If a wage looks wrong, the attendance is the source — fix it there.</span></div>
<div class="tbl-wrap" id="wrap"><table class="t"><thead><tr><th style="width:36px"><input type="checkbox" id="all" aria-label="Select all generated records"></th><th>Employee</th><th>Date</th><th class="num">Hours</th><th class="num">Rate (₹/h)</th><th class="num">Amount</th><th>Status</th><th>Notes</th><th class="act">Actions</th></tr></thead><tbody id="rows"></tbody></table></div>
<div class="card empty" id="empty" style="display:none"><b>Nothing needs action</b>All generated records are approved and there are no open disputes.</div>
<div class="card" style="margin-top:16px" id="sumCard"><h2>Team totals in period</h2><div class="tbl-wrap" style="box-shadow:none"><table class="t"><thead><tr><th>Employee</th><th class="num">Approved hours</th><th class="num">Earned (accepted + manager approved)</th><th class="num">Open items</th></tr></thead><tbody id="sumRows"></tbody></table></div></div>
"""

S02_MODAL = r"""
<div class="modal-bg" id="kModal" role="dialog" aria-modal="true" aria-labelledby="kT"><div class="modal"><h2 id="kT">Resolve dispute: keep as is</h2><p id="kWhat"></p>
  <div class="alert info" style="margin-bottom:16px">Use this when the attendance, and so the wage, is correct. The record goes back to <b>Manager Approved</b> and the employee is asked to accept it again, with your explanation.</div>
  <div class="field"><label for="kText" class="req">Explanation for the employee</label><textarea class="in" id="kText" placeholder="e.g. Badge logs show you left at 18:00."></textarea><div class="err-text" id="kErr" hidden>An explanation is required.</div></div>
  <div class="actions"><button class="btn" id="kNo">Cancel</button><button class="btn primary" id="kYes">Keep as is</button></div></div></div>
<div class="modal-bg" id="roModal" role="dialog" aria-modal="true" aria-labelledby="roT"><div class="modal"><h2 id="roT">Resolve dispute: reopen attendance</h2><p id="roWhat"></p>
  <div class="alert info" style="margin-bottom:16px">The attendance goes back to the employee as <b>Rejected</b> to correct. This salary record becomes <b>Voided</b>; a new one is generated when the corrected attendance is approved.</div>
  <div class="field"><label for="roText" class="req">Remarks for the employee</label><textarea class="in" id="roText">Please correct the out time and resubmit.</textarea></div>
  <div class="actions"><button class="btn" id="roNo">Cancel</button><button class="btn primary" id="roYes">Reopen attendance</button></div></div></div>
"""

S02_SCRIPT = COMMON + r"""
const $ = id => document.getElementById(id);
let tab = 'pending';
const S = [
  { id: 1, emp: 'Vikram Singh', eid: 'EMP0008', d: '2026-11-10', h: 9.0, r: 250, st: 'Disputed', rm: 'I left at 17:00, not 18:00.' },
  { id: 2, emp: 'Neha Gupta', eid: 'EMP0009', d: '2026-11-11', h: 8.5, r: 275, st: 'Generated' },
  { id: 3, emp: 'Arjun Rao', eid: 'EMP0010', d: '2026-11-11', h: 6.0, r: 250, st: 'Generated' },
  { id: 4, emp: 'Anita Sharma', eid: 'EMP0007', d: '2026-11-11', h: 8.0, r: 250, st: 'Manager Approved' },
  { id: 5, emp: 'Anita Sharma', eid: 'EMP0007', d: '2026-11-10', h: 8.0, r: 250, st: 'Manager Approved' },
  { id: 6, emp: 'Anita Sharma', eid: 'EMP0007', d: '2026-11-09', h: 9.0, r: 250, st: 'Manager Approved' },
  { id: 7, emp: 'Vikram Singh', eid: 'EMP0008', d: '2026-11-09', h: 8.0, r: 250, st: 'Accepted' },
  { id: 8, emp: 'Anita Sharma', eid: 'EMP0007', d: '2026-11-03', h: 8.0, r: 250, st: 'Accepted' },
  { id: 9, emp: 'Anita Sharma', eid: 'EMP0007', d: '2026-11-03', h: 9.0, r: 250, st: 'Voided', note: 'Attendance reopened after dispute' },
  { id: 10, emp: 'Anita Sharma', eid: 'EMP0007', d: '2026-11-02', h: 8.5, r: 250, st: 'Accepted' },
  { id: 11, emp: 'Neha Gupta', eid: 'EMP0009', d: '2026-11-02', h: 8.0, r: 275, st: 'Accepted' }
];
const needs = s => s.st === 'Generated' || s.st === 'Disputed';
function render() {
  const e = $('fEmp').value, fr = $('fFrom').value, to = $('fTo').value, sv = $('showV').checked;
  const inP = S.filter(s => (!e || s.emp === e) && s.d >= fr && s.d <= to);
  const rows = inP.filter(s => (tab === 'pending' ? needs(s) : (sv || s.st !== 'Voided'))).sort((a, b) => (b.st === 'Disputed') - (a.st === 'Disputed') || b.d.localeCompare(a.d));
  $('cP').textContent = S.filter(needs).length;
  $('rows').innerHTML = rows.map(s => { const v = s.st === 'Voided';
    return '<tr data-id="' + s.id + '"' + (v ? ' style="color:var(--text-3)"' : '') + '><td>' + (s.st === 'Generated' ? '<input type="checkbox" class="sel" aria-label="Select ' + s.emp + ' ' + sh(s.d) + '">' : '') + '</td>' +
    '<td style="white-space:nowrap"><div style="font-weight:500">' + s.emp + '</div><div class="small muted">' + s.eid + '</div></td><td style="white-space:nowrap">' + sh(s.d) + '</td><td class="num">' + s.h.toFixed(2) + '</td><td class="num">' + s.r.toFixed(2) + '</td>' +
    '<td class="num"' + (v ? ' style="text-decoration:line-through"' : '') + '>' + inr(s.h * s.r) + '</td><td>' + badge(s.st) + '</td><td class="small" style="max-width:220px">' + (s.rm ? 'Employee: "' + s.rm + '"' : s.note || '<span class="muted">—</span>') + '</td><td class="act">' +
    (s.st === 'Generated' ? '<button class="btn primary sm" data-a="ok">Approve</button>' : s.st === 'Disputed' ? '<button class="btn sm" data-a="keep">Keep as is</button><button class="btn primary sm" data-a="ro">Reopen attendance</button>' : '<span class="muted small">—</span>') + '</td></tr>'; }).join('');
  $('wrap').style.display = rows.length ? '' : 'none'; $('empty').style.display = rows.length ? 'none' : '';
  const emps = [...new Set(S.map(s => s.emp))].filter(n => !e || n === e).sort();
  $('sumRows').innerHTML = emps.map(n => { const m = inP.filter(s => s.emp === n && (s.st === 'Accepted' || s.st === 'Manager Approved'));
    return '<tr><td>' + n + '</td><td class="num">' + m.reduce((a, s) => a + s.h, 0).toFixed(2) + '</td><td class="num">' + inr(m.reduce((a, s) => a + s.h * s.r, 0)) + '</td><td class="num">' + inP.filter(s => s.emp === n && needs(s)).length + '</td></tr>'; }).join('');
  $('all').checked = false; sync();
}
function sync() { const n = document.querySelectorAll('.sel:checked').length; $('selCount').textContent = n + ' selected'; $('bulk').classList.toggle('show', n > 0); }
$('sub').addEventListener('click', e => { const a = e.target.closest('a'); if (!a) return; e.preventDefault(); tab = a.dataset.t; document.querySelectorAll('#sub a').forEach(x => x.classList.toggle('on', x === a)); render(); });
['fEmp', 'fFrom', 'fTo', 'showV'].forEach(i => $(i).addEventListener('input', render));
$('all').onchange = e => { document.querySelectorAll('.sel').forEach(c => c.checked = e.target.checked); sync(); };
$('rows').addEventListener('change', e => { if (e.target.classList.contains('sel')) sync(); });
$('bulkClear').onclick = () => { document.querySelectorAll('.sel').forEach(c => c.checked = false); sync(); };
$('bulkApprove').onclick = () => { const ids = [...document.querySelectorAll('.sel:checked')].map(c => +c.closest('tr').dataset.id); ids.forEach(id => S.find(s => s.id === id).st = 'Manager Approved'); render(); toast(ids.length + ' salary record(s) approved. Employees can now review them.'); };
let cur;
$('rows').addEventListener('click', e => { const b = e.target.closest('button[data-a]'); if (!b) return; cur = S.find(s => s.id === +b.closest('tr').dataset.id);
  if (b.dataset.a === 'ok') { cur.st = 'Manager Approved'; render(); toast('Approved. ' + cur.emp + ' can now review it.'); }
  else if (b.dataset.a === 'keep') { $('kWhat').textContent = cur.emp + ' · ' + sh(cur.d) + ' · ' + inr(cur.h * cur.r) + ' · Employee: "' + cur.rm + '"'; $('kText').value = ''; $('kErr').hidden = true; $('kModal').classList.add('open'); $('kText').focus(); }
  else { $('roWhat').textContent = cur.emp + ' · ' + sh(cur.d) + ' · ' + cur.h.toFixed(2) + ' h = ' + inr(cur.h * cur.r) + ' · Employee: "' + cur.rm + '"'; $('roModal').classList.add('open'); } });
$('kNo').onclick = () => $('kModal').classList.remove('open');
$('kYes').onclick = () => { if (!$('kText').value.trim()) { $('kErr').hidden = false; return; } $('kModal').classList.remove('open'); cur.st = 'Manager Approved'; cur.note = 'Kept as is: "' + $('kText').value.trim() + '"'; cur.rm = null; render(); toast('Dispute closed. ' + cur.emp + ' can accept the record.'); };
$('roNo').onclick = () => $('roModal').classList.remove('open');
$('roYes').onclick = () => { $('roModal').classList.remove('open'); cur.st = 'Voided'; cur.note = 'Attendance reopened after dispute'; cur.rm = null; render(); toast('Attendance reopened. Salary record voided.'); };
render();
"""


def s02():
    return shell("SCR-SMS-02", "Team salary review", "salary", "My work / Salary / Team", S02_HEAD, S02_BODY, S02_SCRIPT,
                 roles=("manager",), default="manager", modal=S02_MODAL)


PAGES = {
    "scr-sms-01-my-salary.html": s01,
    "scr-sms-02-team-review.html": s02,
}
