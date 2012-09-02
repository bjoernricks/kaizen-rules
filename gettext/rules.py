import kaizen.rules

from kaizen.system import Quilt

class Gettext(kaizen.rules.ConfigureRules):

    url = "http://ftp.gnu.org/pub/gnu/gettext/gettext-%(version)s.tar.gz"
    hash = { "md5" : "3dd55b952826d2b32f51308f2f91aa89",
             "sha1" : "5009deb02f67fc3c59c8ce6b82408d1d35d4e38f" }
    version = "0.18.1.1"
    name = "gettext"

    patch_cmd = Quilt

    configure_args = ["--without-git",
                      "--without-cvs",
                      "--disable-csharp",
                      "--disable-native-java",
                      "--without-emacs",
                     ]

    depends = ["libexpat", "ncurses"]
