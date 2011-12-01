import os.path
import jam.session

from jam.system import Move

class Dbus(jam.session.ConfigureSession):

    url = "http://dbus.freedesktop.org/releases/dbus/dbus-%(version)s.tar.gz"
    hash = { "md5" : "44a2a10678e7e50460879c3eb4453a65",
             "sha1" : "d6e6538cfc1ed71992f6786a6da55d815d995b5b" }
    version = "1.4.16"
    name = "dbus"

    configure_args = ["--without-x", "--enable-launchd"]

    def post_destroot(self):
        path = "Library"
        Move(os.path.join(self.dest_dir, path), os.path.join(self.dest_dir +
            self.prefix, path)).run()
