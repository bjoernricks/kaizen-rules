import os.path
import jam.session

from jam.system import Command, Make, Copy

class QtCreator(jam.session.MakeSession):

    url = "http://get.qt.nokia.com/qtcreator/qt-creator-%(version)s-src.tar.gz"
    hash = { "md5" : "8aa296ed9034f847bd53ee0424e5ef08",
             "sha1" : "620fe944994fffe0812a1474deff78e07b34025b" }
    version = "2.3.1"
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
             os.path.join(self.dest_dir + self.apps_dir, "Qt Creator.app")).run()
