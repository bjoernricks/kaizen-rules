import os.path

from jam.session import MakeSession
from jam.system import Command


class Qt4(MakeSession):

    url = "http://get.qt.nokia.com/qt/source/qt-everywhere-opensource-src-4.7.2.tar.gz"
    hash = { "md5" : "66b992f5c21145df08c99d21847f4fdb" }
    version = "4.7.2"
    name = "qt4"

    patches = ["http://qt.nokia.com/files/qt-patches/blacklist-fraudulent-comodo-certificates-patch.diff"]

    src_path = "%(src_dir)s/qt-everywhere-opensource-src-%(version)s"

    depends = ["dbus",
               "sqlite3",
               "libpng",
               "openssl",
               "libjpeg",
               "zlib"]

    args = ["-opensource",
            "-confirm-license",
            "-no-sql-db2",
            "-no-sql-ibase",
            "-no-sql-oci",
            "-no-sql-tds",
            "-no-phonon",
            "-no-phonon-backend",
            "-prefix %(prefix)s",
            "-system-libpng",
            "-system-zlib",
            "-system-sqlite"]

    def configure(self):
        if self.config.get("verbose"):
            self.args.append("-v")
        cmd = os.path.join(self.src_path, "configure")
        Command(cmd, self.args, self.build_path, self.debug).run()
