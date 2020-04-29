import pathlib
from setuptools import setup, find_packages
from miyadaiku import setuputils

DIR = pathlib.Path(__file__).resolve().parent

srcdir = DIR / 'node_modules/popper.js/dist/umd/'
destdir = DIR / 'miyadaiku_theme_popper_js/externals/'
copy_files = [[srcdir, ['popper*.js'], destdir]]

setup(
    cmdclass={'copy_files': setuputils.copy_files},
    copy_files=copy_files
)
