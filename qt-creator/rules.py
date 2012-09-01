import os.path
import kaizen.rules

from kaizen.system import Command, Make, Copy

class QtCreator(kaizen.rules.MakeRules):

    url = "http://get.qt.nokia.com/qtcreator/qt-creator-%(version)s-src.tar.gz"
    hash = { "md5" : "80c1a2be4c685ce147c42424ad977e1a",
             "sha1" : "12934e34fdda3f493812e671f8db1fb789578e91" }
    version = "2.4.0"
    name = "qt-creator"

    src_path = "%(src_dir)s/%(name)s-%(version)s-src"

    depends = ["qt4"]

    def configure(self):
        Command("qmake", [os.path.join(self.src_path, "qtcreator.pro")],
                self.build_path, self.debug).run()

    def destroot(self):
        args = ["INSTALL_ROOT=" + self.dest_dir + self.prefix, "install"]
        Make(self.build_path, self.debug).run(args)

    def post_destroot(self):
        Copy(os.path.join(self.build_path, "bin", "Qt Creator.app"),
             os.path.join(self.dest_dir + self.apps_dir)).run()

    def distclean(self):
        # FIXME
        pass
