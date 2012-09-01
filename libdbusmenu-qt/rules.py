import kaizen.rules

from kaizen.system import Quilt

class Libdbusmenuqt(kaizen.rules.CMakeRules):

    url = "http://launchpad.net/libdbusmenu-qt/trunk/%(version)s/+download/libdbusmenu-qt-%(version)s.tar.bz2"
    hash = { "md5" : "cc6b7b551377e2a07f6fa5afef0d29ff",
             "sha1" : "690a885825d45579607f3d6708aad84b6f3ecdd0" }
    version = "0.9.0"
    name = "libdbusmenu-qt"

    depends = ["qt4"]

    patchsystem = Quilt

    configure_args = ["-DWITH_DOC=OFF"]
