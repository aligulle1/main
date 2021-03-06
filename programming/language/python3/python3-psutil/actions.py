#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

def build():
    # suppress compiler warnings
    pisitools.cflags.add("-Wno-stringop-truncation")
    # fix unused direct dependency analysis
    shelltools.export("LDSHARED", "x86_64-pc-linux-gnu-gcc -Wl,-O1,--as-needed -shared -L/var/pisi/python3-3.8.1-8/work/temp/lib -lbz2 -lpthread -ldl")
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
