#!/usr/bin/env python3

import pathlib
from miyadaiku import setuputils

DIR = pathlib.Path(__file__).resolve().parent

srcdir = DIR / 'node_modules/popper.js/dist/umd/'
destdir = DIR / 'miyadaiku_theme_popper_js/externals/'
copy_files = [[srcdir, ['popper*.js'], destdir]]

setuputils.copyfiles(copy_files)
