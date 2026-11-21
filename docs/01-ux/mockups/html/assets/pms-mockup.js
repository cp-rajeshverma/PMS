/* PMS mockup shared behaviour: role switcher, user menu, toast. Mockup-only. */
const USERS = {
  employee: { name: 'Anita Sharma', initials: 'AS', meta: 'Employee · EMP0007', pending: 0 },
  manager:  { name: 'Rahul Mehta',  initials: 'RM', meta: 'Manager · EMP0002', pending: 9 },
  admin:    { name: 'PMS Administrator', initials: 'PA', meta: 'Administrator',   pending: 4 }
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
