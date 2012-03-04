import os.path
import jam.session

from jam.system import Copy

class Gitmanpages(jam.session.Session):

    url = "http://git-core.googlecode.com/files/git-manpages-%(version)s.tar.gz"
    hash = { "md5" : "dfe782bd962ad66a7865c0db27d48362",
             "sha1" : "93315f7f51d7f27d3e421c9b0d64afa27f3d16df" }
    version = "1.7.8"
    name = "git-manpages"

    def destroot(self):
        Copy(os.path.join(self.src_dir, "man*"),
             os.path.join(self.dest_path, "share", "man")).run()
