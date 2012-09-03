import os.path
import kaizen.rules

from kaizen.system import Copy

class Gitmanpages(kaizen.rules.Rules):

    url = "http://git-core.googlecode.com/files/git-manpages-%(version)s.tar.gz"
    hash = { "md5" : "0070ad185cfc29da545abe35ba8862e7",
             "sha1" : "fb572729ca5c60161dc651564a50d4378507e20f" }
    version = "1.7.12"
    name = "git-manpages"

    def destroot(self):
        Copy(os.path.join(self.src_dir, "man*"),
             os.path.join(self.dest_path, "share", "man")).run()
