import os.path
import jam.session

from jam.system import Command, Make, Copy, Quilt, Mkdirs, Move

class Qt4(jam.session.ConfigureSession):

    url = "http://get.qt.nokia.com/qt/source/qt-everywhere-opensource-src-%(version)s.tar.gz"
    hash = { "md5" : "7960ba8e18ca31f0c6e4895a312f92ff",
             "sha1" : "a074d0f605f009e23c63e0a4cb9b71c978146ffc" }
    version = "4.8.1"
    name = "qt4"

    patchsystem = Quilt

    src_path = "%(src_dir)s/qt-everywhere-opensource-src-%(version)s"

    depends = ["dbus",
               "sqlite3",
               "mysql",
               "libpng",
               "libjpeg",
               "libtiff",
               "openssl",
               "pkg-config",
               "zlib"]

    configure_cpath = ["%(prefix)s/include"]
    configure_library_path = ["%(prefix)s/lib"]
    build_cpath = configure_cpath
    build_library_path = configure_library_path

    configure_args = ["-opensource",
                      "-confirm-license",
                      "-no-sql-db2",
                      "-no-sql-ibase",
                      "-no-sql-oci",
                      "-no-sql-tds",
                      "-no-phonon",
                      "-no-phonon-backend",
                      "-dbus-linked",
                      "-fast",
                      "-optimized-qmake",
                      "-prefix %(prefix)s",
                      "-system-libpng",
                      "-system-zlib",
                      "-system-sqlite",
                      "-plugin-sql-mysql",
                      "-demosdir %(prefix)s/share/%(name)s/demos",
                      "-examplesdir %(prefix)s/share/%(name)s/examples",
                      "-translationdir %(prefix)s/share/%(name)s/translations",
                      "-docdir %(prefix)s/share/%(name)s/doc",
                      "-plugindir %(prefix)s/lib/%(name)s/plugins",
                      "-importdir %(prefix)s/lib/%(name)s/imports",
                      "-datadir %(prefix)s/share/%(name)s",
                      "-sysconfdir %(prefix)s/etc/xdg",
                      ]


    def configure(self):
        if self.config.get("verbose"):
            self.configure_args.append("-v")
        cmd_str = os.path.join(self.src_path, "configure")
        cmd = Command(cmd_str, self.configure_args, self.build_path, self.debug)
        cmd.set_env("CPATH", ":".join(self.configure_cpath))
        cmd.set_env("LIBRARY_PATH", ":".join(self.configure_library_path))
        cmd.run()


    def destroot(self):
        args = ["INSTALL_ROOT=" + self.dest_dir, "install"]
        make = Make(self.build_path, self.debug).run(args)
