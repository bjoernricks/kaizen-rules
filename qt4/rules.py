import os.path
import kaizen.rules

from kaizen.system import Command, Make, Copy, Quilt, Mkdirs, Move, Delete

class Qt4(kaizen.rules.ConfigureRules):

    url = "http://releases.qt-project.org/qt4/source/qt-everywhere-opensource-src-%(version)s.tar.gz"

    hash = { "md5" : "3c1146ddf56247e16782f96910a8423b",
             "sha1" : "e1e2edef1d63ed677d6534d32800c2e1f7ad0e73" }
    version = "4.8.2"
    name = "qt4"

    patch_cmd = Quilt

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

    configure_cc = "gcc"
    configure_cxx = "g++"
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
                      "-no-framework",
                      "-cocoa",
                      "-prefix %(prefix)s",
                      "-L/usr/X11/lib",
                      "-I/usr/X11/include",
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
        Copy(os.path.join(self.src_path, "src", "gui", "mac", "qt_menu.nib"),
             os.path.join(self.dest_path, "lib", "Resources")).run()
        Mkdirs(self.apps_dir).run()
        Move(self.dest_path + "/bin/*.app",
             self.destroot_path + self.apps_dir).run()

    def distclean(self):
        Delete(self.build_path).run()
