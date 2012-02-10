import jam.session
import jam.run

from jam.system import Replace, Copy, Command, Delete

class Glib(jam.session.ConfigureSession):

    url = "ftp://ftp.gnome.org/pub/gnome/sources/glib/2.30/glib-2.30.2.tar.bz2"
    hash = { "md5" : "b40f3889e8d24e1b367763673ca6deb5",
             "sha1" : "70208757905037fa1f8b89797db0097c5e82a140" }
    version = "2.30.2"
    name = "glib"

    configure_args = ["--disable-dtrace", "--with-libiconv=native"]
    configure_path = "%(build_path)s"
    configure_cflags = ["-I%(prefix)s/include"]
    configure_ldflags = ["-L%(prefix)s/lib"]

    patches = ["patch-configure.diff",
               "patch-glib-2.0.pc.in.diff",
               "patch-glib_gunicollate.c.diff",
               "patch-gi18n.h.diff",
               "patch-gio_xdgmime_xdgmime.c.diff",
               "patch-gio_gdbusprivate.c.diff",
               "patch-gconvert.c.diff",
               ]

    depends = ["gettext", "libiconv", "zlib", "libffi"]


    def pre_configure(self):
        Copy(self.src_path, self.build_path).run()
        for f in ["/gio/xdgmime/xdgmime.c", "/gio/gdbusprivate.c"]:
            Replace("@@PREFIX@@", self.prefix, self.build_path + f).run()

    def post_configure(self):
        cmd = ["ed", "-", self.build_path + "/config.h"]
        self.log.debug("Running ed on %s" % self.buld_path + "/config.h")
        jam.run.call(cmd, not self.verbose, cwd=self.build_path, 
                     inputdata=self.session_path + "/config.h.ed")

    def distclean(self):
        Delete(self.build_path).run()
