import os.path

import kaizen.rules
from kaizen.system import Replace

class BashCompletion(kaizen.rules.ConfigureRules):

    url = "http://bash-completion.alioth.debian.org/files/bash-completion-%(version)s.tar.bz2"
    hash = { "md5" : "a1262659b4bbf44dc9e59d034de505ec",
             "sha1" : "6a46b93f44c56cc336632ab28d90c0595fbcc98f" }
    version = "1.3"
    name = "bash-completion"

    def post_destroot(self):
        Replace("/etc/bash_completion", self.prefix + "/etc/bash_completion",
                os.path.join(self.destroot_path + self.prefix,
                             "etc", "bash_completion")).run()
