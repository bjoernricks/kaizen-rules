import kaizen.rules

class Libpng(kaizen.rules.ConfigureRules):

    url = "http://sourceforge.net/projects/libpng/files/libpng15/%(version)s/libpng-%(version)s.tar.bz2"
    hash = { "md5" : "d87f9c34ccab8242c00e41925839f6c9",
             "sha1" : "e45110a5e6787819be50f31092f1a1d43b717de0" }
    version = "1.5.12"
    name = "libpng"

    depends = ["zlib"]
