import kaizen.rules

class Pcre(kaizen.rules.CMakeRules):

    url = "http://downloads.sourceforge.net/project/pcre/pcre/%(version)s/pcre-%(version)s.tar.bz2"
    hash = { "md5" : "0a7b592bea64b7aa7f4011fc7171a730",
             "sha1" : "52abf655d94f5208377258ffff27c7b35c53af39" }
    version = "8.21"
    name = "pcre"

    depends = ["bzip2", "zlib"]

    configure_args = ["--enable-utf8",
                      "--enable-unicode-properties",
                      "--enable-pcregrep-libz",
                      "--enable-pcregrep-libbz2"]
