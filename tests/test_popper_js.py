import pytest
import pathlib

import miyadaiku.core
import miyadaiku.core.site  # install pyyaml converter

#miyadaiku.core.SHOW_TRACEBACK = True
#miyadaiku.core.DEBUG = True

from miyadaiku.core.site import Site

@pytest.fixture
def sitedir(tmpdir):
    d = tmpdir.mkdir('site')
    d.mkdir('contents')
    d.mkdir('templates')
    return pathlib.Path(str(d))

def test_install(sitedir):
    (sitedir / 'config.yml').write_text('''
themes:
    - miyadaiku.themes.popper_js

''')

    (sitedir /'contents/index.rst').write_text('''

test
---------------

abc 

.. jinja::

   {{ popper_js.load_js(page) }}
''')

    site = Site(sitedir)
    site.build()

    ret = (sitedir / 'outputs/index.html').read_text()
    assert '<script src="static/popper.js/popper.min.js">' in ret

    assert (sitedir / 'outputs/static/popper.js/popper.min.js').exists()
