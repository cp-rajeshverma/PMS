"""Builds PMS HTML mockups from the page modules.
Usage (from this folder): python build.py shell_pages [eims_pages ...]
Output: ../mockups/<screen>.html
"""
import sys, importlib, pathlib
out = pathlib.Path(__file__).resolve().parent.parent / 'mockups'
out.mkdir(exist_ok=True)
for mod in sys.argv[1:]:
    m = importlib.import_module(mod)
    for name, fn in m.PAGES.items():
        (out / name).write_text(fn().replace('₹ ', '₹ '), encoding='utf-8')
        print('built', name)
