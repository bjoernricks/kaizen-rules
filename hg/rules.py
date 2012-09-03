import os.path

from kaizen.rules import MakeRules
from kaizen.system import Make, Copy Delete

class Hg(MakeRules):

    url = "http://mercurial.selenic.com/release/mercurial-%(version)s.tar.gz"
    hash = { "md5" : "0ff7c7f7c50e506d494ff84baa10a77d",
             "sha1" : "40961a436920628ff9db48dc8aab8012d72dcd52" }
    version = "2.2.1"
    depends = ["python-docutils"]
    name = "hg"

    src_path = "%(src_dir)s/mercurial-%(version)s"

    def configure(self):
        Copy(self.src_path + "/*", self.build_path).run()

    def build(self):
        Make(self.build_path, self.debug).run(["all"])

    def destroot(self):
        Make(self.build_path, self.debug).run(
                ["PREFIX=" + self.prefix,
                 "DESTDIR=" + self.dest_dir,
                 "install"])
        Copy(os.path.join(self.build_path, "contrib", "bash_completion"),
             os.path.join(self.destroot_path + self.prefix, "etc",
                          "bash_completion.d", "mercurial")).run()
        Copy(os.path.join(self.build_path, "contrib"),
             os.path.join(self.destroot_path + self.prefix, "share",
                          "mercurial", "contrib")).run()
        Copy(os.path.join(self.build_path, "contrib", "hgk"),
             os.path.join(self.destroot_path + self.prefix, "bin",
                          "hgk")).run()

    def distclean(self):
        Delete(self.build_path).run()
