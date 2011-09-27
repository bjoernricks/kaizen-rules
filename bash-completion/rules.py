import os.path

import jam.session
from jam.system import Replace

class BashCompletion(jam.session.ConfigureSession):

    url = "http://bash-completion.alioth.debian.org/files/bash-completion-1.3.tar.bz2"
    hash = { "md5" : "a1262659b4bbf44dc9e59d034de505ec",
             "sha1" : "6a46b93f44c56cc336632ab28d90c0595fbcc98f" }
    version = "1.3"
    name = "bash-completion"

    # uncomment to add additonal patches 
    # all patches will be copied to %(downloadroot)s/%(session)s/patches
    # e.g. patches = ["01-patch.diff", "http://url.com/remotepatch.diff"]
    # patches = [""]

    def post_destroot(self):
        Replace("/etc/bash_completion", self.prefix + "/etc/bash_completion",
                os.path.join(self.destroot_path + self.prefix,
                             "etc", "bash_completion")).run()
