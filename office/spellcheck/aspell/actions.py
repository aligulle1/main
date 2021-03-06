#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    #shelltools.system("sed -i '/ top.do_check ==/s/top.do_check/*&/' modules/filter/tex.cpp")
    #shelltools.system("sed -i '/word ==/s/word/*&/' prog/check_funs.cpp")
    
    autotools.autoreconf()
    autotools.configure("--disable-static \
                         --sysconfdir=/etc/aspell \
                         --enable-docdir=/usr/share/doc/%s" % get.srcNAME())

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # install ispell/spell compatibility scripts
    pisitools.insinto("/usr/bin","scripts/ispell","ispell-aspell")
    pisitools.insinto("/usr/bin","scripts/spell", "spell-aspell")

    pisitools.dodoc("README*", "TODO")
