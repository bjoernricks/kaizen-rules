import jam.session

from jam.system import Copy, Make

class Getopt(jam.session.Session):

    url = "http://software.frodo.looijaard.name/getopt/files/getopt-%(version)s.tar.gz"
    hash = { "md5" : "02188ca68da27c4175d6e9f3da732101",
             "sha1" : "8b9b329b3a8f5d52c91c0381616ecbd1ba291486" }
    version = "1.1.4"
    name = "getopt"

    depends = ["gettext"]
    patches = ["patch-Makefile.diff"]

    def configure(self):
        Copy(self.src_path, self.build_path).run()

    def build(self):
        Make(self.build_path, self.debug).run(
                ["prefix=" + self.prefix,
                 "DESTDIR=" + self.dest_dir,
                 "LIBCGETOPT=0",
                 "WITH_GETTEXT=1",
                 "LDFLAGS=-L" + self.prefix + "/lib -lintl",
                 ])

    def destroot(self):
        Make(self.build_path, self.debug).run(
                ["prefix=" + self.prefix,
                 "DESTDIR=" + self.dest_dir,
                 "LIBCGETOPT=0",
                 "WITH_GETTEXT=1",
                 "LDFLAGS=-L" + self.prefix + "/lib -lintl",
                 "install",
                 ])
