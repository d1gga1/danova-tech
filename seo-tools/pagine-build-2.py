# -*- coding: utf-8 -*-
"""Genera SOLO le pagine di un file dati (default pagine-dati-2.py), con il
   motore di pagine-build.py.
   Uso:  python3 seo-tools/pagine-build-2.py [pagine-dati-3.py]"""
import os, sys, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, fn):
    s = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
pb = load('pb', 'pagine-build.py')
pb.pd = load('pd2', sys.argv[1] if len(sys.argv) > 1 else 'pagine-dati-2.py')
for d in pb.pd.PAGINE:
    p = pb.build(d)
    print('%-3s  %-44s  %6d byte' % (d['lang'], d['url'], len(open(os.path.join(pb.ROOT,p),encoding='utf-8').read())))
