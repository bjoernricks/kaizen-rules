from jam.session import MakeSession
from jam.command import Make, Copy

class Hg(MakeSession):

    url = "http://mercurial.selenic.com/release/mercurial-1.8.3.tar.gz"
    hash = { "md5" : "7afea936dfdb21220064cac6402f8743" }
    version = "1.8.3"
    name = "hg"
    depends = ["python-docutils"]

    src_path = "%(src_dir)s/mercurial-%(version)s"


    def configure(self):
        Copy(self.src_path, self.build_path).run()

    def build(self):
        Make(self.build_path, self.debug).run(["all"])

    def destroot(self):
        Make(self.build_path, self.debug).run(
                ["PREFIX=" + self.config.get("prefix"),
                 "DESTDIR=" + self.dest_dir,
                 "install"])
