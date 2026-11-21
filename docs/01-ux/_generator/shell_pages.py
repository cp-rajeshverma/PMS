from base import shell, standalone

# ---------------------------------------------------------------- SCR-SH-02
SH02_BODY = r"""
<div class="wrap">
  <form class="auth" id="form" novalidate>
    <div class="brand"><div class="brand-mark" aria-hidden="true">P</div><div><b>PMS</b><span>Payroll Management System</span></div></div>
    <h1 id="title">Set your password</h1>
    <p class="lead" id="lead" style="margin-bottom:20px">You signed in with a temporary password. Choose your own password to continue.</p>
    <div class="alert error" id="alert" role="alert" style="display:none;margin-bottom:16px"></div>

    <div class="field" id="curWrap" style="display:none">
      <label for="cur" class="req">Current password</label>
      <input class="in" type="password" id="cur" autocomplete="current-password">
    </div>
    <div class="field">
      <label for="np" class="req">New password</label>
      <input class="in" type="password" id="np" autocomplete="new-password" aria-describedby="rules">
    </div>
    <ul id="rules" class="small" style="list-style:none;padding:0;margin:-6px 0 16px;color:var(--text-3)">
      <li data-r="len">○ At least 8 characters</li>
      <li data-r="up">○ An uppercase and a lowercase letter</li>
      <li data-r="num">○ A number</li>
      <li data-r="sp">○ A special character (e.g. ! @ # $)</li>
      <li data-r="id">○ Not your Employee Id</li>
    </ul>
    <div class="field">
      <label for="cp" class="req">Confirm new password</label>
      <input class="in" type="password" id="cp" autocomplete="new-password">
      <div class="err-text" id="cpErr" style="display:none">Passwords do not match.</div>
    </div>
    <button class="btn primary" style="width:100%;height:42px;justify-content:center" type="submit">Save password</button>
    <p class="small muted" style="text-align:center;margin:16px 0 0" id="backWrap"><a href="scr-sh-03-dashboard.html">Cancel and go back</a></p>
    <p class="small muted" style="text-align:center;margin:16px 0 0">PMS POC · v1.1</p>
  </form>
</div>
"""

SH02_SCRIPT = r"""
const $ = id => document.getElementById(id);
const EMP = 'EMP0007';
function setMode(m) {
  const first = m === 'first';
  $('title').textContent = first ? 'Set your password' : 'Change password';
  $('lead').textContent = first ? 'You signed in with a temporary password. Choose your own password to continue.' : 'Enter your current password, then choose a new one.';
  $('curWrap').style.display = first ? 'none' : '';
  $('backWrap').style.display = first ? 'none' : '';
  $('mode').value = m;
}
$('mode').addEventListener('change', e => setMode(e.target.value));
setMode(new URLSearchParams(location.search).get('first') ? 'first' : 'change');
const tests = {
  len: v => v.length >= 8, up: v => /[A-Z]/.test(v) && /[a-z]/.test(v), num: v => /\d/.test(v),
  sp: v => /[^A-Za-z0-9]/.test(v), id: v => v && v.toUpperCase() !== EMP
};
function check() {
  const v = $('np').value; let all = true;
  document.querySelectorAll('#rules li').forEach(li => {
    const ok = tests[li.dataset.r](v); all = all && ok;
    li.textContent = (ok ? '✓ ' : '○ ') + li.textContent.slice(2);
    li.style.color = ok ? 'var(--success)' : 'var(--text-3)';
  });
  return all;
}
$('np').addEventListener('input', check);
$('form').addEventListener('submit', e => {
  e.preventDefault(); $('alert').style.display = 'none'; $('cpErr').style.display = 'none';
  if ($('mode').value === 'change' && $('cur').value === 'wrong') { $('alert').textContent = 'Current password is incorrect.'; $('alert').style.display = 'block'; return; }
  if (!check()) { $('alert').textContent = 'The new password does not meet all the rules below.'; $('alert').style.display = 'block'; return; }
  if ($('np').value !== $('cp').value) { $('cpErr').style.display = 'block'; $('cp').classList.add('invalid'); return; }
  toast('Password saved.');
  setTimeout(() => location.href = 'scr-sh-03-dashboard.html', 900);
});
"""

SH02_CONTROLS = r"""Mode: <select id="mode" aria-label="Mode"><option value="first">First login (temporary password)</option><option value="change">Change password (from user menu)</option></select>
<span>Tip: type <b>wrong</b> as current password to see the error</span>"""


def sh02():
    return standalone("SCR-SH-02", "Set password", SH02_BODY, SH02_SCRIPT, SH02_CONTROLS)


# ---------------------------------------------------------------- SCR-SH-03
SH03_HEAD = r"""<div><h1 id="greet">Good morning, Anita</h1><p class="lead">Monday, 16 November 2026</p></div>
<div data-roles="admin"><a class="btn primary" href="scr-eims-02-admin-form.html">+ Onboard employee</a></div>"""

SH03_BODY = r"""
<!-- Employee + Manager: my work -->
<div data-roles="employee manager">
  <div class="grid g4" style="margin-bottom:16px">
    <div class="card tile"><div class="k">Hours this month</div><div class="v">41.5 h</div><div class="s">5 approved days</div></div>
    <div class="card tile"><div class="k">Earnings this month</div><div class="v">₹ 10,375</div><div class="s">Accepted + manager approved, excl. voided</div></div>
    <div class="card tile"><div class="k">Leave this month</div><div class="v">2 days</div><div class="s">1 request pending</div></div>
    <div class="card tile"><div class="k">Profile</div><div class="v" style="font-size:18px;margin-top:8px"><span class="badge b-approved">Approved</span></div><div class="s">Change request submitted 18 Nov · waiting for Rahul Mehta</div></div>
  </div>
  <div class="grid g2">
    <div class="card">
      <h2>Things to do <span class="badge b-warn" style="margin-left:6px">4</span></h2>
      <div class="list-row"><div><div class="t1"><span class="dot" style="background:var(--danger)"></span>Attendance for Thu 12 Nov was rejected</div><div class="t2">Manager remark: "Out time looks wrong, please check."</div></div><a class="btn sm" href="scr-ams-02-entry.html?case=fix">Fix</a></div>
      <div class="list-row"><div><div class="t1"><span class="dot" style="background:var(--warning)"></span>Attendance not entered for Wed 04 Nov</div><div class="t2">Working day up to yesterday with no attendance or leave</div></div><a class="btn sm" href="scr-ams-02-entry.html?date=2026-11-04">Enter</a></div>
      <div class="list-row"><div><div class="t1"><span class="dot" style="background:var(--primary)"></span>3 salary records waiting for your review</div><div class="t2">₹ 6,250 · 09–11 Nov</div></div><a class="btn sm" href="scr-sms-01-my-salary.html">Review</a></div>
      <div class="list-row"><div><div class="t1"><span class="dot" style="background:var(--primary)"></span>Leave request 23–24 Nov is waiting for approval</div><div class="t2">Casual leave · submitted 14 Nov</div></div><a class="btn sm" href="scr-lms-01-my-leave.html">View</a></div>
    </div>
    <div class="card">
      <div data-roles="manager">
        <h2>Waiting for your approval</h2>
        <div class="list-row"><div class="t1">Profiles and change requests</div><div><span class="badge b-submitted">1</span></div></div>
        <div class="list-row"><div class="t1">Attendance</div><div><span class="badge b-submitted">3</span></div></div>
        <div class="list-row"><div class="t1">Leave</div><div><span class="badge b-submitted">2</span></div></div>
        <div class="list-row"><div class="t1">Salary (incl. 1 dispute)</div><div><span class="badge b-submitted">3</span></div></div>
        <div style="margin-top:14px"><a class="btn primary" href="scr-sh-04-approvals.html">Open approvals inbox</a></div>
      </div>
      <div data-roles="employee">
        <h2>Recent activity</h2>
        <div class="list-row"><div><div class="t1">Attendance 11 Nov approved</div><div class="t2">by Rahul Mehta · 13 Nov, 10:42</div></div><span class="badge b-approved">Approved</span></div>
        <div class="list-row"><div><div class="t1">Salary record 11 Nov approved by manager</div><div class="t2">8.0 h × ₹ 250 = ₹ 2,000 · waiting for your review</div></div><span class="badge b-mgrapproved">Manager Approved</span></div>
        <div class="list-row"><div><div class="t1">Attendance 12 Nov rejected</div><div class="t2">by Rahul Mehta · 13 Nov, 10:43</div></div><span class="badge b-rejected">Rejected</span></div>
        <div class="list-row"><div><div class="t1">Leave 23–24 Nov submitted</div><div class="t2">14 Nov, 17:05</div></div><span class="badge b-submitted">Submitted</span></div>
      </div>
    </div>
  </div>
</div>

<!-- Admin -->
<div data-roles="admin">
  <div class="grid g4" style="margin-bottom:16px">
    <div class="card tile"><div class="k">Active employees</div><div class="v">19</div><div class="s">1 inactive</div></div>
    <div class="card tile"><div class="k">Profiles not yet approved</div><div class="v">3</div><div class="s">2 Draft · 1 Submitted</div></div>
    <div class="card tile"><div class="k">Waiting for you</div><div class="v">4</div><div class="s">Top-level employee's items</div></div>
    <div class="card tile"><div class="k">Last reconciliation</div><div class="v" style="font-size:18px;margin-top:8px"><span class="badge b-approved">Succeeded</span></div><div class="s">Today 01:00 IST · 0 created · 1 voided · 0 mismatches</div></div>
  </div>
  <div class="grid g2">
    <div class="card">
      <h2>Recently onboarded</h2>
      <div class="list-row"><div><div class="t1">Kavya Iyer · EMP0020</div><div class="t2">Joined 16 Nov 2026 · Manager: Rahul Mehta</div></div><span class="badge b-draft">Draft</span></div>
      <div class="list-row"><div><div class="t1">Sameer Khan · EMP0019</div><div class="t2">Joined 09 Nov 2026 · Manager: Rahul Mehta</div></div><span class="badge b-draft">Draft</span></div>
      <div class="list-row"><div><div class="t1">Meera Joshi · EMP0018</div><div class="t2">Joined 02 Nov 2026 · Manager: Rahul Mehta</div></div><span class="badge b-submitted">Submitted</span></div>
      <div style="margin-top:14px"><a href="scr-eims-01-directory.html">View all employees →</a></div>
    </div>
    <div class="card">
      <h2>Waiting for your approval</h2>
      <div class="list-row"><div><div class="t1">Rahul Mehta (EMP0002) · top-level employee</div><div class="t2">1 profile change request · 1 attendance · 1 leave · 1 salary record</div></div><a class="btn sm" href="scr-sh-04-approvals.html">Review</a></div>
      <h2 style="margin-top:20px">System jobs</h2>
      <div class="list-row"><div><div class="t1">Nightly salary reconciliation</div><div class="t2">Runs daily 01:00 IST · last run today, 4 s · 0 records created, 1 voided, 0 mismatches logged</div></div><span class="badge b-approved">Succeeded</span></div>
    </div>
  </div>
</div>
"""

SH03_SCRIPT = r"""
function onRole(r) { document.getElementById('greet').textContent = 'Good morning, ' + USERS[r].name.split(' ')[0]; }
"""


def sh03():
    return shell("SCR-SH-03", "Dashboard", "home", "Home", SH03_HEAD, SH03_BODY, SH03_SCRIPT)


# ---------------------------------------------------------------- SCR-SH-04
SH04_HEAD = r"""<div><h1>Approvals</h1><p class="lead">Everything waiting for your decision, across all modules (Admin: the top-level employee's items only). Your own items never appear here.</p></div>"""

SH04_BODY = r"""
<div class="tabs" role="tablist" id="tabs">
  <a href="#" class="on" data-f="all">All<span class="count" data-c="all"></span></a>
  <a href="#" data-f="Profile">Profiles<span class="count" data-c="Profile"></span></a>
  <a href="#" data-f="Attendance">Attendance<span class="count" data-c="Attendance"></span></a>
  <a href="#" data-f="Leave">Leave<span class="count" data-c="Leave"></span></a>
  <a href="#" data-f="Salary">Salary<span class="count" data-c="Salary"></span></a>
</div>
<div class="bulk" id="bulk" role="region" aria-label="Bulk actions">
  <b id="selCount">0 selected</b>
  <button class="btn primary sm" id="bulkApprove">Approve selected</button>
  <button class="btn sm" id="bulkClear">Clear</button>
  <span class="small muted">Reject one at a time — remarks are required. Salary records cannot be rejected; disputes are resolved by keeping as is or reopening attendance.</span>
</div>
<div class="tbl-wrap" id="tblWrap">
  <table class="t">
    <thead><tr>
      <th style="width:36px"><input type="checkbox" id="all" aria-label="Select all approvable items"></th>
      <th>Type</th><th>Employee</th><th>Details</th><th>Submitted / note</th><th>Status</th><th class="act">Actions</th>
    </tr></thead>
    <tbody id="rows"></tbody>
  </table>
</div>
<div class="card empty" id="empty" style="display:none"><b>All caught up</b>Nothing is waiting for your approval.</div>
"""

SH04_MODAL = r"""
<div class="modal-bg" id="rejectModal" role="dialog" aria-modal="true" aria-labelledby="rjTitle">
  <div class="modal">
    <h2 id="rjTitle">Reject item</h2>
    <p class="small muted" id="rjWhat" style="margin-top:-6px"></p>
    <div class="field">
      <label for="rjText" class="req">Remarks for the employee</label>
      <textarea class="in" id="rjText" placeholder="Explain what needs to be corrected"></textarea>
      <div class="err-text" id="rjErr" style="display:none">Remarks are required to reject.</div>
    </div>
    <div class="actions"><button class="btn" id="rjCancel">Cancel</button><button class="btn danger" id="rjOk">Reject</button></div>
  </div>
</div>
<div class="modal-bg" id="keepModal" role="dialog" aria-modal="true" aria-labelledby="kTitle">
  <div class="modal">
    <h2 id="kTitle">Resolve dispute: keep as is</h2>
    <p id="kWhat"></p>
    <div class="alert info" style="margin-bottom:16px">Use this when the attendance, and so the wage, is correct. The record goes back to <b>Manager Approved</b> and the employee is asked to accept it again, with your explanation.</div>
    <div class="field">
      <label for="kText" class="req">Explanation for the employee</label>
      <textarea class="in" id="kText" placeholder="e.g. Badge logs show you left at 18:00."></textarea>
      <div class="err-text" id="kErr" style="display:none">An explanation is required.</div>
    </div>
    <div class="actions"><button class="btn" id="kCancel">Cancel</button><button class="btn primary" id="kOk">Keep as is</button></div>
  </div>
</div>
<div class="modal-bg" id="reopenModal" role="dialog" aria-modal="true" aria-labelledby="roTitle">
  <div class="modal">
    <h2 id="roTitle">Resolve dispute: reopen attendance</h2>
    <p id="roWhat"></p>
    <div class="alert info" style="margin-bottom:16px">Reopening sends the attendance back to the employee as <b>Rejected</b> to correct. This salary record becomes <b>Voided</b>; a new one is generated when the corrected attendance is approved.</div>
    <div class="field">
      <label for="roText" class="req">Remarks for the employee</label>
      <textarea class="in" id="roText">Please correct the out time and resubmit.</textarea>
    </div>
    <div class="actions"><button class="btn" id="roCancel">Cancel</button><button class="btn primary" id="roOk">Reopen attendance</button></div>
  </div>
</div>
"""

SH04_SCRIPT = r"""
const ITEMS = {
  manager: [
    { id: 1, type: 'Profile', emp: 'Meera Joshi', eid: 'EMP0018', det: 'New profile · joined 02 Nov 2026', sub: '15 Nov, 09:12', st: 'Submitted', open: 'scr-eims-04-profile-review.html' },
    { id: 2, type: 'Attendance', emp: 'Anita Sharma', eid: 'EMP0007', det: 'Fri 13 Nov · 09:00–17:30 · 8.5 h', sub: '13 Nov, 18:02', st: 'Submitted', open: 'scr-ams-03-team-review.html' },
    { id: 3, type: 'Attendance', emp: 'Vikram Singh', eid: 'EMP0008', det: 'Fri 13 Nov · 10:00–18:00 · 8.0 h', sub: '13 Nov, 18:15', st: 'Submitted', open: 'scr-ams-03-team-review.html' },
    { id: 4, type: 'Attendance', emp: 'Neha Gupta', eid: 'EMP0009', det: 'Mon 16 Nov · 08:30–13:00 · 4.5 h', sub: '16 Nov, 13:05', st: 'Submitted', open: 'scr-ams-03-team-review.html' },
    { id: 11, type: 'Attendance', emp: 'Arjun Rao', eid: 'EMP0010', det: 'Fri 13 Nov · 07:00–20:00 · 13.0 h <span class="badge b-warn">Over 12 h</span>', sub: '13 Nov, 20:10', st: 'Submitted', open: 'scr-ams-03-team-review.html' },
    { id: 12, type: 'Profile', emp: 'Anita Sharma', eid: 'EMP0007', det: 'Profile change request · address changed', sub: '18 Nov, 11:05', st: 'Submitted', open: 'scr-eims-04-profile-review.html' },
    { id: 13, type: 'Salary', emp: 'Neha Gupta', eid: 'EMP0009', det: 'Thu 29 Oct · 8.0 h × ₹ 275 = ₹ 2,200', sub: 'Employee remark: "Still think 08:30 start is missing."<br><span class="muted">Your earlier explanation: "Attendance shows 09:00 start as you entered it."</span>', st: 'Disputed', open: 'scr-sms-02-team-review.html' },
    { id: 8, type: 'Leave', emp: 'Anita Sharma', eid: 'EMP0007', det: 'Casual · 23–24 Nov · 2 days', sub: '14 Nov, 17:05', st: 'Submitted', open: 'scr-lms-03-team-review.html' },
    { id: 5, type: 'Leave', emp: 'Arjun Rao', eid: 'EMP0010', det: 'Casual · 20–21 Nov · 2 days', sub: '14 Nov, 11:30', st: 'Submitted', open: 'scr-lms-03-team-review.html' },
    { id: 9, type: 'Salary', emp: 'Neha Gupta', eid: 'EMP0009', det: 'Wed 11 Nov · 8.5 h × ₹ 275 = ₹ 2,337.50', sub: 'Generated 12 Nov, 10:01', st: 'Generated', open: 'scr-sms-02-team-review.html' },
    { id: 10, type: 'Salary', emp: 'Arjun Rao', eid: 'EMP0010', det: 'Wed 11 Nov · 6.0 h × ₹ 250 = ₹ 1,500', sub: 'Generated 12 Nov, 10:01', st: 'Generated', open: 'scr-sms-02-team-review.html' },
    { id: 6, type: 'Salary', emp: 'Vikram Singh', eid: 'EMP0008', det: 'Tue 10 Nov · 9.0 h × ₹ 250 = ₹ 2,250', sub: 'Employee remark: "I left at 17:00, not 18:00."', st: 'Disputed', open: 'scr-sms-02-team-review.html' }
  ],
  admin: [
    { id: 7, type: 'Profile', emp: 'Rahul Mehta', eid: 'EMP0002', det: 'Profile change request · address changed', sub: '15 Nov, 16:40', st: 'Submitted', open: 'scr-eims-04-profile-review.html' },
    { id: 14, type: 'Attendance', emp: 'Rahul Mehta', eid: 'EMP0002', det: 'Fri 13 Nov · 09:00–18:00 · 9.0 h', sub: '13 Nov, 18:30', st: 'Submitted', open: 'scr-ams-03-team-review.html' },
    { id: 15, type: 'Leave', emp: 'Rahul Mehta', eid: 'EMP0002', det: 'Earned · 25–27 Nov · 3 days', sub: '15 Nov, 11:20', st: 'Submitted', open: 'scr-lms-03-team-review.html' },
    { id: 16, type: 'Salary', emp: 'Rahul Mehta', eid: 'EMP0002', det: 'Thu 12 Nov · 8.5 h × ₹ 600 = ₹ 5,100', sub: 'Generated 13 Nov, 10:02', st: 'Generated', open: 'scr-sms-02-team-review.html' }
  ],
  employee: []
};
let filter = 'all', data = [];
const badge = s => '<span class="badge b-' + s.toLowerCase().replace(/ /g, '') + '">' + s + '</span>';
function render() {
  const rows = data.filter(i => filter === 'all' || i.type === filter);
  document.querySelectorAll('[data-c]').forEach(c => { const n = data.filter(i => c.dataset.c === 'all' || i.type === c.dataset.c).length; c.textContent = n; });
  document.getElementById('rows').innerHTML = rows.map(i => {
    const disputed = i.st === 'Disputed';
    return '<tr data-id="' + i.id + '">' +
      '<td>' + (disputed ? '' : '<input type="checkbox" class="sel" aria-label="Select ' + i.type + ' of ' + i.emp + '">') + '</td>' +
      '<td><span class="chip">' + i.type.toUpperCase() + '</span></td>' +
      '<td><div style="font-weight:500;white-space:nowrap">' + i.emp + '</div><div class="small muted">' + i.eid + '</div></td>' +
      '<td>' + i.det + '</td><td class="small ' + (disputed ? '' : 'muted') + '" style="max-width:220px">' + i.sub + '</td>' +
      '<td>' + badge(i.st) + '</td><td class="act">' +
      (disputed
        ? '<button class="btn sm" data-a="keep">Keep as is</button><button class="btn primary sm" data-a="reopen">Reopen attendance</button>'
        : i.type === 'Salary' ? '<button class="btn primary sm" data-a="approve">Approve</button><a class="btn sm" href="' + i.open + '">Open</a>'
        : '<button class="btn primary sm" data-a="approve">Approve</button><button class="btn danger sm" data-a="reject">Reject</button><a class="btn sm" href="' + i.open + '">Open</a>') +
      '</td></tr>';
  }).join('');
  document.getElementById('tblWrap').style.display = rows.length ? '' : 'none';
  document.getElementById('empty').style.display = rows.length ? 'none' : '';
  document.getElementById('all').checked = false; syncBulk();
  const p = document.getElementById('pending'); if (p) { p.textContent = data.length; p.style.display = data.length ? '' : 'none'; }
}
function syncBulk() { const n = document.querySelectorAll('.sel:checked').length; document.getElementById('selCount').textContent = n + ' selected'; document.getElementById('bulk').classList.toggle('show', n > 0); }
function remove(ids) { data = data.filter(i => !ids.includes(i.id)); render(); }
function onRole(r) { data = ITEMS[r].slice(); render(); }
document.getElementById('tabs').addEventListener('click', e => { const a = e.target.closest('a'); if (!a) return; e.preventDefault(); document.querySelectorAll('#tabs a').forEach(x => x.classList.toggle('on', x === a)); filter = a.dataset.f; render(); });
document.getElementById('all').addEventListener('change', e => { document.querySelectorAll('.sel').forEach(c => c.checked = e.target.checked); syncBulk(); });
document.getElementById('rows').addEventListener('change', e => { if (e.target.classList.contains('sel')) syncBulk(); });
document.getElementById('bulkClear').addEventListener('click', () => { document.querySelectorAll('.sel').forEach(c => c.checked = false); syncBulk(); });
document.getElementById('bulkApprove').addEventListener('click', () => { const ids = [...document.querySelectorAll('.sel:checked')].map(c => +c.closest('tr').dataset.id); remove(ids); toast(ids.length + ' item(s) approved.'); });
let current = null;
document.getElementById('rows').addEventListener('click', e => {
  const b = e.target.closest('button[data-a]'); if (!b) return;
  current = data.find(i => i.id === +b.closest('tr').dataset.id);
  if (b.dataset.a === 'approve') { remove([current.id]); toast(current.type + ' for ' + current.emp + ' approved.' + (current.type === 'Attendance' ? ' Salary record will be generated.' : '')); }
  if (b.dataset.a === 'reject') { document.getElementById('rjWhat').textContent = current.type + ' · ' + current.emp + ' · ' + current.det; document.getElementById('rjText').value = ''; document.getElementById('rjErr').style.display = 'none'; document.getElementById('rejectModal').classList.add('open'); document.getElementById('rjText').focus(); }
  if (b.dataset.a === 'keep') { document.getElementById('kWhat').textContent = current.emp + ' · ' + current.det; document.getElementById('kText').value = ''; document.getElementById('kErr').style.display = 'none'; document.getElementById('keepModal').classList.add('open'); }
  if (b.dataset.a === 'reopen') { document.getElementById('roWhat').textContent = current.emp + ' · ' + current.det; document.getElementById('reopenModal').classList.add('open'); }
});
document.getElementById('rjCancel').onclick = () => document.getElementById('rejectModal').classList.remove('open');
document.getElementById('rjOk').onclick = () => { if (!document.getElementById('rjText').value.trim()) { document.getElementById('rjErr').style.display = 'block'; return; } document.getElementById('rejectModal').classList.remove('open'); remove([current.id]); toast(current.type + ' for ' + current.emp + ' rejected and returned to the employee.'); };
document.getElementById('kCancel').onclick = () => document.getElementById('keepModal').classList.remove('open');
document.getElementById('kOk').onclick = () => { if (!document.getElementById('kText').value.trim()) { document.getElementById('kErr').style.display = 'block'; return; } document.getElementById('keepModal').classList.remove('open'); remove([current.id]); toast('Dispute closed. ' + current.emp + ' can accept the record.'); };
document.getElementById('roCancel').onclick = () => document.getElementById('reopenModal').classList.remove('open');
document.getElementById('roOk').onclick = () => { document.getElementById('reopenModal').classList.remove('open'); remove([current.id]); toast('Attendance reopened. Salary record voided.'); };
"""


def sh04():
    return shell("SCR-SH-04", "Approvals inbox", "approvals", "Home / Approvals", SH04_HEAD, SH04_BODY, SH04_SCRIPT,
                 roles=("manager", "admin"), default="manager", modal=SH04_MODAL)



# ---------------------------------------------------------------- SCR-SH-00
SH00_BODY = r"""
<div class="card" id="area" style="border:2px dashed var(--border-strong);box-shadow:none;height:420px;display:grid;place-items:center;text-align:center;color:var(--text-3)">
  <div><b style="display:block;color:var(--text-2);font-size:15px;margin-bottom:4px">Page content area</b>Each module screen renders here inside the shell.<br>Width 1366 px desktop; sidebar 232 px; content padding 32 px.</div>
</div>
"""


SH00_CTRL = r""" Content: <select id="cv" aria-label="Content example"><option value="page">Page content</option><option value="err">System error (with reference)</option><option value="noacc">No access</option></select>"""

SH00_SCRIPT = r"""
const V = {
  page: '<div><b style="display:block;color:var(--text-2);font-size:15px;margin-bottom:4px">Page content area</b>Each module screen renders here inside the shell.<br>Width 1366 px desktop; sidebar 232 px; content padding 32 px.</div>',
  err: '<div class="alert error" style="text-align:left;max-width:520px">Attendance could not be saved. Please try again.<br><span class="small">Reference: 7F3K-2Q9M-81XA</span> <button class="btn sm" style="margin-left:8px">Retry</button></div>',
  noacc: '<div><b style="display:block;color:var(--text-2);font-size:15px;margin-bottom:8px">You don\'t have access to this page.</b><a class="btn" href="scr-sh-03-dashboard.html">Go to Home</a></div>'
};
document.getElementById('cv').addEventListener('change', e => document.getElementById('area').innerHTML = V[e.target.value]);
"""


def sh00():
    return shell("SCR-SH-00", "Shell layout", "home", "Home", "<h1>Page title</h1>", SH00_BODY, SH00_SCRIPT, extra_controls=SH00_CTRL)


# ---------------------------------------------------------------- SCR-SH-01
SH01_BODY = r"""
<div class="wrap">
  <form class="auth" id="form" novalidate>
    <div class="brand"><div class="brand-mark" aria-hidden="true">P</div><div><b>PMS</b><span>Payroll Management System</span></div></div>
    <h1>Sign in</h1>
    <p class="lead" style="margin-bottom:22px">Use your Employee Id and password.</p>
    <div class="alert error" id="alertError" role="alert" style="display:none;margin-bottom:18px"></div>
    <div class="alert warn" id="alertWarn" role="alert" style="display:none;margin-bottom:18px"></div>
    <div class="field">
      <label for="empId">Employee Id</label>
      <input class="in" type="text" id="empId" placeholder="e.g. EMP0007" autocomplete="username" autofocus style="height:40px">
      <div class="err-text" id="empErr" hidden>Enter your Employee Id.</div>
    </div>
    <div class="field">
      <label for="pwd">Password</label>
      <div class="pw-wrap">
        <input class="in" type="password" id="pwd" autocomplete="current-password" style="height:40px">
        <button type="button" class="pw-toggle" id="toggle" aria-label="Show password">Show</button>
      </div>
      <div class="err-text" id="pwdErr" hidden>Enter your password.</div>
    </div>
    <button class="btn primary" id="submit" type="submit" style="width:100%;height:42px;justify-content:center;margin-top:4px">Sign in</button>
    <p class="small" style="text-align:center;color:var(--text-2);margin:18px 0 0">Forgot your password? Contact your PMS administrator.</p>
    <p class="small muted" style="text-align:center;margin:18px 0 0">PMS POC · v1.1</p>
  </form>
</div>
"""

SH01_SCRIPT = r"""
const $ = id => document.getElementById(id);
$('toggle').addEventListener('click', () => {
  const show = $('pwd').type === 'password';
  $('pwd').type = show ? 'text' : 'password';
  $('toggle').textContent = show ? 'Hide' : 'Show';
  $('toggle').setAttribute('aria-label', show ? 'Hide password' : 'Show password');
});
function reset() {
  ['alertError', 'alertWarn'].forEach(i => $(i).style.display = 'none');
  ['empErr', 'pwdErr'].forEach(i => $(i).hidden = true);
  ['empId', 'pwd'].forEach(i => $(i).classList.remove('invalid'));
}
$('form').addEventListener('submit', e => {
  e.preventDefault(); reset();
  let ok = true;
  if (!$('empId').value.trim()) { $('empErr').hidden = false; $('empId').classList.add('invalid'); ok = false; }
  if (!$('pwd').value) { $('pwdErr').hidden = false; $('pwd').classList.add('invalid'); ok = false; }
  if (!ok) return;
  const s = $('scenario').value, btn = $('submit');
  btn.disabled = true; btn.textContent = 'Signing in…';
  setTimeout(() => {
    btn.disabled = false; btn.textContent = 'Sign in';
    if (s === 'ok') location.href = 'scr-sh-03-dashboard.html';
    else if (s === 'first') location.href = 'scr-sh-02-set-password.html?first=1';
    else if (s === 'bad') { $('alertError').textContent = 'Employee Id or password is incorrect. Please try again.'; $('alertError').style.display = 'block'; $('pwd').value = ''; $('pwd').focus(); }
    else if (s === 'inactive') { $('alertError').textContent = 'Your account is inactive. Contact your PMS administrator.'; $('alertError').style.display = 'block'; }
    else { $('alertWarn').textContent = 'Too many failed attempts. Your account is locked for 15 minutes.'; $('alertWarn').style.display = 'block'; }
  }, 600);
});
"""

SH01_CTRL = r"""Scenario on Sign in: <select id="scenario" aria-label="Scenario">
<option value="ok">Valid credentials → Dashboard</option><option value="first">First login (temporary password) → Set password</option>
<option value="bad">Wrong Employee Id or password (also: deactivated account with a wrong password)</option><option value="inactive">Deactivated account, correct password</option>
<option value="locked">Too many attempts (locked 15 min)</option></select>"""


def sh01():
    return standalone("SCR-SH-01", "Login", SH01_BODY, SH01_SCRIPT, SH01_CTRL)


PAGES = {
    "scr-sh-00-layout.html": sh00,
    "scr-sh-01-login.html": sh01,
    "scr-sh-02-set-password.html": sh02,
    "scr-sh-03-dashboard.html": sh03,
    "scr-sh-04-approvals.html": sh04,
}
