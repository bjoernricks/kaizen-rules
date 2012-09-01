import kaizen.rules

class Fontconfig(kaizen.rules.ConfigureRules):

    url = "http://www.freedesktop.org/software/fontconfig/release/fontconfig-%(version)s.tar.gz"
    hash = { "md5" : "26c83855ed256b5c032baae032fadc4f",
             "sha1" : "1ab2f437c2261028ae7969892277af2d8d8db489" }
    version = "2.9.0"
    name = "fontconfig"

    depends = ["libxml2", "freetype", "libiconv", "pkg-config"]

    configure_args = ["--enable-libxml2"]
