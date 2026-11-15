"""Shared building blocks for PMS mockups (approved style, D-27)."""

CSS = r"""
  :root {
    --bg: #f5f7fa; --surface: #ffffff; --border: #dde3ea; --border-strong: #c3ccd7;
    --text: #1f2933; --text-2: #52606d; --text-3: #7b8794;
    --primary: #1f5fae; --primary-hover: #184d8e; --primary-tint: #e8f0fa;
    --success: #1e7b4f; --success-tint: #e3f4ea; --warning: #a35f00; --warning-tint: #fdf1dc;
    --danger: #b42318; --danger-tint: #fdeceb; --muted-tint: #eef1f4;
    --radius: 8px; --shadow: 0 1px 2px rgba(16,24,40,.06);
    --font: "Segoe UI", system-ui, -apple-system, Roboto, Arial, sans-serif;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; min-height: 100%; }
  body { font: 14px/1.5 var(--font); color: var(--text); background: var(--bg); }
  a { color: var(--primary); text-decoration: none; }
  a:hover { text-decoration: underline; }
  button { font: inherit; cursor: pointer; }
  :focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; }

  .mock-bar { background: #fff8db; border-bottom: 1px dashed #d4a800; padding: 6px 24px; font-size: 12px; color: #5c4a00; display: flex; gap: 16px; align-items: center; flex-wrap: wrap; }
  .mock-bar strong { letter-spacing: .04em; text-transform: uppercase; font-size: 11px; }
  .mock-bar label { display: inline-flex; gap: 4px; align-items: center; cursor: pointer; }
  .mock-bar select { font: inherit; font-size: 12px; }
  .mock-id { margin-left: auto; }

  .app { display: grid; grid-template-columns: 232px 1fr; grid-template-rows: 56px 1fr; min-height: calc(100vh - 31px); }
  .header { grid-column: 1 / -1; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; background: var(--surface); border-bottom: 1px solid var(--border); }
  .brand { display: flex; align-items: center; gap: 10px; font-weight: 600; font-size: 16px; }
  .brand-mark { width: 28px; height: 28px; border-radius: 6px; background: var(--primary); color: #fff; display: grid; place-items: center; font-size: 13px; font-weight: 700; }
  .brand small { font-weight: 400; color: var(--text-3); font-size: 13px; }
  .user { position: relative; }
  .user-btn { display: flex; align-items: center; gap: 10px; background: none; border: 1px solid transparent; border-radius: var(--radius); padding: 4px 8px; }
  .user-btn:hover { border-color: var(--border); }
  .avatar { width: 32px; height: 32px; border-radius: 50%; background: var(--primary-tint); color: var(--primary); display: grid; place-items: center; font-weight: 600; font-size: 13px; }
  .user-meta { text-align: left; line-height: 1.2; }
  .user-meta span { display: block; font-size: 12px; color: var(--text-3); }
  .menu-pop { position: absolute; right: 0; top: 46px; width: 200px; background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); box-shadow: 0 8px 24px rgba(16,24,40,.12); padding: 6px; display: none; z-index: 10; }
  .menu-pop.open { display: block; }
  .menu-pop a { display: block; padding: 8px 10px; border-radius: 6px; color: var(--text); }
  .menu-pop a:hover { background: var(--bg); text-decoration: none; }
  .menu-pop hr { border: 0; border-top: 1px solid var(--border); margin: 6px 0; }
  .side { background: var(--surface); border-right: 1px solid var(--border); padding: 16px 12px; }
  .nav a { display: flex; align-items: center; justify-content: space-between; padding: 9px 12px; border-radius: var(--radius); color: var(--text-2); font-weight: 500; margin-bottom: 2px; }
  .nav a:hover { background: var(--bg); text-decoration: none; color: var(--text); }
  .nav a.active { background: var(--primary-tint); color: var(--primary); }
  .count { background: var(--danger); color: #fff; border-radius: 10px; font-size: 11px; font-weight: 600; padding: 1px 7px; }
  .nav-label { font-size: 11px; text-transform: uppercase; letter-spacing: .06em; color: var(--text-3); padding: 14px 12px 6px; }
  .main { padding: 24px 32px; min-width: 0; }
  .crumbs { font-size: 12px; color: var(--text-3); margin-bottom: 4px; }
  .page-head { display: flex; align-items: flex-end; justify-content: space-between; gap: 16px; margin-bottom: 20px; }
  h1 { font-size: 22px; font-weight: 600; margin: 0; }
  h2 { font-size: 16px; font-weight: 600; margin: 0 0 12px; }
  .lead { color: var(--text-2); margin: 4px 0 0; }
  .footer { font-size: 12px; color: var(--text-3); margin-top: 24px; }

  /* Components */
  .card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); box-shadow: var(--shadow); padding: 20px; }
  .grid { display: grid; gap: 16px; }
  .g2 { grid-template-columns: repeat(2, 1fr); } .g3 { grid-template-columns: repeat(3, 1fr); } .g4 { grid-template-columns: repeat(4, 1fr); }
  .stack > * + * { margin-top: 16px; }
  .tile .k { font-size: 12px; color: var(--text-3); text-transform: uppercase; letter-spacing: .04em; }
  .tile .v { font-size: 24px; font-weight: 600; margin-top: 4px; }
  .tile .s { font-size: 12px; color: var(--text-2); }
  .btn { display: inline-flex; align-items: center; gap: 6px; height: 36px; padding: 0 14px; border-radius: var(--radius); border: 1px solid var(--border-strong); background: var(--surface); color: var(--text); font-weight: 500; white-space: nowrap; }
  .btn:hover { background: var(--bg); text-decoration: none; }
  .btn.primary { background: var(--primary); border-color: var(--primary); color: #fff; }
  .btn.primary:hover { background: var(--primary-hover); }
  .btn.danger { color: var(--danger); border-color: #f0b8b2; }
  .btn.danger:hover { background: var(--danger-tint); }
  .btn.sm { height: 30px; padding: 0 10px; font-size: 13px; }
  .btn[disabled] { opacity: .5; cursor: not-allowed; }
  .badge { display: inline-block; font-size: 12px; font-weight: 600; padding: 2px 8px; border-radius: 10px; background: var(--muted-tint); color: var(--text-2); white-space: nowrap; }
  .b-draft { background: var(--muted-tint); color: var(--text-2); }
  .b-submitted, .b-generated { background: var(--primary-tint); color: var(--primary); }
  .b-approved, .b-accepted, .b-mgrapproved { background: var(--success-tint); color: var(--success); }
  .b-rejected, .b-disputed { background: var(--danger-tint); color: var(--danger); }
  .b-cancelled, .b-voided, .b-inactive { background: var(--muted-tint); color: var(--text-3); }
  .b-warn { background: var(--warning-tint); color: var(--warning); }
  .chip { display: inline-block; font-size: 11px; font-weight: 600; letter-spacing: .03em; padding: 1px 6px; border-radius: 4px; border: 1px solid var(--border-strong); color: var(--text-2); }
  table.t { width: 100%; border-collapse: collapse; background: var(--surface); }
  .t th { text-align: left; font-size: 12px; font-weight: 600; color: var(--text-3); text-transform: uppercase; letter-spacing: .03em; padding: 10px 12px; border-bottom: 1px solid var(--border); background: #fafbfc; }
  .t td { padding: 11px 12px; border-bottom: 1px solid var(--border); vertical-align: middle; }
  .t tr:last-child td { border-bottom: 0; }
  .t tr:hover td { background: #fafcff; }
  .t .num { text-align: right; font-variant-numeric: tabular-nums; }
  .t .act { text-align: right; white-space: nowrap; }
  .t .act .btn + .btn { margin-left: 6px; }
  .tbl-wrap { border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow); }
  .muted { color: var(--text-3); } .small { font-size: 12px; }
  .tabs { display: flex; gap: 4px; border-bottom: 1px solid var(--border); margin-bottom: 16px; }
  .tabs a { padding: 8px 14px; color: var(--text-2); font-weight: 500; border-bottom: 2px solid transparent; margin-bottom: -1px; }
  .tabs a:hover { text-decoration: none; color: var(--text); }
  .tabs a.on { color: var(--primary); border-color: var(--primary); }
  .tabs .count { background: var(--muted-tint); color: var(--text-2); margin-left: 6px; }
  .tabs a.on .count { background: var(--primary-tint); color: var(--primary); }
  .toolbar { display: flex; gap: 12px; align-items: center; margin-bottom: 12px; flex-wrap: wrap; }
  .bulk { display: none; align-items: center; gap: 12px; background: var(--primary-tint); border: 1px solid #c5d8f0; border-radius: var(--radius); padding: 8px 12px; margin-bottom: 12px; }
  .bulk.show { display: flex; }
  .field { margin-bottom: 16px; }
  .field label, .lbl { display: block; font-weight: 500; margin-bottom: 6px; }
  .req::after { content: " *"; color: var(--danger); }
  .in, select.in, textarea.in { width: 100%; height: 38px; border: 1px solid var(--border-strong); border-radius: var(--radius); padding: 0 12px; font: inherit; color: var(--text); background: #fff; }
  textarea.in { height: 88px; padding: 8px 12px; resize: vertical; }
  .in:focus { border-color: var(--primary); outline: none; box-shadow: 0 0 0 3px var(--primary-tint); }
  .in.invalid { border-color: var(--danger); }
  .in[readonly], .in:disabled { background: var(--bg); color: var(--text-2); }
  .hint { font-size: 12px; color: var(--text-3); margin-top: 4px; }
  .err-text { font-size: 12px; color: var(--danger); margin-top: 4px; }
  .alert { border-radius: var(--radius); padding: 10px 14px; font-size: 13px; border: 1px solid; }
  .alert.info { background: var(--primary-tint); color: #17457d; border-color: #c5d8f0; }
  .alert.error { background: var(--danger-tint); color: var(--danger); border-color: #f5c2bd; }
  .alert.warn { background: var(--warning-tint); color: var(--warning); border-color: #f3d29a; }
  .alert.ok { background: var(--success-tint); color: var(--success); border-color: #b5dfc6; }
  .empty { text-align: center; padding: 48px 16px; color: var(--text-3); }
  .empty b { display: block; color: var(--text-2); font-size: 15px; margin-bottom: 4px; }
  .modal-bg { position: fixed; inset: 0; background: rgba(16,24,40,.45); display: none; align-items: center; justify-content: center; z-index: 50; }
  .modal-bg.open { display: flex; }
  .modal { background: var(--surface); border-radius: 12px; width: 480px; padding: 24px; box-shadow: 0 20px 48px rgba(16,24,40,.25); }
  .modal h2 { font-size: 18px; }
  .modal .actions { display: flex; justify-content: flex-end; gap: 8px; margin-top: 8px; }
  .toast { position: fixed; bottom: 24px; right: 24px; background: #1f2933; color: #fff; padding: 12px 16px; border-radius: var(--radius); box-shadow: 0 8px 24px rgba(16,24,40,.25); display: none; z-index: 60; }
  .toast.show { display: block; }
  .list-row { display: flex; align-items: center; justify-content: space-between; gap: 12px; padding: 12px 0; border-bottom: 1px solid var(--border); }
  .list-row:last-child { border-bottom: 0; }
  .list-row .t1 { font-weight: 500; }
  .list-row .t2 { font-size: 12px; color: var(--text-3); }
  .dot { width: 8px; height: 8px; border-radius: 50%; display: inline-block; margin-right: 8px; }
  .kv { display: grid; grid-template-columns: 180px 1fr; gap: 8px 16px; }
  .kv dt { color: var(--text-3); } .kv dd { margin: 0; }
  .section-title { font-size: 12px; text-transform: uppercase; letter-spacing: .06em; color: var(--text-3); font-weight: 600; margin: 4px 0 12px; }
  .form-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0 20px; }
  .form-actions { display: flex; gap: 8px; justify-content: flex-end; padding-top: 16px; border-top: 1px solid var(--border); margin-top: 8px; }
  [data-show] { display: none; }

  .opt { display: inline-flex; gap: 8px; align-items: center; border: 1px solid var(--border-strong); border-radius: var(--radius); padding: 8px 16px; cursor: pointer; background: var(--surface); }
  .opt:has(input:checked) { border-color: var(--primary); background: var(--primary-tint); color: var(--primary); font-weight: 500; }

  /* Calendar (attendance) */
  .cal-head { display: grid; grid-template-columns: repeat(7, 1fr); background: #fafbfc; border-bottom: 1px solid var(--border); }
  .cal-head div { padding: 8px 12px; font-size: 12px; font-weight: 600; color: var(--text-3); text-transform: uppercase; }
  .cal-grid { display: grid; grid-template-columns: repeat(7, 1fr); }
  .cell { min-height: 92px; border-right: 1px solid var(--border); border-bottom: 1px solid var(--border); padding: 8px 10px; display: flex; flex-direction: column; gap: 4px; text-align: left; background: var(--surface); font: inherit; color: inherit; border-top: 0; border-left: 0; }
  .cell:nth-child(7n) { border-right: 0; }
  button.cell { cursor: pointer; } button.cell:hover { background: #f7faff; }
  .cell .d { font-weight: 600; font-size: 13px; }
  .cell.out { background: #fafbfc; color: var(--text-3); }
  .cell.future { background: #fafbfc; color: var(--text-3); cursor: default; }
  .cell.today .d { color: #fff; background: var(--primary); border-radius: 10px; padding: 0 7px; align-self: flex-start; }
  .cell.missing { box-shadow: inset 0 0 0 2px #f3d29a; }
  .cell .h { font-size: 12px; color: var(--text-2); }
  .b-leave { background: #efe9fb; color: #5b3fa8; }

  /* Auth pages (Keycloak theme): login, set password */
  .wrap { min-height: calc(100vh - 31px); display: grid; place-items: center; padding: 32px; }
  .auth { width: 420px; background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 36px 36px 28px; box-shadow: var(--shadow); }
  .auth .brand { margin-bottom: 28px; }
  .auth .brand-mark { width: 36px; height: 36px; border-radius: 8px; font-size: 16px; }
  .auth .brand b { display: block; font-size: 17px; } .auth .brand span { font-size: 13px; color: var(--text-3); font-weight: 400; }
  .auth h1 { font-size: 20px; margin-bottom: 4px; }
  .pw-wrap { position: relative; }
  .pw-toggle { position: absolute; right: 8px; top: 7px; background: none; border: 0; color: var(--primary); font-size: 12px; padding: 2px 4px; }
"""

JS = r"""/* PMS mockup shared behaviour: role switcher, user menu, toast. Mockup-only. */
const USERS = {
  employee: { name: 'Anita Sharma', initials: 'AS', meta: 'Employee · EMP0007', pending: 0 },
  manager:  { name: 'Rahul Mehta',  initials: 'RM', meta: 'Manager · EMP0002', pending: 9 },
  admin:    { name: 'Priya Nair',   initials: 'PN', meta: 'Administrator · system account',   pending: 1 }
};
let ROLE = 'employee';
function applyRole(role) {
  ROLE = role;
  document.querySelectorAll('[data-roles]').forEach(el => {
    el.style.display = el.dataset.roles.split(' ').includes(role) ? '' : 'none';
  });
  const u = USERS[role];
  document.getElementById('userName').textContent = u.name;
  document.getElementById('avatar').textContent = u.initials;
  document.getElementById('userRole').textContent = u.meta;
  const p = document.getElementById('pending');
  if (p) { p.textContent = u.pending; p.style.display = u.pending ? '' : 'none'; }
  const e = document.getElementById('empLink'); if (e) e.firstChild.textContent = role === 'manager' ? 'My Team' : 'Employees';
  if (typeof onRole === 'function') onRole(role);
}
document.querySelectorAll('input[name=role]').forEach(r => r.addEventListener('change', e => applyRole(e.target.value)));
const ub = document.getElementById('userBtn'), um = document.getElementById('userMenu');
if (ub) {
  ub.addEventListener('click', () => { const o = um.classList.toggle('open'); ub.setAttribute('aria-expanded', o); });
  document.addEventListener('click', e => { if (!ub.contains(e.target)) { um.classList.remove('open'); ub.setAttribute('aria-expanded', false); } });
}
function toast(msg) { const t = document.getElementById('toast'); t.textContent = msg; t.classList.add('show'); clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove('show'), 2600); }

"""

NAV = [
    ("home", "scr-sh-03-dashboard.html", "Home", "employee manager admin"),
    ("approvals", "scr-sh-04-approvals.html", 'Approvals <span class="count" id="pending">0</span>', "manager admin"),
    ("label", None, "My work", "employee manager"),
    ("profile", "scr-eims-03-my-profile.html", "My Profile", "employee manager"),
    ("attendance", "scr-ams-01-my-attendance.html", "Attendance", "employee manager"),
    ("leave", "scr-lms-01-my-leave.html", "Leave", "employee manager"),
    ("salary", "scr-sms-01-my-salary.html", "Salary", "employee manager"),
    ("label", None, "People", "manager admin"),
    ("employees", "scr-eims-01-directory.html", "Employees", "manager admin"),
]


def mock_bar(screen_id, title, roles=("employee", "manager", "admin"), default="employee", extra=""):
    radios = "".join(
        f'<label><input type="radio" name="role" value="{r}"{" checked" if r == default else ""}> {r.capitalize()}</label>'
        for r in roles)
    view = f"View as: {radios}" if roles else ""
    return (f'<div class="mock-bar" role="region" aria-label="Mockup controls"><strong>Mockup controls</strong>'
            f'{view}{extra}<span class="mock-id">{screen_id} · {title} · v0.1</span></div>')


def shell(screen_id, title, active, crumbs, head, body, script="", roles=("employee", "manager", "admin"),
          default="employee", extra_controls="", modal=""):
    nav = []
    for key, href, label, r in NAV:
        if key == "label":
            nav.append(f'<div class="nav-label" data-roles="{r}">{label}</div>')
        else:
            idattr = ' id="empLink"' if key == "employees" else ""
            cls = ' class="active"' if key == active else ""
            nav.append(f'<a href="{href}"{cls}{idattr} data-roles="{r}">{label}</a>')
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{screen_id} · {title} · PMS mockup</title>
<link rel="stylesheet" href="assets/pms-mockup.css">
</head>
<body>
{mock_bar(screen_id, title, roles, default, extra_controls)}
<div class="app">
  <header class="header">
    <div class="brand"><div class="brand-mark" aria-hidden="true">P</div>PMS <small>Payroll Management System</small></div>
    <div class="user">
      <button class="user-btn" id="userBtn" aria-haspopup="menu" aria-expanded="false">
        <div class="avatar" id="avatar">AS</div>
        <div class="user-meta"><b id="userName">Anita Sharma</b><span id="userRole">Employee · EMP0007</span></div>
        <span aria-hidden="true">▾</span>
      </button>
      <div class="menu-pop" id="userMenu" role="menu">
        <a href="scr-sh-02-set-password.html" role="menuitem">Change password</a><hr>
        <a href="scr-sh-01-login.html" role="menuitem">Log out</a>
      </div>
    </div>
  </header>
  <nav class="side" aria-label="Main menu"><div class="nav">{''.join(nav)}</div></nav>
  <main class="main">
    <div class="crumbs">{crumbs}</div>
    <div class="page-head">{head}</div>
{body}
    <div class="footer">PMS POC · v0.1</div>
  </main>
</div>
{modal}
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="assets/pms-mockup.js"></script>
<script>
{script}
applyRole('{default}');
</script>
</body>
</html>
"""


def standalone(screen_id, title, body, script="", extra_controls=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{screen_id} · {title} · PMS mockup</title>
<link rel="stylesheet" href="assets/pms-mockup.css">
</head>
<body>
{mock_bar(screen_id, title, roles=(), extra=extra_controls)}
{body}
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="assets/pms-mockup.js"></script>
<script>
{script}
</script>
</body>
</html>
"""
