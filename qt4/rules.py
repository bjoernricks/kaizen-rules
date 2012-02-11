import os.path
import jam.session

from jam.system import Command, Make, Copy

class Qt4(jam.session.ConfigureSession):

    url = "http://get.qt.nokia.com/qt/source/qt-everywhere-opensource-src-%(version)s.tar.gz"
    hash = { "md5" : "e8a5fdbeba2927c948d9f477a6abe904",
             "sha1" : "2ba35adca8fb9c66a58eca61a15b21df6213f22e" }
    version = "4.8.0"
    name = "qt4"

    src_path = "%(src_dir)s/qt-everywhere-opensource-src-%(version)s"

    depends = ["dbus",
               "sqlite3",
               "libpng",
               "libjpeg",
               "libtiff",
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
                      "-dbus-linked",
                      "-fast",
                      "-optimized-qmake",
                      "-no-framework",
                      "-cocoa",
                      "-prefix %(prefix)s",
                      "-L%(prefix)s/lib",
                      "-I%(prefix)s/include",
                      "-L/usr/X11/lib",
                      "-I/usr/X11/include",
                      "-system-libpng",
                      "-system-zlib",
                      "-system-sqlite",
                      "-demosdir %(prefix)s/share/%(name)s/demos",
                      "-examplesdir %(prefix)s/share/%(name)s/examples",
                      "-translationdir %(prefix)s/share/%(name)s/translations",
                      "-docdir %(prefix)s/share/%(name)s/doc",
                      ]

    #TODO move *.app from prefix/bin to apps_dir

    def configure(self):
        if self.config.get("verbose"):
            self.configure_args.append("-v")
        cmd = os.path.join(self.src_path, "configure")
        Command(cmd, self.configure_args, self.build_path, self.debug).run()

    def destroot(self):
        args = ["INSTALL_ROOT=" + self.dest_dir, "install"]
        Make(self.build_path, self.debug).run(args)
        Copy(os.path.join(self.src_path, "src", "gui", "mac", "qt_menu.nib"),
             os.path.join(self.dest_path, "lib", "Resources", "qt_menu.nib")
             ).run()
