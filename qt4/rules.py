import os.path
import jam.session

from jam.system import Command, Make

class Qt4(jam.session.ConfigureSession):

    url = "http://get.qt.nokia.com/qt/source/qt-everywhere-opensource-src-%(version)s.tar.gz"
    hash = { "md5" : "9831cf1dfa8d0689a06c2c54c5c65aaf",
             "sha1" : "af9016aa924a577f7b06ffd28c9773b56d74c939" }
    version = "4.7.4"
    name = "qt4"

    src_path = "%(src_dir)s/qt-everywhere-opensource-src-%(version)s"

    depends = ["dbus",
               "sqlite3",
               "libpng",
               #"libjpeg",
               "openssl",
               "pkg-config",
               "zlib"]

    configure_args = ["-opensource",
                      "-confirm-license",
                      "-no-sql-db2",
                      "-no-sql-ibase",
                      "-no-sql-oci",
                      "-no-sql-tds",
                      "-no-phonon",
                      "-no-phonon-backend",
                      "-no-framework",
                      "-dbus-linked",
                      "-fast",
                      "-prefix %(prefix)s",
                      "-L%(prefix)s/lib",
                      "-I%(prefix)s/include",
                      "-L/usr/X11/lib",
                      "-I/usr/X11/include",
                      "-system-libpng",
                      #"-system-libjpeg",
                      "-system-zlib",
                      "-system-sqlite",
                      ]

    def configure(self):
        if self.config.get("verbose"):
            self.configure_args.append("-v")
        cmd = os.path.join(self.src_path, "configure")
        Command(cmd, self.configure_args, self.build_path, self.debug).run()

    def destroot(self):
        args = ["INSTALL_ROOT=" + self.dest_dir, "install"]
        Make(self.build_path, self.debug).run(args)
