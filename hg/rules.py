import os.path
import sys

from kaizen.rules import MakeRules
from kaizen.system import Make, Copy, Delete

class Hg(MakeRules):

    url = "http://mercurial.selenic.com/release/mercurial-%(version)s.tar.gz"
    hash = { "md5" : "450ed0c8c10e66c3cbca1d82fcb36a29",
             "sha1" : "21800a6355fadd67ddb85205f8dd887798502da6" }
    version = "2.5"
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
        Copy(os.path.join(self.build_path, "hgeditor"),
             os.path.join(self.destroot_path + self.prefix, "bin",
                          "hgeditor")).run()
        # Delete locales
        Delete(os.path.join(self.destroot_path + self.prefix, "lib",
                            "python%s.%s" % (sys.version_info[0],
                                             sys.version_info[1]),
                            "site-packages", "mercurial", "locale")).run()

    def distclean(self):
        Delete(self.build_path).run()
