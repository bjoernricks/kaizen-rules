import kaizen.rules

from kaizen.system.patch import Quilt

class Giflib(kaizen.rules.ConfigureRules):

    url = "http://downloads.sourceforge.net/project/giflib/giflib-4.x/giflib-%(version)s.tar.bz2"
    hash = { "md5" : "711ad48551ee14db7c200b5f402df849",
             "sha1" : "bc942711f75de7d8539f79be34d69c0d53c381c1" }
    version = "4.2.0"
    name = "giflib"

    patch_cmd = Quilt

    configure_args = ["--disable-x11"]
