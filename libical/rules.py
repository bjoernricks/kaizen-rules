import kaizen.rules

from kaizen.system import Quilt

class Libical(kaizen.rules.CMakeRules):

    url = "http://downloads.sourceforge.net/project/freeassociation/libical/libical-%(version)s/libical-%(version)s.tar.gz"
    hash = { "md5" : "e549f434d5fbf9cd156c60ed4943618f",
             "sha1" : "4693cd0438be9f3727146ac1a46aa5b1b93b8c86" }
    version = "0.48"
    name = "libical"

    patch_cmd = Quilt

    parallel = False
