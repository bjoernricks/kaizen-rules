import jam.session

from jam.system import Command, Make, Copy, Mkdirs, Quilt

class Qtscriptgenerator(jam.session.MakeSession):

    url = "http://qtscriptgenerator.googlecode.com/files/qtscriptgenerator-src-%(version)s.tar.gz"
    hash = { "md5" : "9f82b0aa212f7938de37df46cd27165c",
             "sha1" : "4c1078f26b196156e857c17c9d11a66cfea66f00" }
    version = "0.2.0"
    name = "qtscriptgenerator-src"

    build_path = "%(src_path)s"

    patchsystem = Quilt

    def configure(self):
        Mkdirs(self.build_path + "/generator").run()
        Command("qmake", ["-o", "Makefile", self.src_path + \
            "/generator/generator.pro"],
                self.build_path + "/generator", self.debug).run()
        Mkdirs(self.build_path + "/qtbindings").run()
        Command("qmake", ["-o", "Makefile", self.src_path + \
            "/qtbindings/qtbindings.pro"],
                self.build_path + "/qtbindings", self.debug).run()

    def build(self):
        Make(self.build_path + "/generator", self.debug).run()
        Command(self.build_path + "/generator/generator", ["--include-paths=" +\
            self.prefix + "/include"], self.build_path + "/generator/", self.debug).run()
        Make(self.build_path + "/qtbindings", self.debug).run()

    def destroot(self):
        args = ["INSTALL_ROOT=" + self.dest_dir + self.prefix, "install"]
        Make(self.build_path, self.debug).run(args)
