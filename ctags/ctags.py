import os.path
import jam.session

from jam.system import Copy

class Ctags(jam.session.ConfigureSession):

    url = "http://prdownloads.sourceforge.net/ctags/ctags-5.8.tar.gz"
    hash = { "md5" : "c00f82ecdcc357434731913e5b48630d",
             "sha1" : "482da1ecd182ab39bbdc09f2f02c9fba8cd20030" }
    version = "5.8"
    name = "ctags"

    # uncomment to set path to source directory
    # default is %(src_dir)s/%(name)s-%(version)s
    # src_path = ""

    # uncomment to set path to build directory (normally not necessary)
    # build_path = ""

    # uncomment to pass additonal parameters to configure script
    args = ["--enable-macro-patterns"]

    # uncomment to add additonal patches 
    # all patches will be copied to %(downloadroot)s/%(session)s/patches
    # e.g. patches = ["01-patch.diff", "http://url.com/remotepatch.diff"]
    # patches = [""]

    # uncomment to add a dependency on an other session
    # depends = [""]

    def destroot(self):
        prefix = self.prefix[1:]
        Copy(os.path.join(self.build_path, "ctags"), 
             os.path.join(self.dest_dir, prefix, "bin", "ctags")).run()
        Copy(os.path.join(self.src_path, "ctags.1"),
             os.path.join(self.dest_dir, prefix, "share", "man",
             "man1", "ctags.1")).run()
