import kaizen.rules

from kaizen.system.patch import Quilt

class Libechonest(kaizen.rules.CMakeRules):

    url = "http://files.lfranchi.com/libechonest-%(version)s.tar.bz2"
    hash = { "md5" : "d6dd16dd6ee28d279b4ec9fa64f67af3",
             "sha1" : "5dd98ffb370e0e199e37ece4a1775a05594f3dcb" }
    version = "2.0.1"
    name = "libechonest"

    patch_system = Quilt

    depends = ["qt4", "qjson"]
