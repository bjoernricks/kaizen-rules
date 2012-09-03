import os.path

from kaizen.rules import MakeRules
from kaizen.system import Make, Copy, Delete

class Hg(MakeRules):

    url = "http://mercurial.selenic.com/release/mercurial-%(version)s.tar.gz"
    hash = { "md5" : "22a46a3ae64a5d625f068e588b4d6ec2",
             "sha1" : "59e42fd0aebabe8ec9bd59ca6a41416032f7ca48" }
    version = "2.3.1"
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
