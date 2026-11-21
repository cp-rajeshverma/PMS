from base import shell

TEAM = r"""
const EMPS = [
  { id: 'EMP0002', name: 'Rahul Mehta', email: 'rahul.mehta@pms.local', mgr: '— (top-level)', doj: '15 Mar 2024', rate: '400.00', st: 'Submitted', active: true, role: 'Manager' },
  { id: 'EMP0007', name: 'Anita Sharma', email: 'anita.sharma@pms.local', mgr: 'Rahul Mehta (EMP0002)', doj: '01 Jul 2025', rate: '250.00', st: 'Approved', active: true, role: 'Employee', team: true },
  { id: 'EMP0008', name: 'Vikram Singh', email: 'vikram.singh@pms.local', mgr: 'Rahul Mehta (EMP0002)', doj: '18 Aug 2025', rate: '250.00', st: 'Approved', active: true, role: 'Employee', team: true },
  { id: 'EMP0009', name: 'Neha Gupta', email: 'neha.gupta@pms.local', mgr: 'Rahul Mehta (EMP0002)', doj: '05 Jan 2026', rate: '275.00', st: 'Approved', active: true, role: 'Employee', team: true },
  { id: 'EMP0010', name: 'Arjun Rao', email: 'arjun.rao@pms.local', mgr: 'Rahul Mehta (EMP0002)', doj: '12 Feb 2026', rate: '250.00', st: 'Rejected', active: true, role: 'Employee', team: true },
  { id: 'EMP0015', name: 'Deepak Verma', email: 'deepak.verma@pms.local', mgr: 'Rahul Mehta (EMP0002)', doj: '01 Apr 2025', rate: '250.00', st: 'Approved', active: false, role: 'Employee', team: true },
  { id: 'EMP0018', name: 'Meera Joshi', email: 'meera.joshi@pms.local', mgr: 'Rahul Mehta (EMP0002)', doj: '02 Nov 2026', rate: '250.00', st: 'Submitted', active: true, role: 'Employee', team: true },
  { id: 'EMP0019', name: 'Sameer Khan', email: 'sameer.khan@pms.local', mgr: 'Rahul Mehta (EMP0002)', doj: '09 Nov 2026', rate: '250.00', st: 'Draft', active: true, role: 'Employee', team: true },
  { id: 'EMP0020', name: 'Kavya Iyer', email: 'kavya.iyer@pms.local', mgr: 'Rahul Mehta (EMP0002)', doj: '16 Nov 2026', rate: '250.00', st: 'Draft', active: true, role: 'Employee', team: true }
];
"""

# ---------------------------------------------------------------- SCR-EIMS-01
E01_HEAD = r"""<div><h1 id="ttl">Employees</h1><p class="lead" id="sub">All employees in PMS.</p></div>
<div data-roles="admin"><a class="btn primary" href="scr-eims-02-admin-form.html">+ Onboard employee</a></div>"""

E01_BODY = r"""
<div class="toolbar">
  <input class="in" id="q" placeholder="Search by name, Employee Id or email" style="width:320px" aria-label="Search">
  <select class="in" id="fs" style="width:180px" aria-label="Profile status"><option value="">All profile statuses</option><option>Draft</option><option>Submitted</option><option>Approved</option><option>Rejected</option></select>
  <label class="small" style="display:inline-flex;gap:6px;align-items:center"><input type="checkbox" id="inact"> Show inactive</label>
  <span class="muted small" id="cnt" style="margin-left:auto"></span>
</div>
<div class="tbl-wrap">
  <table class="t"><thead><tr>
    <th>Employee Id</th><th>Name</th><th>Email</th><th id="thMgr">Manager</th><th>Joined</th><th class="num" id="thRate">Rate (₹/h)</th><th>Profile</th><th class="act">Actions</th>
  </tr></thead><tbody id="rows"></tbody></table>
</div>
<div class="card empty" id="empty" style="display:none"><b>No employees found</b>Try a different search or filter.</div>
"""

E01_MODAL = r"""
<div class="modal-bg" id="rpModal" role="dialog" aria-modal="true" aria-labelledby="rpTitle">
  <div class="modal">
    <h2 id="rpTitle">Reset password</h2>
    <div id="rpAsk"><p>Issue a new temporary password for <b id="rpWho"></b>? Their current password stops working immediately, and they must set a new one at next sign-in.</p>
      <div class="actions"><button class="btn" data-close>Cancel</button><button class="btn primary" id="rpOk">Reset password</button></div></div>
    <div id="rpDone" style="display:none"><div class="alert ok" style="margin-bottom:12px">Temporary password issued. It is shown only once — share it with the employee securely.</div>
      <div class="kv" style="margin-bottom:16px"><dt>Employee</dt><dd id="rpWho2"></dd><dt>Temporary password</dt><dd><code style="font-size:15px;background:var(--bg);padding:2px 8px;border-radius:4px">Tmp#8kQ2vL</code> <button class="btn sm" onclick="toast('Copied to clipboard.')">Copy</button></dd></div>
      <div class="actions"><button class="btn primary" data-close>Done</button></div></div>
  </div>
</div>
"""

E01_SCRIPT = TEAM + r"""
const badge = s => '<span class="badge b-' + s.toLowerCase() + '">' + s + '</span>';
function render() {
  const q = document.getElementById('q').value.toLowerCase(), fs = document.getElementById('fs').value, inact = document.getElementById('inact').checked;
  const admin = ROLE === 'admin';
  const list = EMPS.filter(e => (admin || e.team) && (inact || e.active) && (!fs || e.st === fs) &&
    (!q || (e.name + e.id + e.email).toLowerCase().includes(q)));
  document.getElementById('thRate').style.display = admin ? '' : 'none';
  document.getElementById('thMgr').style.display = admin ? '' : 'none';
  document.getElementById('rows').innerHTML = list.map(e =>
    '<tr' + (e.active ? '' : ' style="opacity:.6"') + '><td>' + e.id + '</td><td style="font-weight:500">' + e.name +
    (e.role !== 'Employee' ? ' <span class="chip">' + e.role.toUpperCase() + '</span>' : '') +
    (e.active ? '' : ' <span class="badge b-inactive">Inactive</span>') + '</td><td>' + e.email + '</td>' +
    (admin ? '<td>' + e.mgr + '</td>' : '') + '<td style="white-space:nowrap">' + e.doj + '</td>' + (admin ? '<td class="num">' + e.rate + '</td>' : '') +
    '<td>' + badge(e.st) + '</td><td class="act">' +
    (admin ? '<a class="btn sm" href="scr-eims-02-admin-form.html?mode=edit&id=' + e.id + '">Edit</a>' + (e.active ? '<button class="btn sm" data-rp="' + e.id + '">Reset password</button>' : '')
           : '<a class="btn sm" href="scr-eims-04-profile-review.html?mode=view">View</a>') + '</td></tr>').join('');
  document.getElementById('cnt').textContent = list.length + ' employee' + (list.length === 1 ? '' : 's');
  document.getElementById('empty').style.display = list.length ? 'none' : '';
  document.querySelector('.tbl-wrap').style.display = list.length ? '' : 'none';
}
function onRole(r) {
  document.getElementById('ttl').textContent = r === 'manager' ? 'My Team' : 'Employees';
  document.getElementById('sub').textContent = r === 'manager' ? 'Your direct reports (read-only).' : 'All employees in PMS. Hourly rates are visible to Admin only.';
  render();
}
['q', 'fs', 'inact'].forEach(i => document.getElementById(i).addEventListener('input', render));
const m = document.getElementById('rpModal');
document.getElementById('rows').addEventListener('click', e => {
  const b = e.target.closest('[data-rp]'); if (!b) return;
  const emp = EMPS.find(x => x.id === b.dataset.rp);
  document.getElementById('rpWho').textContent = emp.name + ' (' + emp.id + ')';
  document.getElementById('rpWho2').textContent = emp.name + ' (' + emp.id + ')';
  document.getElementById('rpAsk').style.display = ''; document.getElementById('rpDone').style.display = 'none'; m.classList.add('open');
});
document.getElementById('rpOk').onclick = () => { document.getElementById('rpAsk').style.display = 'none'; document.getElementById('rpDone').style.display = ''; };
m.querySelectorAll('[data-close]').forEach(b => b.onclick = () => m.classList.remove('open'));
"""


def e01():
    return shell("SCR-EIMS-01", "Employee directory", "employees", "People / Employees", E01_HEAD, E01_BODY, E01_SCRIPT,
                 roles=("admin", "manager"), default="admin", modal=E01_MODAL)


# ---------------------------------------------------------------- SCR-EIMS-02
E02_HEAD = r"""<div><h1 id="ttl">Onboard employee</h1><p class="lead" id="sub">Create the employee with basic details. The employee completes the rest of the profile.</p></div>
<div id="stBadges"></div>"""

E02_BODY = r"""
<div class="alert ok" id="created" style="display:none;margin-bottom:16px" role="status">
  <b>Employee created.</b> Share these sign-in details with the employee securely. The temporary password is shown only once.
  <div class="kv" style="margin-top:10px"><dt>Employee Id</dt><dd><b>EMP0021</b></dd><dt>Temporary password</dt><dd><code style="background:#fff;padding:2px 8px;border-radius:4px">Tmp#4rTz9W</code> <button class="btn sm" onclick="toast('Copied to clipboard.')">Copy</button></dd></div>
  <div style="margin-top:10px"><a href="scr-eims-01-directory.html">Back to employees</a> · <a href="scr-eims-02-admin-form.html">Onboard another</a></div>
</div>
<form class="card" id="form" novalidate>
  <div class="section-title">Identity</div>
  <div class="form-grid">
    <div class="field"><label>Employee Id</label><input class="in" id="eid" value="Generated on save" readonly></div>
  </div>
  <div class="section-title">Name</div>
  <div class="form-grid">
    <div class="field"><label for="fn" class="req">First name</label><input class="in" id="fn" maxlength="50"><div class="err-text" hidden>Enter a first name.</div></div>
    <div class="field"><label for="mn">Middle name</label><input class="in" id="mn" maxlength="50"></div>
    <div class="field"><label for="ln" class="req">Last name</label><input class="in" id="ln" maxlength="50"><div class="err-text" hidden>Enter a last name.</div></div>
  </div>
  <div class="section-title">Employment and pay</div>
  <div class="form-grid">
    <div class="field"><label for="em" class="req">Email</label><input class="in" id="em" type="email"><div class="err-text" hidden>Enter a valid email that is not used by another employee.</div></div>
    <div class="field"><label for="doj" class="req">Date of joining</label><input class="in" id="doj" type="date" max="2026-11-16"><div class="err-text" hidden>Date of joining cannot be after today.</div></div>
    <div class="field"><label for="role" class="req">Role</label><select class="in" id="role"><option>Employee</option><option>Manager</option></select><div class="hint">Managers can approve their direct reports.</div></div>
    <div class="field"><label for="mgr" class="req">Manager</label><select class="in" id="mgr"><option value="">Select manager…</option><option>Rahul Mehta (EMP0002)</option><option>None – top-level (approved by Admin)</option></select><div class="err-text" hidden>Select an active manager.</div><div class="hint">Approves this employee's profile, attendance, leave and salary.</div></div>
    <div class="field"><label for="rate" class="req">Hourly wage rate (₹)</label><input class="in" id="rate" inputmode="decimal" placeholder="e.g. 250.00"><div class="err-text" hidden>Enter an amount greater than 0, up to 2 decimals.</div><div class="hint" id="rateHint">Used for every new salary record.</div></div>
  </div>
  <div id="danger" style="display:none;border-top:1px solid var(--border);margin-top:8px;padding-top:16px">
    <div class="section-title">Account</div>
    <div style="display:flex;gap:12px;align-items:center"><button type="button" class="btn danger" id="deact">Deactivate employee</button><span class="small muted">The employee can no longer sign in. Their records are kept.</span></div>
  </div>
  <div class="form-actions"><a class="btn" href="scr-eims-01-directory.html">Cancel</a><button class="btn primary" type="submit" id="save">Create employee</button></div>
</form>
"""

E02_MODAL = r"""
<div class="modal-bg" id="dModal" role="dialog" aria-modal="true" aria-labelledby="dTitle">
  <div class="modal"><h2 id="dTitle">Deactivate Anita Sharma?</h2>
    <p>Anita can no longer sign in, and will not appear in active lists. All profile, attendance, leave and salary records are kept. Open items waiting for her action stay as they are.</p>
    <div class="actions"><button class="btn" id="dNo">Cancel</button><button class="btn danger" id="dYes">Deactivate</button></div></div>
</div>
"""

E02_SCRIPT = r"""
const $ = id => document.getElementById(id);
function setMode(m) {
  const edit = m === 'edit';
  $('ttl').textContent = edit ? 'Edit employee · Anita Sharma' : 'Onboard employee';
  $('sub').textContent = edit ? 'Admin-managed details. Personal details are maintained by the employee in My Profile.' : 'Create the employee with basic details. The employee completes the rest of the profile.';
  $('eid').value = edit ? 'EMP0007' : 'Generated on save';
  if (edit) { $('fn').value = 'Anita'; $('ln').value = 'Sharma'; $('em').value = 'anita.sharma@pms.local'; $('doj').value = '2025-07-01'; $('mgr').value = 'Rahul Mehta (EMP0002)'; $('rate').value = '250.00'; }
  ['fn', 'mn', 'ln', 'em'].forEach(i => $(i).readOnly = edit);
  $('rateHint').textContent = edit ? 'A change applies to salary records generated from now on. Past records keep their rate.' : 'Used for every new salary record.';
  $('danger').style.display = edit ? '' : 'none';
  $('stBadges').innerHTML = edit ? '<span class="badge b-approved">Profile approved</span> <span class="badge b-approved">Active</span>' : '';
  $('save').textContent = edit ? 'Save changes' : 'Create employee';
  $('mode').value = m; $('created').style.display = 'none'; $('form').style.display = '';
}
$('mode').addEventListener('change', e => setMode(e.target.value));
setMode(new URLSearchParams(location.search).get('mode') === 'edit' ? 'edit' : 'create');
function err(id, bad) { const f = $(id); f.classList.toggle('invalid', bad); const t = f.parentElement.querySelector('.err-text'); if (t) t.hidden = !bad; return bad; }
$('form').addEventListener('submit', e => {
  e.preventDefault();
  let bad = false;
  bad = err('fn', !$('fn').value.trim()) | bad;
  bad = err('ln', !$('ln').value.trim()) | bad;
  bad = err('em', !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test($('em').value) || $('em').value === 'vikram.singh@pms.local') | bad;
  bad = err('doj', !$('doj').value || $('doj').value > '2026-11-16') | bad;
  bad = err('mgr', !$('mgr').value) | bad;
  bad = err('rate', !/^\d+(\.\d{1,2})?$/.test($('rate').value) || +$('rate').value <= 0) | bad;
  if (bad) return;
  if ($('mode').value === 'edit') { toast('Changes saved.'); return; }
  $('form').style.display = 'none'; $('created').style.display = ''; window.scrollTo(0, 0);
});
$('deact').onclick = () => $('dModal').classList.add('open');
$('dNo').onclick = () => $('dModal').classList.remove('open');
$('dYes').onclick = () => { $('dModal').classList.remove('open'); $('stBadges').innerHTML = '<span class="badge b-approved">Profile approved</span> <span class="badge b-inactive">Inactive</span>'; $('deact').disabled = true; toast('Anita Sharma deactivated.'); };
"""

E02_CTRL = r""" Mode: <select id="mode" aria-label="Mode"><option value="create">Create (onboard)</option><option value="edit">Edit existing</option></select>
<span>Tip: email vikram.singh@pms.local shows the duplicate error</span>"""


def e02():
    return shell("SCR-EIMS-02", "Employee admin form", "employees", "People / Employees / Onboard", E02_HEAD, E02_BODY, E02_SCRIPT,
                 roles=("admin",), default="admin", extra_controls=E02_CTRL, modal=E02_MODAL)


# ---------------------------------------------------------------- SCR-EIMS-03
E03_HEAD = r"""<div><h1>My Profile</h1><p class="lead">Your personal details. Your manager approves your profile and every change request.</p></div><div id="stBadge"></div>"""

def _f(fid, label, req=True, typ="text", val="", hint="", ph=""):
    r = ' class="req"' if req else ''
    h = f'<div class="hint">{hint}</div>' if hint else ''
    p = f' placeholder="{ph}"' if ph else ''
    return (f'<div class="field"><label for="{fid}"{r}>{label}</label><input class="in pf" id="{fid}" type="{typ}" value="{val}"{p}>'
            f'<div class="err-text" hidden></div>{h}</div>')

def _country(fid, label, val="India"):
    opts = "".join(f'<option{" selected" if c == val else ""}>{c}</option>' for c in ["India", "Nepal", "Sri Lanka", "United Arab Emirates", "United Kingdom", "United States", "Other"])
    return f'<div class="field"><label for="{fid}" class="req">{label}</label><select class="in pf" id="{fid}">{opts}</select></div>'

E03_BODY = (r"""
<div class="alert" id="banner" style="margin-bottom:16px" role="status"></div>
<form class="card" id="form" novalidate>
  <div class="section-title">Set by your administrator</div>
  <dl class="kv" style="margin:0 0 20px">
    <dt>Employee Id</dt><dd>EMP0007</dd><dt>Manager</dt><dd>Rahul Mehta (EMP0002)</dd>
    <dt>Date of joining</dt><dd>01 Jul 2025</dd><dt>Hourly wage rate</dt><dd>₹ 250.00</dd>
  </dl>
  <div class="section-title">Name</div><div class="form-grid">"""
 + _f("fn", "First name", val="Anita") + _f("mn", "Middle name", req=False) + _f("ln", "Last name", val="Sharma") +
 r"""</div><div class="section-title">Parents</div><div class="form-grid">"""
 + _f("fa", "Father's name", val="Suresh Sharma") + _f("mo", "Mother's name", val="Kamla Sharma") +
 r"""</div><div class="section-title">Birth</div><div class="form-grid">"""
 + _f("dob", "Date of birth", typ="date", val="1998-04-12", hint="You must be at least 18 on your date of joining.") + _f("pob", "Place of birth", val="Jaipur") + _country("cob", "Country of birth") +
 r"""</div><div class="section-title">Employment</div><div class="form-grid">"""
 + _f("le", "Last employer", req=False, val="Acme Retail Pvt Ltd") +
 r"""</div><div class="section-title">Address</div><div class="form-grid">"""
 + _f("a1", "Address line 1", val="Flat 402, Lotus Residency") + _f("a2", "Address line 2", req=False, val="MG Road") + _f("ci", "City", val="Pune")
 + _f("stt", "State", val="Maharashtra") + _country("co", "Country") + _f("zip", "Zip / PIN code", val="411001") +
 r"""</div><div class="section-title">Contact</div><div class="form-grid">"""
 + _f("em", "Email", typ="email", val="anita.sharma@pms.local") + _f("mob", "Mobile number", val="9876543210", hint="10 digits, no country code.") +
 r"""</div>
  <div class="form-actions" id="actions">
    <button type="button" class="btn danger" id="wdr">Withdraw request</button>
    <button type="button" class="btn" id="draft">Save draft</button>
    <button type="submit" class="btn primary" id="submit">Submit for approval</button>
  </div>
  <div class="form-actions" id="wdBar" style="display:none"><button type="button" class="btn" id="wdSub">Withdraw</button></div>
  <div class="form-actions" id="editBar" style="display:none"><button type="button" class="btn primary" id="edit">Request a change</button></div>
</form>
""")

E03_SCRIPT = r"""
const $ = id => document.getElementById(id);
const B = {
  Draft: ['info', 'Complete your profile and submit it for approval. You can start entering attendance and leave once it is approved.'],
  Submitted: ['info', 'Submitted on 15 Nov 2026, 10:20 — waiting for Rahul Mehta to approve. You can withdraw it to make changes until a decision is taken.'],
  Approved: ['ok', 'Approved by Rahul Mehta on 02 Nov 2026. To change your details, request a change; your approved profile stays in use until the change is approved.'],
  Rejected: ['error', 'Rejected by Rahul Mehta on 14 Nov 2026: "Mobile number looks incomplete, please correct it." Fix and submit again.'],
  'CR Draft': ['warn', 'Profile change request (draft). Change the fields you need; changed fields are marked. Your approved profile stays in use until the change is approved.'],
  'CR Submitted': ['info', 'Change request submitted on 18 Nov 2026, 11:05 — waiting for Rahul Mehta. Your approved profile stays in use meanwhile. You can withdraw the request until a decision is taken.'],
  'CR Rejected': ['error', 'Change request rejected by Rahul Mehta on 19 Nov 2026: "Please give the full address including the flat number." Correct and submit again, or withdraw the request.']
};
const ORIG = {}; document.querySelectorAll('.pf').forEach(f => ORIG[f.id] = f.value);
function mark() { document.querySelectorAll('.pf').forEach(f => { const ch = state.startsWith('CR') && f.value !== ORIG[f.id];
  f.style.background = ch ? 'var(--warning-tint)' : ''; const l = document.querySelector('label[for=' + f.id + ']');
  if (l) { const b = l.querySelector('.badge'); if (ch && !b) l.insertAdjacentHTML('beforeend', ' <span class="badge b-warn">Changed</span>'); if (!ch && b) b.remove(); } }); }
document.querySelectorAll('.pf').forEach(f => f.addEventListener('input', mark));
let state;
function setState(s) {
  state = s; $('stat').value = s;
  const cr = s.startsWith('CR'), ro = s === 'Submitted' || s === 'Approved' || s === 'CR Submitted';
  if (s === 'Approved') document.querySelectorAll('.pf').forEach(f => f.value = ORIG[f.id]);
  if (s === 'CR Submitted' || s === 'CR Rejected') $('a1').value = 'Flat 7, Green Park';
  document.querySelectorAll('.pf').forEach(f => { f.readOnly = ro; f.disabled = ro && f.tagName === 'SELECT'; });
  $('banner').className = 'alert ' + B[s][0]; $('banner').textContent = B[s][1];
  const badge = cr ? '<span class="badge b-approved">Approved</span> <span class="badge b-' + (s === 'CR Draft' ? 'draft">Change request: Draft' : s === 'CR Submitted' ? 'submitted">Change request: Submitted' : 'rejected">Change request: Rejected') + '</span>'
                   : '<span class="badge b-' + s.toLowerCase() + '">' + s + '</span>';
  $('stBadge').innerHTML = badge;
  $('actions').style.display = ro ? 'none' : ''; $('editBar').style.display = s === 'Approved' ? '' : 'none';
  $('wdBar').style.display = s === 'Submitted' || s === 'CR Submitted' ? '' : 'none';
  $('wdSub').textContent = s === 'CR Submitted' ? 'Withdraw request' : 'Withdraw';
  $('wdr').style.display = cr ? '' : 'none';
  $('submit').textContent = cr ? 'Submit change request' : 'Submit for approval';
  if (s === 'Rejected') { $('mob').value = '98765432'; } else if ($('mob').value === '98765432') $('mob').value = '9876543210';
  mark();
}
$('stat').addEventListener('change', e => setState(e.target.value));
$('edit').onclick = () => setState('CR Draft');
$('wdSub').onclick = () => { if (state === 'CR Submitted') { setState('Approved'); toast('Change request withdrawn.'); } else { setState('Draft'); toast('Profile withdrawn. You can edit it again.'); } };
$('wdr').onclick = () => { setState('Approved'); toast('Change request withdrawn.'); };
$('draft').onclick = () => toast('Draft saved.');
function err(id, msg) { const f = $(id), t = f.parentElement.querySelector('.err-text'); f.classList.toggle('invalid', !!msg); if (t) { t.hidden = !msg; t.textContent = msg || ''; } return !!msg; }
$('form').addEventListener('submit', e => {
  e.preventDefault(); let bad = false;
  ['fn', 'ln', 'fa', 'mo', 'pob', 'a1', 'ci', 'stt', 'zip'].forEach(i => bad = err(i, $(i).value.trim() ? '' : 'This field is required.') || bad);
  bad = err('dob', $('dob').value && $('dob').value <= '2007-07-01' ? '' : 'You must be at least 18 years old on your date of joining (01 Jul 2025).') || bad;
  bad = err('em', /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test($('em').value) ? '' : 'Enter a valid email address.') || bad;
  bad = err('mob', /^\d{10}$/.test($('mob').value) ? '' : 'Enter a 10-digit mobile number.') || bad;
  if (bad) { toast('Please correct the highlighted fields.'); return; }
  if (state.startsWith('CR')) {
    if (![...document.querySelectorAll('.pf')].some(f => f.value !== ORIG[f.id])) { toast('No changes to submit.'); return; }
    setState('CR Submitted'); toast('Change request submitted to Rahul Mehta for approval.'); window.scrollTo(0, 0); return;
  }
  setState('Submitted'); toast('Profile submitted to Rahul Mehta for approval.'); window.scrollTo(0, 0);
});
setState('Approved');
"""

E03_CTRL = r""" Profile status: <select id="stat" aria-label="Profile status"><option>Draft</option><option>Submitted</option><option selected>Approved</option><option>Rejected</option><option>CR Draft</option><option>CR Submitted</option><option>CR Rejected</option></select>"""


def e03():
    return shell("SCR-EIMS-03", "My profile", "profile", "My work / My Profile", E03_HEAD, E03_BODY, E03_SCRIPT,
                 roles=("employee", "manager"), default="employee", extra_controls=E03_CTRL)


# ---------------------------------------------------------------- SCR-EIMS-04
E04_HEAD = r"""<div><h1>Profile review · Meera Joshi</h1><p class="lead" id="sub">EMP0018 · joined 02 Nov 2026 · submitted 15 Nov 2026, 09:12</p></div><div id="stBadge"><span class="badge b-submitted">Submitted</span></div>"""

E04_BODY = r"""
<div class="alert info" id="banner" style="margin-bottom:16px"></div>
<div class="card">
  <table class="t" id="tbl">
    <thead><tr><th style="width:22%">Field</th><th id="thOld">Previously approved</th><th id="thNew">Submitted</th></tr></thead>
    <tbody id="rows"></tbody>
  </table>
  <div class="form-actions" id="acts"><a class="btn" href="scr-sh-04-approvals.html">Back</a><button class="btn danger" id="rej">Reject</button><button class="btn primary" id="apr">Approve</button></div>
  <div class="form-actions" id="back" style="display:none"><a class="btn" href="scr-eims-01-directory.html">Back to My Team</a></div>
</div>
"""

E04_MODAL = r"""
<div class="modal-bg" id="rjModal" role="dialog" aria-modal="true" aria-labelledby="rjT">
  <div class="modal"><h2 id="rjT">Reject profile</h2>
    <div class="field"><label for="rjText" class="req">Remarks for the employee</label><textarea class="in" id="rjText" placeholder="Explain what needs to be corrected"></textarea><div class="err-text" id="rjErr" hidden>Remarks are required to reject.</div></div>
    <div class="actions"><button class="btn" id="rjNo">Cancel</button><button class="btn danger" id="rjYes">Reject</button></div></div>
</div>
"""

E04_SCRIPT = r"""
const $ = id => document.getElementById(id);
const F = [
  ['Name', 'Meera Joshi', 'Meera Joshi'], ['Father\'s name', 'Anil Joshi', 'Anil Joshi'], ['Mother\'s name', 'Sunita Joshi', 'Sunita Joshi'],
  ['Date of birth', '23 Sep 1999', '23 Sep 1999'], ['Place / country of birth', 'Nagpur, India', 'Nagpur, India'],
  ['Last employer', 'Brightway Logistics', 'Brightway Logistics'],
  ['Address', 'B-12, Shanti Nagar, Nagpur, Maharashtra, India 440010', 'Flat 7, Green Park, Baner, Pune, Maharashtra, India 411045'],
  ['Email', 'meera.joshi@pms.local', 'meera.joshi@pms.local'], ['Mobile number', '9822012345', '9822054321']
];
function setMode(m) {
  $('mode').value = m;
  const upd = m === 'update' || m === 'withdrawn', view = m === 'view';
  $('thOld').style.display = upd ? '' : 'none';
  $('thOld').textContent = 'Approved profile';
  $('thNew').textContent = view ? 'Value' : (upd ? 'Requested change' : 'Submitted');
  $('rows').innerHTML = F.map(([k, o, n]) => { const ch = upd && o !== n;
    return '<tr' + (ch ? ' style="background:var(--warning-tint)"' : '') + '><td class="muted">' + k + '</td>' + (upd ? '<td' + (ch ? ' style="text-decoration:line-through;color:var(--text-3)"' : '') + '>' + o + '</td>' : '') +
      '<td>' + n + (ch ? ' <span class="badge b-warn">Changed</span>' : '') + '</td></tr>'; }).join('');
  const wd = m === 'withdrawn';
  $('banner').style.display = view ? 'none' : '';
  $('banner').className = 'alert ' + (wd ? 'warn' : 'info');
  $('banner').textContent = wd ? 'Withdrawn by the employee on 18 Nov 2026, 14:30. No action is possible.' : upd ? 'Profile change request: 2 fields changed (highlighted). The profile stays Approved; approving applies the new values.' : 'New profile, first submission. Check the details before approving.';
  $('acts').style.display = view || wd ? 'none' : ''; $('back').style.display = view ? '' : 'none';
  $('stBadge').innerHTML = view ? '<span class="badge b-approved">Approved</span>' : wd ? '<span class="badge b-cancelled">Withdrawn</span>' : upd ? '<span class="badge b-approved">Approved</span> <span class="badge b-submitted">Change request: Submitted</span>' : '<span class="badge b-submitted">Submitted</span>';
}
$('mode').addEventListener('change', e => setMode(e.target.value));
setMode(new URLSearchParams(location.search).get('mode') || 'update');
$('apr').onclick = () => { $('acts').style.display = 'none'; $('stBadge').innerHTML = '<span class="badge b-approved">Approved</span>'; toast('Profile approved.'); };
$('rej').onclick = () => { $('rjText').value = ''; $('rjErr').hidden = true; $('rjModal').classList.add('open'); };
$('rjNo').onclick = () => $('rjModal').classList.remove('open');
$('rjYes').onclick = () => { if (!$('rjText').value.trim()) { $('rjErr').hidden = false; return; } $('rjModal').classList.remove('open'); $('acts').style.display = 'none'; $('stBadge').innerHTML = '<span class="badge b-rejected">Rejected</span>'; toast('Profile rejected and returned to Meera Joshi.'); };
"""

E04_CTRL = r""" Case: <select id="mode" aria-label="Case"><option value="new">New profile (first submission)</option><option value="update" selected>Profile change request</option><option value="withdrawn">Change request withdrawn by the employee</option><option value="view">Read-only view (from My Team)</option></select>"""


def e04():
    return shell("SCR-EIMS-04", "Profile review", "approvals", "Approvals / Profile review", E04_HEAD, E04_BODY, E04_SCRIPT,
                 roles=("manager", "admin"), default="manager", extra_controls=E04_CTRL, modal=E04_MODAL)


PAGES = {
    "scr-eims-01-directory.html": e01,
    "scr-eims-02-admin-form.html": e02,
    "scr-eims-03-my-profile.html": e03,
    "scr-eims-04-profile-review.html": e04,
}
