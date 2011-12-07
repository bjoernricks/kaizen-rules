import os.path

import jam.session

from jam.system import Command

class Sharedmimeinfo(jam.session.ConfigureSession):

    url = "http://freedesktop.org/~hadess/shared-mime-info-%(version)s.tar.bz2"
    hash = { "md5" : "967d68d3890ba3994cfce3adf5b8f15b",
             "sha1" : "c279d0556acddcfaf9ba7d04bbcae4147d131ede" }
    version = "0.90"
    name = "shared-mime-info"

    depends = ["pkg-config", "glib2", "libxml2", "gettext", "intltool"]

    configure_args = ["--disable-update-mimedb"]

    def post_activate(self):
        Command("update-mime-database", ["-V " + os.path.join(self.prefix,
                                                              "share", "mime")],
                os.path.join(self.prefix, "bin")).run()
