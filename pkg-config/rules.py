import kaizen.rules

class Pkgconfig(kaizen.rules.ConfigureRules):

    url = "http://pkg-config.freedesktop.org/releases/pkg-config-%(version)s.tar.gz"
    hash = { "md5" : "a3270bab3f4b69b7dc6dbdacbcae9745",
             "sha1" : "8922aeb4edeff7ed554cc1969cbb4ad5a4e6b26e" }
    version = "0.25"
    name = "pkg-config"

    configure_args = \
    ["--with-pc-path=%(prefix)s/lib/pkgconfig:/usr/lib/pkgconfig:/usr/X11/lib/pkgconfig/"]
