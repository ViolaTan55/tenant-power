#!d:\0-msrp22\networkcode\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyArango==2.0.1','console_scripts','sample'
__requires__ = 'pyArango==2.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pyArango==2.0.1', 'console_scripts', 'sample')()
    )
