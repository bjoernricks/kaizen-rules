import os.path

import jam.session
from jam.system import Delete

class Diffutils(jam.session.ConfigureSession):

    url = "http://ftp.gnu.org/gnu/diffutils/diffutils-3.0.tar.gz"
    hash = { "md5" : "684aaba1baab743a2a90e52162ff07da",
             "sha1" : "17fcdcd435ef6b424aa9c7a487ffde408d1a00e6" }
    version = "3.0"
    name = "diffutils"

    def post_destroot(self):
        Delete(os.path.join(self.dest_dir + self.prefix, "share", "info",
            "dir")).run()
