import os
import re
import pathlib
import distutils
from setuptools import setup, find_packages
from miyadaiku.common import setuputils

DIR = pathlib.Path(__file__).resolve().parent
os.chdir(DIR)

requires = [
    "miyadaiku"
]

srcdir = 'node_modules/popper.js/dist/umd/'
destdir = 'miyadaiku/themes/popper_js/externals/'
copy_files = [[srcdir, ['popper*.js'], destdir]]

versionpy = DIR / 'miyadaiku/themes/popper_js/__version__.py'
version = re.search(r'"([\d.]+)"', versionpy.read_text())[1]


setup(
    name="miyadaiku.themes.popper_js",
    version=version,
    author="Atsuo Ishimoto",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description='Popper.js files for miyadaiku static site generator',
    long_description=setuputils.read_file(DIR, 'README.rst'),
    url='https://github.com/miyadaiku/miyadaiku-themes-popper_js',
    project_urls={
        'Miyadaiku': 'https://miyadaiku.github.io/',
    },

    packages=list(setuputils.list_packages(DIR, 'miyadaiku')),
    package_data={
        '': setuputils.SETUP_FILE_EXTS,
    },
    install_requires=requires,
    include_package_data=True,
    zip_safe=False,
    cmdclass={'copy_files': setuputils.copy_files},
    copy_files=copy_files
)
