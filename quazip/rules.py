import kaizen.rules

class Quazip(kaizen.rules.CMakeRules):

    url = "http://downloads.sourceforge.net/project/quazip/quazip/%(version)s/quazip-%(version)s.tar.gz"
    hash = { "md5" : "ab0763709c7e6863b30ffd018397a6d3",
             "sha1" : "7074822d7d082890a23e0cb10f6875bcb84b880c" }
    version = "0.5"
    name = "quazip"

    depends = ["qt4", "zlib"]
