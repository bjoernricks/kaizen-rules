import jam.session

class Gdkpixbuf(jam.session.ConfigureSession):

    url = "http://ftp.gnome.org/pub/gnome/sources/gdk-pixbuf/2.24/gdk-pixbuf-%(version)s.tar.bz2"
    hash = { "md5" : "d8ece3a4ade4a91c768328620e473ab8",
             "sha1" : "98416b2de3af0dbccc893eb2ada251ef5e60b89b" }
    version = "2.24.0"
    name = "gdk-pixbuf"

    depends = ["glib2", "libpng", "gettext", "libtiff"]

    configure_ldflags = ["-L%(prefix)s/lib"]

