import os.path

import kaizen.rules
from kaizen.system import Delete

class Diffutils(kaizen.rules.ConfigureRules):

    url = "ftp://ftp.gnu.org/gnu/diffutils/diffutils-%(version)s.tar.xz"
    hash = { "md5" : "26ff64c332429c830c154be46b393382",
             "sha1" : "59b9742e96e2512d4d6f9af7964d71b6ea5a9ef0" }
    version = "3.2"
    name = "diffutils"

    def post_destroot(self):
        Delete(os.path.join(self.dest_dir + self.prefix, "share", "info",
            "dir")).run()
