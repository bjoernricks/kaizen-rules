import os.path
import jam.session

from jam.system import Copy

class Gitmanpages(jam.session.Session):

    url = "http://git-core.googlecode.com/files/git-manpages-%(version)s.tar.gz"
    hash = { "md5" : "5066600fe67986acd36c008c876e9489",
             "sha1" : "5852d1dead0190edeba1803a70fac5d76523a616" }
    version = "1.7.10"
    name = "git-manpages"

    def destroot(self):
        Copy(os.path.join(self.src_dir, "man*"),
             os.path.join(self.dest_path, "share", "man")).run()
