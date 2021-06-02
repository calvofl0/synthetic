#!/bin/env python
# -*- coding: utf-8 -*-

# Loads a python module from remote file
# Inspired from: https://stackoverflow.com/questions/18747043/import-python-module-over-the-internet-multiple-protocols-or-dynamically-create

from os.path import basename, splitext
from urllib.request import urlopen
from imp import new_module

def rimport(url, obj=None, modname=None):
    if modname is None:
        modname = splitext(basename(url))[0]
    mod = urlopen(url).read()
    codeobj = compile(mod, basename(url), 'exec')
    newmod = new_module(modname)
    exec(codeobj,newmod.__dict__)
    if obj is None:
        return newmod
    else:
        return newmod.__dict__[obj]
