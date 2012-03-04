import jam.session

from jam.system import Move

class Avahi(jam.session.ConfigureSession):

    url = "http://avahi.org/download/avahi-%(version)s.tar.gz"
    hash = { "md5" : "2f22745b8f7368ad5a0a3fddac343f2d",
             "sha1" : "7e05bd78572c9088b03b1207a0ad5aba38490684" }
    version = "0.6.31"
    name = "avahi"

    depends = ["pkg-config", "glib2", "qt4", "gettext", "libexpat", "dbus",
               "perl", "libdaemon", "gdbm"]

    configure_ldflags = ["-L%(prefix)s/lib"]
    configure_cppflags = ["-I%(prefix)s/include"]

    configure_args = ["--with-distro=darwin",
                      "--disable-doxygen-doc",
                      "--disable-monodoc",
                      "--disable-mono",
                      "--disable-pygtk",
                      "--disable-qt3",
                      "--disable-gtk",
                      "--disable-gtk3",
                      "--enable-compat-libdns_sd",
                      "--disable-autoipd",
                      "--with-xml=expat",
                      "--disable-python",
                      "--disable-python-dbus",
                      "--disable-manpages",
                      ]


    def post_destroot(self):
        Move(self.destroot_path + "/Library", self.dest_path).run()
