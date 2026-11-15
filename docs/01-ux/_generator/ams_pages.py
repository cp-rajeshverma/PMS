from base import shell

# Sample data for Anita Sharma (EMP0007), November 2026. Today = Mon 16 Nov 2026.
MY_DATA = r"""
const TODAY = '2026-11-16', DOJ = '2025-07-01';
const ATT = {
  '2026-11-02': { f: '09:00', t: '17:30', st: 'Approved' },
  '2026-11-03': { f: '09:00', t: '17:00', st: 'Approved' },
  '2026-11-09': { f: '09:00', t: '18:00', st: 'Approved' },
  '2026-11-10': { f: '09:30', t: '17:30', st: 'Approved' },
  '2026-11-11': { f: '09:00', t: '17:00', st: 'Approved' },
  '2026-11-12': { f: '09:00', t: '19:30', st: 'Rejected', rm: 'Out time looks wrong, please check.' },
  '2026-11-13': { f: '09:00', t: '17:30', st: 'Submitted' },
  '2026-11-16': { f: '09:00', t: '', st: 'Draft' }
};
const LEAVE = { '2026-11-05': 'Casual', '2026-11-06': 'Casual', '2026-11-23': 'Casual (pending)', '2026-11-24': 'Casual (pending)' };
const hrs = (f, t) => { if (!f || !t) return null; const [a, b] = f.split(':').map(Number), [c, d] = t.split(':').map(Number); return ((c * 60 + d) - (a * 60 + b)) / 60; };
const fmtH = h => h == null ? '—' : h.toFixed(2).replace(/\.00$/, '.0').replace(/(\.\d)0$/, '$1') + ' h';
const DOW = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
const nice = iso => { const d = new Date(iso + 'T00:00:00'); return DOW[d.getDay()] + ' ' + String(d.getDate()).padStart(2, '0') + ' ' + MON[d.getMonth()]; };
"""

# ---------------------------------------------------------------- SCR-AMS-01
A01_HEAD = r"""<div><h1>Attendance</h1><p class="lead">Your daily attendance. Each day needs your manager's approval.</p></div>
<div><a class="btn primary" href="scr-ams-02-entry.html">+ Enter attendance</a></div>"""

A01_BODY = r"""
<div class="tabs" data-roles="manager"><a href="scr-ams-01-my-attendance.html" class="on">My attendance</a><a href="scr-ams-03-team-review.html">Team<span class="count">3</span></a></div>
<div class="grid g4" style="margin-bottom:16px">
  <div class="card tile"><div class="k">Approved hours</div><div class="v" id="tH"></div><div class="s" id="tD"></div></div>
  <div class="card tile"><div class="k">Waiting for approval</div><div class="v" id="tS"></div><div class="s">Submitted days</div></div>
  <div class="card tile"><div class="k">Needs your action</div><div class="v" id="tR" style="color:var(--danger)"></div><div class="s">Rejected or draft days</div></div>
  <div class="card tile"><div class="k">Missing weekdays</div><div class="v" id="tM" style="color:var(--warning)"></div><div class="s">No attendance or leave (reminder)</div></div>
</div>
<div class="toolbar">
  <button class="btn sm" aria-label="Previous month" onclick="toast('Mockup: only November 2026 has sample data.')">‹</button>
  <b style="font-size:16px;min-width:130px;text-align:center">November 2026</b>
  <button class="btn sm" aria-label="Next month" disabled>›</button>
  <div style="margin-left:auto;display:flex;gap:4px" role="group" aria-label="View">
    <button class="btn sm" id="vCal" aria-pressed="true">Calendar</button><button class="btn sm" id="vList" aria-pressed="false">List</button>
  </div>
</div>
<div id="cal" class="card" style="padding:0;overflow:hidden">
  <div class="cal-head"><div>Mon</div><div>Tue</div><div>Wed</div><div>Thu</div><div>Fri</div><div>Sat</div><div>Sun</div></div>
  <div class="cal-grid" id="grid"></div>
</div>
<div class="small muted" id="legend" style="margin-top:10px;display:flex;gap:16px;flex-wrap:wrap">
  <span><span class="badge b-approved">Approved</span></span><span><span class="badge b-submitted">Submitted</span></span>
  <span><span class="badge b-rejected">Rejected</span></span><span><span class="badge b-draft">Draft</span></span>
  <span><span class="badge b-leave">Leave</span></span><span><span class="badge b-warn">Missing</span> weekday reminder</span>
</div>
<div id="list" class="tbl-wrap" style="display:none">
  <table class="t"><thead><tr><th>Date</th><th>From</th><th>To</th><th class="num">Hours</th><th>Status</th><th>Manager remarks</th><th class="act">Actions</th></tr></thead><tbody id="rows"></tbody></table>
</div>
"""

A01_SCRIPT = MY_DATA + r"""
const $ = id => document.getElementById(id);
function build() {
  let html = '', apH = 0, apD = 0, sub = 0, act = 0, miss = 0;
  // Nov 2026 starts on Sunday -> 6 leading cells (Mon-start grid)
  for (let i = 0; i < 6; i++) html += '<div class="cell out"><span class="d">' + (26 + i) + '</span></div>';
  for (let day = 1; day <= 30; day++) {
    const iso = '2026-11-' + String(day).padStart(2, '0'), dow = new Date(iso + 'T00:00:00').getDay();
    const a = ATT[iso], lv = LEAVE[iso], future = iso > TODAY, weekday = dow > 0 && dow < 6;
    let inner = '', cls = 'cell';
    if (iso === TODAY) cls += ' today';
    if (a) { const h = hrs(a.f, a.t); inner = '<span class="badge b-' + a.st.toLowerCase() + '">' + a.st + '</span><span class="h">' + a.f + '–' + (a.t || '…') + (h ? ' · ' + fmtH(h) : '') + '</span>';
      if (a.st === 'Approved') { apH += h; apD++; } if (a.st === 'Submitted') sub++; if (a.st === 'Rejected' || a.st === 'Draft') act++; }
    else if (lv) inner = '<span class="badge b-leave">Leave</span><span class="h">' + lv + '</span>';
    else if (!future && weekday && iso < TODAY) { inner = '<span class="badge b-warn">Missing</span><span class="h">Click to enter</span>'; cls += ' missing'; miss++; }
    if (future && !a) { cls += ' future'; html += '<div class="' + cls + '"><span class="d">' + day + '</span>' + inner + '</div>'; continue; }
    if (lv && !a) { html += '<div class="' + cls + '"><span class="d">' + day + '</span>' + inner + '</div>'; continue; }
    html += '<button class="' + cls + '" data-iso="' + iso + '" aria-label="' + nice(iso) + (a ? ', ' + a.st : '') + '"><span class="d">' + day + '</span>' + inner + '</button>';
  }
  for (let i = 1; i <= 6; i++) html += '<div class="cell out"><span class="d">' + i + '</span></div>';
  $('grid').innerHTML = html;
  $('tH').textContent = fmtH(apH); $('tD').textContent = apD + ' approved days'; $('tS').textContent = sub; $('tR').textContent = act; $('tM').textContent = miss;
  const days = Object.keys(ATT).sort().reverse();
  $('rows').innerHTML = days.map(iso => { const a = ATT[iso], edit = a.st === 'Rejected' || a.st === 'Draft';
    return '<tr><td style="white-space:nowrap">' + nice(iso) + '</td><td>' + a.f + '</td><td>' + (a.t || '—') + '</td><td class="num">' + fmtH(hrs(a.f, a.t)) + '</td><td><span class="badge b-' + a.st.toLowerCase() + '">' + a.st + '</span></td><td class="small">' + (a.rm || '<span class="muted">—</span>') + '</td><td class="act"><a class="btn sm" href="scr-ams-02-entry.html?date=' + iso + (a.st === 'Rejected' ? '&case=fix' : '') + '">' + (edit ? 'Edit' : 'View') + '</a></td></tr>'; }).join('');
}
build();
$('grid').addEventListener('click', e => { const c = e.target.closest('button.cell'); if (!c) return; const iso = c.dataset.iso; location.href = 'scr-ams-02-entry.html?date=' + iso + (ATT[iso] && ATT[iso].st === 'Rejected' ? '&case=fix' : ''); });
function view(v) { const cal = v === 'cal'; $('cal').style.display = cal ? '' : 'none'; $('legend').style.display = cal ? 'flex' : 'none'; $('list').style.display = cal ? 'none' : '';
  $('vCal').setAttribute('aria-pressed', cal); $('vList').setAttribute('aria-pressed', !cal); $('vCal').classList.toggle('primary', cal); $('vList').classList.toggle('primary', !cal); }
$('vCal').onclick = () => view('cal'); $('vList').onclick = () => view('list'); view('cal');
"""


def a01():
    return shell("SCR-AMS-01", "My attendance", "attendance", "My work / Attendance", A01_HEAD, A01_BODY, A01_SCRIPT,
                 roles=("employee", "manager"), default="employee")


# ---------------------------------------------------------------- SCR-AMS-02
A02_HEAD = r"""<div><h1 id="ttl">Enter attendance</h1><p class="lead">One entry per day. Times are in IST, same day only.</p></div><div id="stBadge"></div>"""

A02_BODY = r"""
<div class="alert" id="banner" style="margin-bottom:16px;display:none" role="status"></div>
<div class="grid" style="grid-template-columns: 2fr 1fr;align-items:start">
  <form class="card" id="form" novalidate>
    <div class="form-grid">
      <div class="field"><label for="dt" class="req">Date</label><input class="in" type="date" id="dt" min="2025-07-01" max="2026-11-16"><div class="err-text" id="dtErr" hidden></div></div>
      <div class="field"><label for="ft" class="req">From time</label><input class="in" type="time" id="ft" step="900"><div class="err-text" hidden></div></div>
      <div class="field"><label for="tt" class="req">To time</label><input class="in" type="time" id="tt" step="900"><div class="err-text" id="ttErr" hidden></div></div>
    </div>
    <div class="alert info" style="display:flex;justify-content:space-between;align-items:center">
      <span>Hours worked</span><b id="hrs" style="font-size:18px">—</b>
    </div>
    <div class="alert warn" id="longWarn" hidden style="margin-top:12px">Over 12 hours — please check the times before submitting.</div>
    <div class="form-actions">
      <a class="btn" href="scr-ams-01-my-attendance.html">Cancel</a>
      <button type="button" class="btn" id="draft">Save draft</button>
      <button type="submit" class="btn primary" id="submit">Submit for approval</button>
    </div>
  </form>
  <div class="card">
    <h2>Before you submit</h2>
    <ul class="small" style="margin:0;padding-left:18px;color:var(--text-2);line-height:1.8">
      <li>One entry per day; no future dates. Times in 15-minute steps.</li>
      <li>You cannot withdraw a submitted entry; ask your manager to reject it if it is wrong.</li>
      <li>From time must be before To time; overnight shifts are not supported.</li>
      <li>Not allowed on a day with submitted or approved leave.</li>
      <li>After approval the entry is locked and your salary record for the day is generated automatically.</li>
    </ul>
  </div>
</div>
"""

A02_SCRIPT = MY_DATA + r"""
const $ = id => document.getElementById(id);
const P = new URLSearchParams(location.search);
function load(iso, fix) {
  const a = ATT[iso];
  $('dt').value = iso || ''; $('ft').value = a ? a.f : '09:00'; $('tt').value = a ? a.t : '';
  const locked = a && (a.st === 'Approved' || a.st === 'Submitted');
  [$('dt'), $('ft'), $('tt')].forEach(x => x.readOnly = locked);
  $('dt').readOnly = !!a;
  $('submit').style.display = $('draft').style.display = locked ? 'none' : '';
  $('ttl').textContent = a ? (locked ? 'Attendance · ' + nice(iso) : 'Edit attendance · ' + nice(iso)) : 'Enter attendance';
  $('stBadge').innerHTML = a ? '<span class="badge b-' + a.st.toLowerCase() + '">' + a.st + '</span>' : '';
  const b = $('banner'); b.style.display = 'none';
  if (a && a.st === 'Rejected') { b.className = 'alert error'; b.textContent = 'Rejected by Rahul Mehta on 13 Nov 2026: "' + a.rm + '" Correct it and submit again.'; b.style.display = ''; }
  if (a && a.st === 'Submitted') { b.className = 'alert info'; b.textContent = 'Submitted — waiting for Rahul Mehta to approve. It cannot be changed now.'; b.style.display = ''; }
  if (a && a.st === 'Approved') { b.className = 'alert ok'; b.textContent = 'Approved by Rahul Mehta. Locked. Your salary record for this day has been generated.'; b.style.display = ''; }
  calc();
}
function calc() { const h = hrs($('ft').value, $('tt').value); $('hrs').textContent = h > 0 ? fmtH(h) : '—'; $('longWarn').hidden = !(h > 12); }
['ft', 'tt'].forEach(i => $(i).addEventListener('input', calc));
$('dt').addEventListener('change', () => { const iso = $('dt').value; if (ATT[iso]) { $('dtErr').hidden = false; $('dtErr').innerHTML = 'Attendance for ' + nice(iso) + ' already exists. <a href="scr-ams-02-entry.html?date=' + iso + '">Open it</a>'; } else $('dtErr').hidden = true; });
function err(id, msg, box) { const f = $(id), t = box || f.parentElement.querySelector('.err-text'); f.classList.toggle('invalid', !!msg); t.hidden = !msg; if (msg) t.innerHTML = msg; return !!msg; }
function validate() {
  const iso = $('dt').value, existing = ATT[iso] && P.get('date') !== iso;
  let bad = false;
  bad = err('dt', !iso ? 'Select a date.' : iso > TODAY ? 'Date cannot be in the future.' : iso < DOJ ? 'Date cannot be before your date of joining (01 Jul 2025).' :
        existing ? 'Attendance for ' + nice(iso) + ' already exists. <a href="scr-ams-02-entry.html?date=' + iso + '">Open it</a>' :
        LEAVE[iso] ? 'You have leave on ' + nice(iso) + ' (' + LEAVE[iso] + '). Attendance is not allowed on a leave day.' : '', $('dtErr')) || bad;
  bad = err('ft', $('ft').value ? '' : 'Enter a from time.') || bad;
  bad = err('tt', !$('tt').value ? 'Enter a to time.' : hrs($('ft').value, $('tt').value) <= 0 ? 'To time must be after From time (same day).' : '', $('ttErr')) || bad;
  return !bad;
}
$('draft').onclick = () => { toast('Draft saved.'); };
$('form').addEventListener('submit', e => { e.preventDefault(); if (!validate()) return; toast('Attendance for ' + nice($('dt').value) + ' submitted to Rahul Mehta.'); setTimeout(() => location.href = 'scr-ams-01-my-attendance.html', 1100); });
const cs = $('case');
cs.addEventListener('change', () => { const v = cs.value; load(v === 'new' ? '' : v === 'fix' ? '2026-11-12' : v === 'leave' ? '' : '2026-11-10'); if (v === 'leave') { $('dt').value = '2026-11-05'; } });
const initial = P.get('case') === 'fix' ? '2026-11-12' : (P.get('date') || '');
cs.value = P.get('case') === 'fix' ? 'fix' : (ATT[initial] && ATT[initial].st === 'Approved' ? 'approved' : 'new');
load(initial);
if (!ATT[initial] && initial) $('dt').value = initial;
"""

A02_CTRL = r""" Case: <select id="case" aria-label="Case"><option value="new">New entry</option><option value="fix">Fix rejected (Thu 12 Nov)</option><option value="approved">View approved (Tue 10 Nov)</option><option value="leave">Leave clash (pick Thu 05 Nov, submit)</option></select>"""


def a02():
    return shell("SCR-AMS-02", "Attendance entry", "attendance", "My work / Attendance / Entry", A02_HEAD, A02_BODY, A02_SCRIPT,
                 roles=("employee", "manager"), default="employee", extra_controls=A02_CTRL)


# ---------------------------------------------------------------- SCR-AMS-03
A03_HEAD = r"""<div><h1>Team attendance</h1><p class="lead">Approve your direct reports' daily attendance. Approval generates their salary record.</p></div>"""

A03_BODY = r"""
<div class="tabs"><a href="scr-ams-01-my-attendance.html">My attendance</a><a href="#" class="on">Team</a></div>
<div class="tabs" id="sub" style="border-bottom:0;margin-bottom:8px">
  <a href="#" class="on" data-t="pending">Pending<span class="count" id="cP"></span></a><a href="#" data-t="history">History</a>
</div>
<div class="toolbar">
  <select class="in" id="fEmp" style="width:220px" aria-label="Employee"><option value="">All team members</option><option>Anita Sharma</option><option>Vikram Singh</option><option>Neha Gupta</option><option>Arjun Rao</option></select>
  <input class="in" type="date" id="fFrom" value="2026-11-01" style="width:170px" aria-label="From date"> <span class="muted">to</span>
  <input class="in" type="date" id="fTo" value="2026-11-16" style="width:170px" aria-label="To date">
</div>
<div class="bulk" id="bulk"><b id="selCount">0 selected</b><button class="btn primary sm" id="bulkApprove">Approve selected</button><button class="btn sm" id="bulkClear">Clear</button><span class="small muted">Reject one at a time — remarks are required.</span></div>
<div class="tbl-wrap" id="wrap"><table class="t"><thead id="thead"></thead><tbody id="rows"></tbody></table></div>
<div class="card empty" id="empty" style="display:none"><b>Nothing pending</b>All attendance in this range has been decided.</div>
"""

A03_MODAL = r"""
<div class="modal-bg" id="rjModal" role="dialog" aria-modal="true" aria-labelledby="rjT"><div class="modal"><h2 id="rjT">Reject attendance</h2><p class="small muted" id="rjWhat" style="margin-top:-6px"></p>
  <div class="field"><label for="rjText" class="req">Remarks for the employee</label><textarea class="in" id="rjText" placeholder="Explain what needs to be corrected"></textarea><div class="err-text" id="rjErr" hidden>Remarks are required to reject.</div></div>
  <div class="actions"><button class="btn" id="rjNo">Cancel</button><button class="btn danger" id="rjYes">Reject</button></div></div></div>
<div class="modal-bg" id="roModal" role="dialog" aria-modal="true" aria-labelledby="roT"><div class="modal"><h2 id="roT">Reopen attendance</h2><p id="roWhat"></p>
  <div class="alert info" style="margin-bottom:16px">The attendance goes back to the employee as <b>Rejected</b> to correct. The linked salary record becomes <b>Voided</b>; a new one is generated when the corrected attendance is approved.</div>
  <div class="field"><label for="roText" class="req">Remarks for the employee</label><textarea class="in" id="roText">Please correct the out time and resubmit.</textarea></div>
  <div class="actions"><button class="btn" id="roNo">Cancel</button><button class="btn primary" id="roYes">Reopen attendance</button></div></div></div>
"""

A03_SCRIPT = r"""
const $ = id => document.getElementById(id);
let tab = 'pending';
const R = [
  { id: 1, emp: 'Anita Sharma', eid: 'EMP0007', d: '2026-11-13', f: '09:00', t: '17:30', st: 'Submitted', sub: '13 Nov, 18:02' },
  { id: 2, emp: 'Vikram Singh', eid: 'EMP0008', d: '2026-11-13', f: '10:00', t: '18:00', st: 'Submitted', sub: '13 Nov, 18:15' },
  { id: 3, emp: 'Neha Gupta', eid: 'EMP0009', d: '2026-11-16', f: '08:30', t: '13:00', st: 'Submitted', sub: '16 Nov, 13:05' },
  { id: 4, emp: 'Vikram Singh', eid: 'EMP0008', d: '2026-11-10', f: '09:00', t: '18:00', st: 'Approved', by: 'Rahul Mehta, 11 Nov', disputed: true },
  { id: 5, emp: 'Anita Sharma', eid: 'EMP0007', d: '2026-11-12', f: '09:00', t: '19:30', st: 'Rejected', by: 'Rahul Mehta, 13 Nov', rm: 'Out time looks wrong, please check.' },
  { id: 6, emp: 'Anita Sharma', eid: 'EMP0007', d: '2026-11-11', f: '09:00', t: '17:00', st: 'Approved', by: 'Rahul Mehta, 13 Nov' },
  { id: 7, emp: 'Neha Gupta', eid: 'EMP0009', d: '2026-11-11', f: '09:00', t: '17:30', st: 'Approved', by: 'Rahul Mehta, 12 Nov' },
  { id: 8, emp: 'Arjun Rao', eid: 'EMP0010', d: '2026-11-11', f: '10:00', t: '16:00', st: 'Approved', by: 'Rahul Mehta, 12 Nov' }
];
const hrs = (f, t) => { const [a, b] = f.split(':').map(Number), [c, d] = t.split(':').map(Number); return ((c * 60 + d) - (a * 60 + b)) / 60; };
const DOW = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
const nice = iso => { const d = new Date(iso + 'T00:00:00'); return DOW[d.getDay()] + ' ' + iso.slice(8) + ' Nov'; };
function render() {
  const e = $('fEmp').value, fr = $('fFrom').value, to = $('fTo').value;
  const rows = R.filter(r => (tab === 'pending' ? r.st === 'Submitted' : r.st !== 'Submitted') && (!e || r.emp === e) && r.d >= fr && r.d <= to)
                .sort((a, b) => tab === 'pending' ? a.d.localeCompare(b.d) : b.d.localeCompare(a.d));
  $('cP').textContent = R.filter(r => r.st === 'Submitted').length;
  const pend = tab === 'pending';
  $('thead').innerHTML = '<tr>' + (pend ? '<th style="width:36px"><input type="checkbox" id="all" aria-label="Select all"></th>' : '') + '<th>Employee</th><th>Date</th><th>From</th><th>To</th><th class="num">Hours</th><th>' + (pend ? 'Submitted' : 'Decision') + '</th><th>Status</th><th class="act">Actions</th></tr>';
  $('rows').innerHTML = rows.map(r => '<tr data-id="' + r.id + '">' + (pend ? '<td><input type="checkbox" class="sel" aria-label="Select ' + r.emp + ' ' + nice(r.d) + '"></td>' : '') +
    '<td style="white-space:nowrap"><div style="font-weight:500">' + r.emp + '</div><div class="small muted">' + r.eid + '</div></td><td style="white-space:nowrap">' + nice(r.d) + '</td><td>' + r.f + '</td><td>' + r.t + '</td><td class="num">' + hrs(r.f, r.t).toFixed(1) + ' h</td>' +
    '<td class="small muted">' + (pend ? r.sub : r.by + (r.rm ? '<br>"' + r.rm + '"' : '')) + '</td><td><span class="badge b-' + r.st.toLowerCase() + '">' + r.st + '</span>' + (r.disputed ? ' <span class="badge b-disputed">Salary disputed</span>' : '') + '</td><td class="act">' +
    (pend ? '<button class="btn primary sm" data-a="ok">Approve</button><button class="btn danger sm" data-a="rj">Reject</button>' : r.disputed ? '<button class="btn primary sm" data-a="ro">Reopen</button>' : (r.st === 'Rejected' ? '<span class="muted small">With employee</span>' : '<span class="muted small">Locked</span>')) + '</td></tr>').join('');
  $('wrap').style.display = rows.length ? '' : 'none'; $('empty').style.display = rows.length ? 'none' : '';
  const all = $('all'); if (all) all.onchange = ev => { document.querySelectorAll('.sel').forEach(c => c.checked = ev.target.checked); sync(); };
  sync();
}
function sync() { const n = document.querySelectorAll('.sel:checked').length; $('selCount').textContent = n + ' selected'; $('bulk').classList.toggle('show', n > 0); }
function decide(ids, st, rm) { ids.forEach(id => { const r = R.find(x => x.id === id); r.st = st; r.by = 'Rahul Mehta, 16 Nov'; if (rm) r.rm = rm; }); render(); }
$('sub').addEventListener('click', e => { const a = e.target.closest('a'); if (!a) return; e.preventDefault(); tab = a.dataset.t; document.querySelectorAll('#sub a').forEach(x => x.classList.toggle('on', x === a)); render(); });
['fEmp', 'fFrom', 'fTo'].forEach(i => $(i).addEventListener('input', render));
$('rows').addEventListener('change', e => { if (e.target.classList.contains('sel')) sync(); });
$('bulkClear').onclick = () => { document.querySelectorAll('.sel').forEach(c => c.checked = false); sync(); };
$('bulkApprove').onclick = () => { const ids = [...document.querySelectorAll('.sel:checked')].map(c => +c.closest('tr').dataset.id); decide(ids, 'Approved'); toast(ids.length + ' attendance record(s) approved. Salary records will be generated.'); };
let cur;
$('rows').addEventListener('click', e => { const b = e.target.closest('button[data-a]'); if (!b) return; cur = R.find(x => x.id === +b.closest('tr').dataset.id);
  const what = cur.emp + ' · ' + nice(cur.d) + ' · ' + cur.f + '–' + cur.t;
  if (b.dataset.a === 'ok') { decide([cur.id], 'Approved'); toast('Approved. Salary record for ' + cur.emp + ' will be generated.'); }
  if (b.dataset.a === 'rj') { $('rjWhat').textContent = what; $('rjText').value = ''; $('rjErr').hidden = true; $('rjModal').classList.add('open'); $('rjText').focus(); }
  if (b.dataset.a === 'ro') { $('roWhat').textContent = what + ' · salary disputed: "I left at 17:00, not 18:00."'; $('roModal').classList.add('open'); } });
$('rjNo').onclick = () => $('rjModal').classList.remove('open');
$('rjYes').onclick = () => { if (!$('rjText').value.trim()) { $('rjErr').hidden = false; return; } $('rjModal').classList.remove('open'); decide([cur.id], 'Rejected', $('rjText').value.trim()); toast('Rejected and returned to ' + cur.emp + '.'); };
$('roNo').onclick = () => $('roModal').classList.remove('open');
$('roYes').onclick = () => { $('roModal').classList.remove('open'); cur.disputed = false; decide([cur.id], 'Rejected', $('roText').value.trim()); toast('Attendance reopened. Salary record voided.'); };
render();
"""


def a03():
    return shell("SCR-AMS-03", "Team attendance review", "attendance", "My work / Attendance / Team", A03_HEAD, A03_BODY, A03_SCRIPT,
                 roles=("manager",), default="manager", modal=A03_MODAL)


PAGES = {
    "scr-ams-01-my-attendance.html": a01,
    "scr-ams-02-entry.html": a02,
    "scr-ams-03-team-review.html": a03,
}
