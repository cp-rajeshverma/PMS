"""Builds PMS HTML mockups from the page modules.
Usage (from this folder): python build.py shell_pages eims_pages [...]
Output: ../mockups/<screen>.html and ../mockups/assets/pms-mockup.{css,js}
"""
import sys, importlib, pathlib
from base import CSS, JS
out = pathlib.Path(__file__).resolve().parent.parent / 'mockups'
(out / 'assets').mkdir(parents=True, exist_ok=True)
(out / 'assets' / 'pms-mockup.css').write_text('/* PMS mockup styles (approved style, D-27). Shared by all mockups. */\n' + CSS.strip('\n') + '\n', encoding='utf-8')
(out / 'assets' / 'pms-mockup.js').write_text(JS.strip('\n') + '\n', encoding='utf-8')
for mod in sys.argv[1:]:
    m = importlib.import_module(mod)
    for name, fn in m.PAGES.items():
        (out / name).write_text(fn().replace('₹ ', '₹ '), encoding='utf-8')
        print('built', name)
