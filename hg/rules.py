import os.path

from jam.session import MakeSession
from jam.system import Make, Copy

class Hg(MakeSession):

    url = "http://mercurial.selenic.com/release/mercurial-1.8.3.tar.gz"
    hash = { "md5" : "7afea936dfdb21220064cac6402f8743" }
    version = "1.8.3"
    depends = ["python-docutils"]

    src_path = "%(src_dir)s/mercurial-%(version)s"

    def configure(self):
        Copy(self.src_path, self.build_path).run()

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
        Copy(os.path.join(self.build_path, "contrib", "hgk"),
             os.path.join(self.destroot_path + self.prefix, "bin",
                          "hgk")).run()

    def distclean(self):
        # TODO remove destroot and copy source to build
        self.clean()
