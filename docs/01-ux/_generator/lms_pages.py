from base import shell

COMMON = r"""
const TODAY = '2026-11-16', DOJ = '2025-07-01';
const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
const DOW = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
const d2 = iso => { const d = new Date(iso + 'T00:00:00'); return String(d.getDate()).padStart(2, '0') + ' ' + MON[d.getMonth()] + ' ' + d.getFullYear(); };
const sh = iso => { const d = new Date(iso + 'T00:00:00'); return DOW[d.getDay()] + ' ' + String(d.getDate()).padStart(2, '0') + ' ' + MON[d.getMonth()]; };
const days = (f, t) => Math.round((new Date(t) - new Date(f)) / 864e5) + 1;
const range = (f, t) => f === t ? sh(f) : sh(f) + ' – ' + sh(t);
const badge = s => '<span class="badge b-' + s.toLowerCase() + '">' + s + '</span>';
"""

MY_LEAVE = r"""
const LV = [
  { id: 1, req: '2026-11-14', type: 'Casual', f: '2026-11-23', t: '2026-11-24', st: 'Submitted' },
  { id: 2, req: '2026-10-28', type: 'Earned', f: '2026-12-22', t: '2026-12-26', st: 'Rejected', rm: 'Year-end release week — please pick dates in January.' },
  { id: 3, req: '2026-11-02', type: 'Casual', f: '2026-11-05', t: '2026-11-06', st: 'Approved', by: 'Rahul Mehta' },
  { id: 4, req: '2026-09-15', type: 'Sick', f: '2026-09-14', t: '2026-09-14', st: 'Approved', by: 'Rahul Mehta' },
  { id: 5, req: '2026-08-20', type: 'Earned', f: '2026-10-05', t: '2026-10-07', st: 'Cancelled' },
  { id: 6, req: '2026-07-25', type: 'Earned', f: '2026-08-10', t: '2026-08-14', st: 'Approved', by: 'Rahul Mehta' }
];
"""

# ---------------------------------------------------------------- SCR-LMS-01
L01_HEAD = r"""<div><h1>Leave</h1><p class="lead">Your leave requests. Each request needs your manager's approval.</p></div>
<div><a class="btn primary" href="scr-lms-02-request.html">+ Request leave</a></div>"""

L01_BODY = r"""
<div class="tabs" data-roles="manager"><a href="scr-lms-01-my-leave.html" class="on">My leave</a><a href="scr-lms-03-team-review.html">Team<span class="count">2</span></a></div>
<div class="grid g4" style="margin-bottom:16px">
  <div class="card tile"><div class="k">Casual taken (2026)</div><div class="v" id="tC"></div><div class="s">Approved days</div></div>
  <div class="card tile"><div class="k">Sick taken (2026)</div><div class="v" id="tS"></div><div class="s">Approved days</div></div>
  <div class="card tile"><div class="k">Earned taken (2026)</div><div class="v" id="tE"></div><div class="s">Approved days</div></div>
  <div class="card tile"><div class="k">Pending requests</div><div class="v" id="tP"></div><div class="s">Waiting for Rahul Mehta</div></div>
</div>
<div class="alert info" style="margin-bottom:12px">Leave balances are not tracked in this version. Days are counted as calendar days, from and to inclusive.</div>
<div class="toolbar">
  <select class="in" id="fs" style="width:200px" aria-label="Status"><option value="">All statuses</option><option>Submitted</option><option>Approved</option><option>Rejected</option><option>Cancelled</option></select>
  <select class="in" id="ft" style="width:180px" aria-label="Leave type"><option value="">All types</option><option>Casual</option><option>Sick</option><option>Earned</option></select>
</div>
<div class="tbl-wrap"><table class="t"><thead><tr><th>Dates</th><th>Type</th><th class="num">Days</th><th>Requested</th><th>Status</th><th>Manager remarks</th><th class="act">Actions</th></tr></thead><tbody id="rows"></tbody></table></div>
<div class="card empty" id="empty" style="display:none"><b>No leave requests</b>Use "+ Request leave" to apply.</div>
"""

L01_MODAL = r"""
<div class="modal-bg" id="cModal" role="dialog" aria-modal="true" aria-labelledby="cT"><div class="modal"><h2 id="cT">Cancel leave request?</h2><p id="cWhat"></p>
  <p class="small muted">The request is withdrawn before your manager decides. This cannot be undone; you can submit a new request.</p>
  <div class="actions"><button class="btn" id="cNo">Keep request</button><button class="btn danger" id="cYes">Cancel request</button></div></div></div>
"""

L01_SCRIPT = COMMON + MY_LEAVE + r"""
const $ = id => document.getElementById(id);
function render() {
  const fs = $('fs').value, ft = $('ft').value;
  const rows = LV.filter(l => (!fs || l.st === fs) && (!ft || l.type === ft)).sort((a, b) => b.f.localeCompare(a.f));
  $('rows').innerHTML = rows.map(l => '<tr data-id="' + l.id + '"' + (l.st === 'Cancelled' ? ' style="opacity:.6"' : '') + '><td style="white-space:nowrap;font-weight:500">' + range(l.f, l.t) + ' ' + l.f.slice(0, 4) + '</td><td>' + l.type + '</td><td class="num">' + days(l.f, l.t) + '</td><td class="small muted">' + d2(l.req) + '</td><td>' + badge(l.st) + '</td><td class="small">' + (l.rm ? '"' + l.rm + '"' : '<span class="muted">' + (l.by ? 'Approved by ' + l.by : '—') + '</span>') + '</td><td class="act">' +
    (l.st === 'Submitted' ? '<button class="btn danger sm" data-c>Cancel</button>' : l.st === 'Rejected' ? '<a class="btn sm" href="scr-lms-02-request.html?case=fix">Edit</a>' : '<span class="muted small">—</span>') + '</td></tr>').join('');
  $('empty').style.display = rows.length ? 'none' : ''; document.querySelector('.tbl-wrap').style.display = rows.length ? '' : 'none';
  const sum = t => LV.filter(l => l.type === t && l.st === 'Approved' && l.f >= '2026-01-01').reduce((n, l) => n + days(l.f, l.t), 0);
  $('tC').textContent = sum('Casual'); $('tS').textContent = sum('Sick'); $('tE').textContent = sum('Earned'); $('tP').textContent = LV.filter(l => l.st === 'Submitted').length;
}
let cur;
$('rows').addEventListener('click', e => { if (!e.target.closest('[data-c]')) return; cur = LV.find(l => l.id === +e.target.closest('tr').dataset.id); $('cWhat').textContent = cur.type + ' leave · ' + range(cur.f, cur.t) + ' · ' + days(cur.f, cur.t) + ' days'; $('cModal').classList.add('open'); });
$('cNo').onclick = () => $('cModal').classList.remove('open');
$('cYes').onclick = () => { $('cModal').classList.remove('open'); cur.st = 'Cancelled'; render(); toast('Leave request cancelled.'); };
['fs', 'ft'].forEach(i => $(i).addEventListener('input', render));
render();
"""


def l01():
    return shell("SCR-LMS-01", "My leave", "leave", "My work / Leave", L01_HEAD, L01_BODY, L01_SCRIPT,
                 roles=("employee", "manager"), default="employee", modal=L01_MODAL)


# ---------------------------------------------------------------- SCR-LMS-02
L02_HEAD = r"""<div><h1 id="ttl">Request leave</h1><p class="lead">Full days only. Past dates are allowed, for example for sick leave.</p></div><div id="stBadge"></div>"""

L02_BODY = r"""
<div class="alert error" id="banner" style="margin-bottom:16px;display:none" role="status"></div>
<div class="grid" style="grid-template-columns: 2fr 1fr;align-items:start">
  <form class="card" id="form" novalidate>
    <div class="field">
      <span class="lbl req" id="typeLbl">Leave type</span>
      <div role="radiogroup" aria-labelledby="typeLbl" style="display:flex;gap:12px" id="types">
        <label class="opt"><input type="radio" name="type" value="Casual" checked> Casual</label>
        <label class="opt"><input type="radio" name="type" value="Sick"> Sick</label>
        <label class="opt"><input type="radio" name="type" value="Earned"> Earned</label>
      </div>
    </div>
    <div class="form-grid" style="grid-template-columns:repeat(2,1fr)">
      <div class="field"><label for="fd" class="req">From date</label><input class="in" type="date" id="fd" min="2025-07-01"><div class="err-text" id="fdErr" hidden></div></div>
      <div class="field"><label for="td" class="req">To date</label><input class="in" type="date" id="td" min="2025-07-01"><div class="err-text" id="tdErr" hidden></div></div>
    </div>
    <div class="alert info" style="display:flex;justify-content:space-between;align-items:center"><span id="sumTxt">Leave days</span><b id="cnt" style="font-size:18px">—</b></div>
    <div class="form-actions">
      <a class="btn" href="scr-lms-01-my-leave.html">Cancel</a>
      <button type="submit" class="btn primary">Submit for approval</button>
    </div>
  </form>
  <div class="card">
    <h2>Before you submit</h2>
    <ul class="small" style="margin:0;padding-left:18px;color:var(--text-2);line-height:1.8">
      <li>Casual, Sick or Earned; full days only.</li>
      <li>Days are calendar days, from and to inclusive. Balances are not checked.</li>
      <li>Cannot overlap your other submitted or approved leave.</li>
      <li>Cannot include a day that already has submitted or approved attendance.</li>
      <li>You can cancel a request until your manager decides.</li>
    </ul>
  </div>
</div>
"""

L02_SCRIPT = COMMON + MY_LEAVE + r"""
const $ = id => document.getElementById(id);
const ATT_DAYS = ['2026-11-02', '2026-11-03', '2026-11-09', '2026-11-10', '2026-11-11', '2026-11-13'];
function calc() { const f = $('fd').value, t = $('td').value; const n = f && t && t >= f ? days(f, t) : null; $('cnt').textContent = n ? n + (n === 1 ? ' day' : ' days') : '—'; $('sumTxt').textContent = n ? 'Leave days · ' + range(f, t) : 'Leave days'; }
['fd', 'td'].forEach(i => $(i).addEventListener('input', () => { if (i === 'fd' && !$('td').value) $('td').value = $('fd').value; calc(); }));
function err(box, field, msg) { $(field).classList.toggle('invalid', !!msg); $(box).hidden = !msg; if (msg) $(box).textContent = msg; return !!msg; }
$('form').addEventListener('submit', e => {
  e.preventDefault();
  const f = $('fd').value, t = $('td').value; let bad = false;
  bad = err('fdErr', 'fd', !f ? 'Select a from date.' : f < DOJ ? 'From date cannot be before your date of joining (01 Jul 2025).' : '') || bad;
  bad = err('tdErr', 'td', !t ? 'Select a to date.' : f && t < f ? 'To date must be on or after From date.' : '') || bad;
  if (!bad) {
    const ov = LV.find(l => (l.st === 'Submitted' || l.st === 'Approved') && l.id !== editingId && !(t < l.f || f > l.t));
    const att = ATT_DAYS.filter(d => d >= f && d <= t);
    if (ov) bad = err('fdErr', 'fd', 'Overlaps your ' + ov.st.toLowerCase() + ' ' + ov.type + ' leave (' + range(ov.f, ov.t) + ').');
    else if (att.length) bad = err('fdErr', 'fd', 'You already have attendance on ' + att.map(sh).join(', ') + '. Remove those days from the range.');
  }
  if (bad) return;
  toast(document.querySelector('input[name=type]:checked').value + ' leave ' + range(f, t) + ' submitted to Rahul Mehta.');
  setTimeout(() => location.href = 'scr-lms-01-my-leave.html', 1100);
});
let editingId = null;
function setCase(c) {
  $('case').value = c; editingId = c === 'fix' ? 2 : null;
  $('banner').style.display = c === 'fix' ? '' : 'none';
  $('banner').textContent = 'Rejected by Rahul Mehta on 30 Oct 2026: "Year-end release week — please pick dates in January." Change the dates and submit again.';
  $('ttl').textContent = c === 'fix' ? 'Edit leave request' : 'Request leave';
  $('stBadge').innerHTML = c === 'fix' ? badge('Rejected') : '';
  if (c === 'fix') { document.querySelector('input[value=Earned]').checked = true; $('fd').value = '2026-12-22'; $('td').value = '2026-12-26'; }
  else if (c === 'overlap') { $('fd').value = '2026-11-24'; $('td').value = '2026-11-25'; }
  else if (c === 'att') { document.querySelector('input[value=Sick]').checked = true; $('fd').value = '2026-11-10'; $('td').value = '2026-11-10'; }
  else { $('fd').value = ''; $('td').value = ''; }
  calc();
}
$('case').addEventListener('change', e => setCase(e.target.value));
setCase(new URLSearchParams(location.search).get('case') || 'new');
"""

L02_CTRL = r""" Case: <select id="case" aria-label="Case"><option value="new">New request</option><option value="fix">Fix rejected (Earned, 22–26 Dec)</option><option value="overlap">Overlap with pending leave (submit)</option><option value="att">Clash with attendance (submit)</option></select>"""


def l02():
    return shell("SCR-LMS-02", "Leave request", "leave", "My work / Leave / Request", L02_HEAD, L02_BODY, L02_SCRIPT,
                 roles=("employee", "manager"), default="employee", extra_controls=L02_CTRL)


# ---------------------------------------------------------------- SCR-LMS-03
L03_HEAD = r"""<div><h1>Team leave</h1><p class="lead">Approve your direct reports' leave. See who else is away before deciding.</p></div>"""

L03_BODY = r"""
<div class="tabs"><a href="scr-lms-01-my-leave.html">My leave</a><a href="#" class="on">Team</a></div>
<div class="tabs" id="sub" style="border-bottom:0;margin-bottom:8px"><a href="#" class="on" data-t="pending">Pending<span class="count" id="cP"></span></a><a href="#" data-t="history">History</a></div>
<div class="toolbar">
  <select class="in" id="fEmp" style="width:220px" aria-label="Employee"><option value="">All team members</option><option>Anita Sharma</option><option>Vikram Singh</option><option>Neha Gupta</option><option>Arjun Rao</option></select>
  <select class="in" id="fType" style="width:170px" aria-label="Leave type"><option value="">All types</option><option>Casual</option><option>Sick</option><option>Earned</option></select>
</div>
<div class="bulk" id="bulk"><b id="selCount">0 selected</b><button class="btn primary sm" id="bulkApprove">Approve selected</button><button class="btn sm" id="bulkClear">Clear</button><span class="small muted">Reject one at a time — remarks are required.</span></div>
<div class="tbl-wrap" id="wrap"><table class="t"><thead id="thead"></thead><tbody id="rows"></tbody></table></div>
<div class="card empty" id="empty" style="display:none"><b>Nothing pending</b>All leave requests have been decided.</div>
"""

L03_MODAL = r"""
<div class="modal-bg" id="rjModal" role="dialog" aria-modal="true" aria-labelledby="rjT"><div class="modal"><h2 id="rjT">Reject leave request</h2><p class="small muted" id="rjWhat" style="margin-top:-6px"></p>
  <div class="field"><label for="rjText" class="req">Remarks for the employee</label><textarea class="in" id="rjText" placeholder="Explain why, or suggest other dates"></textarea><div class="err-text" id="rjErr" hidden>Remarks are required to reject.</div></div>
  <div class="actions"><button class="btn" id="rjNo">Cancel</button><button class="btn danger" id="rjYes">Reject</button></div></div></div>
"""

L03_SCRIPT = COMMON + r"""
const $ = id => document.getElementById(id);
let tab = 'pending';
const R = [
  { id: 1, emp: 'Arjun Rao', eid: 'EMP0010', type: 'Casual', f: '2026-11-20', t: '2026-11-21', st: 'Submitted', req: '2026-11-14' },
  { id: 2, emp: 'Anita Sharma', eid: 'EMP0007', type: 'Casual', f: '2026-11-23', t: '2026-11-24', st: 'Submitted', req: '2026-11-14' },
  { id: 3, emp: 'Vikram Singh', eid: 'EMP0008', type: 'Earned', f: '2026-11-24', t: '2026-11-27', st: 'Approved', req: '2026-11-01', by: 'Rahul Mehta, 03 Nov' },
  { id: 4, emp: 'Anita Sharma', eid: 'EMP0007', type: 'Casual', f: '2026-11-05', t: '2026-11-06', st: 'Approved', req: '2026-11-02', by: 'Rahul Mehta, 03 Nov' },
  { id: 5, emp: 'Anita Sharma', eid: 'EMP0007', type: 'Earned', f: '2026-12-22', t: '2026-12-26', st: 'Rejected', req: '2026-10-28', by: 'Rahul Mehta, 30 Oct', rm: 'Year-end release week — please pick dates in January.' },
  { id: 6, emp: 'Neha Gupta', eid: 'EMP0009', type: 'Sick', f: '2026-11-04', t: '2026-11-04', st: 'Approved', req: '2026-11-05', by: 'Rahul Mehta, 05 Nov' }
];
function overlaps(r) { return R.filter(o => o.id !== r.id && (o.st === 'Approved' || o.st === 'Submitted') && !(r.t < o.f || r.f > o.t)).map(o => o.emp.split(' ')[0] + ' (' + range(o.f, o.t) + (o.st === 'Submitted' ? ', pending' : '') + ')'); }
function render() {
  const e = $('fEmp').value, ty = $('fType').value, pend = tab === 'pending';
  const rows = R.filter(r => (pend ? r.st === 'Submitted' : r.st !== 'Submitted') && (!e || r.emp === e) && (!ty || r.type === ty)).sort((a, b) => pend ? a.f.localeCompare(b.f) : b.f.localeCompare(a.f));
  $('cP').textContent = R.filter(r => r.st === 'Submitted').length;
  $('thead').innerHTML = '<tr>' + (pend ? '<th style="width:36px"><input type="checkbox" id="all" aria-label="Select all"></th>' : '') + '<th>Employee</th><th>Type</th><th>Dates</th><th class="num">Days</th>' + (pend ? '<th>Also away</th><th>Requested</th>' : '<th>Decision</th>') + '<th>Status</th><th class="act">Actions</th></tr>';
  $('rows').innerHTML = rows.map(r => { const ov = overlaps(r);
    return '<tr data-id="' + r.id + '">' + (pend ? '<td><input type="checkbox" class="sel" aria-label="Select ' + r.emp + '"></td>' : '') +
    '<td style="white-space:nowrap"><div style="font-weight:500">' + r.emp + '</div><div class="small muted">' + r.eid + '</div></td><td>' + r.type + '</td><td style="white-space:nowrap">' + range(r.f, r.t) + '</td><td class="num">' + days(r.f, r.t) + '</td>' +
    (pend ? '<td class="small">' + (ov.length ? '<span class="badge b-warn">' + ov.length + '</span> ' + ov.join(', ') : '<span class="muted">No one</span>') + '</td><td class="small muted">' + d2(r.req) + '</td>'
          : '<td class="small muted">' + r.by + (r.rm ? '<br>"' + r.rm + '"' : '') + '</td>') +
    '<td>' + badge(r.st) + '</td><td class="act">' + (pend ? '<button class="btn primary sm" data-a="ok">Approve</button><button class="btn danger sm" data-a="rj">Reject</button>' : '<span class="muted small">—</span>') + '</td></tr>'; }).join('');
  $('wrap').style.display = rows.length ? '' : 'none'; $('empty').style.display = rows.length ? 'none' : '';
  const all = $('all'); if (all) all.onchange = ev => { document.querySelectorAll('.sel').forEach(c => c.checked = ev.target.checked); sync(); };
  sync();
}
function sync() { const n = document.querySelectorAll('.sel:checked').length; $('selCount').textContent = n + ' selected'; $('bulk').classList.toggle('show', n > 0); }
function decide(ids, st, rm) { ids.forEach(id => { const r = R.find(x => x.id === id); r.st = st; r.by = 'Rahul Mehta, 16 Nov'; if (rm) r.rm = rm; }); render(); }
$('sub').addEventListener('click', e => { const a = e.target.closest('a'); if (!a) return; e.preventDefault(); tab = a.dataset.t; document.querySelectorAll('#sub a').forEach(x => x.classList.toggle('on', x === a)); render(); });
['fEmp', 'fType'].forEach(i => $(i).addEventListener('input', render));
$('rows').addEventListener('change', e => { if (e.target.classList.contains('sel')) sync(); });
$('bulkClear').onclick = () => { document.querySelectorAll('.sel').forEach(c => c.checked = false); sync(); };
$('bulkApprove').onclick = () => { const ids = [...document.querySelectorAll('.sel:checked')].map(c => +c.closest('tr').dataset.id); decide(ids, 'Approved'); toast(ids.length + ' leave request(s) approved.'); };
let cur;
$('rows').addEventListener('click', e => { const b = e.target.closest('button[data-a]'); if (!b) return; cur = R.find(x => x.id === +b.closest('tr').dataset.id);
  if (b.dataset.a === 'ok') { decide([cur.id], 'Approved'); toast('Leave for ' + cur.emp + ' approved.'); }
  else { $('rjWhat').textContent = cur.emp + ' · ' + cur.type + ' · ' + range(cur.f, cur.t); $('rjText').value = ''; $('rjErr').hidden = true; $('rjModal').classList.add('open'); $('rjText').focus(); } });
$('rjNo').onclick = () => $('rjModal').classList.remove('open');
$('rjYes').onclick = () => { if (!$('rjText').value.trim()) { $('rjErr').hidden = false; return; } $('rjModal').classList.remove('open'); decide([cur.id], 'Rejected', $('rjText').value.trim()); toast('Leave rejected and returned to ' + cur.emp + '.'); };
render();
"""


def l03():
    return shell("SCR-LMS-03", "Team leave review", "leave", "My work / Leave / Team", L03_HEAD, L03_BODY, L03_SCRIPT,
                 roles=("manager",), default="manager", modal=L03_MODAL)


PAGES = {
    "scr-lms-01-my-leave.html": l01,
    "scr-lms-02-request.html": l02,
    "scr-lms-03-team-review.html": l03,
}
