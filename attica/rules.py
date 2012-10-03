import kaizen.rules

from kaizen.system.patch import Quilt

class Attica(kaizen.rules.CMakeRules):

    url = "ftp://ftp.kde.org/pub/kde/stable/attica/attica-%(version)s.tar.bz2"
    hash = { "md5" : "b90983ec5d79e5ddcbc9146fa23cab72",
            "sha1" : "f4962636ec9282c32c4ceaec0c85f92ca5102b60" }
    version = "0.4.1"
    name = "attica"

    depends = ["qt4"]

    patch_cmd = Quilt

    patches = ["patch-lib-CMakeLists.txt.diff"]

    configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
