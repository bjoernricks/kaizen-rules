import os.path
import kaizen.rules

from kaizen.system import Move

class Dbus(kaizen.rules.ConfigureRules):

    url = "http://dbus.freedesktop.org/releases/dbus/dbus-%(version)s.tar.gz"
    hash = { "md5" : "5ec43dc4554cba638917317b2b4f7640",
             "sha1" : "17e619f008301592b7f01a60e7cf18e2752b5270" }
    version = "1.6.4"
    name = "dbus"

    configure_args = ["--without-x", "--enable-launchd"]

    def post_destroot(self):
        path = "Library"
        Move(os.path.join(self.dest_dir, path), os.path.join(self.dest_dir +
            self.prefix, path)).run()
