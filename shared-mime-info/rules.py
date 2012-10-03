import os.path

import kaizen.rules

from kaizen.system import Command, Replace

class Sharedmimeinfo(kaizen.rules.ConfigureRules):

    url = "http://freedesktop.org/~hadess/shared-mime-info-%(version)s.tar.xz"
    hash = { "md5" : "901b7977dbb2b71d12d30d4d8fb97028",
             "sha1" : "146dbad62f5450116b0353f88bb8e700f0034013" }
    version = "1.0"
    name = "shared-mime-info"

    depends = ["pkg-config", "glib2", "libxml2", "gettext", "intltool", "perl",
               "perl-xml-sax"]

    configure_args = ["--disable-update-mimedb"]
    configure_env = {"ALL_LIBS" : "-L/usr/lib -L%(prefix)s/lib "\
                                  "-lglib-2.0 -lxml2",
                     "ALL_CFLAGS" : "-I/usr/include -I%(prefix)s/include " \
                                    "-I/usr/include/libxml2 " \
                                    "-I%(prefix)s/include/glib-2.0 " \
                                    "-I%(prefix)s/lib/glib-2.0/include"
                    }

    def pre_configure(self):
        Replace('env = "/usr/local/share/"PATH_SEPARATOR"/usr/share/',
                'env = "' + self.prefix +
                '/share"PATH_SEPARATOR"/usr/local/share/"PATH_SEPARATOR"/usr/share/',
                self.src_path + "/update-mime-database.c").run()

    def post_activate(self):
        Command("update-mime-database", ["-V " + os.path.join(self.prefix,
                                                              "share", "mime")],
                os.path.join(self.prefix, "bin"), self.verbose).run()
