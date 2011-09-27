import os.path
import jam.session

from jam.system import Copy

class Ctags(jam.session.ConfigureSession):

    url = "http://prdownloads.sourceforge.net/ctags/ctags-5.8.tar.gz"
    hash = { "md5" : "c00f82ecdcc357434731913e5b48630d",
             "sha1" : "482da1ecd182ab39bbdc09f2f02c9fba8cd20030" }
    version = "5.8"
    name = "ctags"

    configure_args = ["--enable-macro-patterns"]

    def destroot(self):
        prefix = self.prefix[1:]
        Copy(os.path.join(self.build_path, "ctags"), 
             os.path.join(self.dest_dir, prefix, "bin", "ctags")).run()
        Copy(os.path.join(self.src_path, "ctags.1"),
             os.path.join(self.dest_dir, prefix, "share", "man",
             "man1", "ctags.1")).run()
