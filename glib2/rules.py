import jam.session

class Glib(jam.session.ConfigureSession):

    url = "ftp://ftp.gnome.org/pub/gnome/sources/glib/2.30/glib-2.30.2.tar.bz2"
    hash = { "md5" : "b40f3889e8d24e1b367763673ca6deb5",
             "sha1" : "70208757905037fa1f8b89797db0097c5e82a140" }
    version = "2.30.2"
    name = "glib"

    configure_args = ["--disable-dtrace"]

    patches = ["patch-configure.diff",
               "patch-glib-2.0.pc.in.diff",
               "patch-glib_gunicollate.c.diff",
               "patch-gi18n.h.diff",
               "patch-gio_xdgmime_xdgmime.c.diff",
               "patch-gio_gdbusprivate.c.diff",
               ]

    depends = ["gettext", "libiconv", "zlib", "libffi"]