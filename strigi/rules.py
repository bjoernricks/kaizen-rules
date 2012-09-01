import kaizen.rules

class Strigi(kaizen.rules.CMakeRules):

    url = "http://www.vandenoever.info/software/strigi/strigi-%(version)s.tar.bz2"
    hash = { "md5" : "0559e2ab65d187d30916e9ffe36e0fb6",
             "sha1" : "0aa3632e07c58f2ab5c515004b790bda6cfefbf5" }
    version = "0.7.5"
    name = "strigi"

    depends = ["libxml2", "clucene", "dbus", "qt4"]

    patches = ["patch-libsteamanalyzer-lib-CMakelists.txt.diff",
               "patch-libstreams-lib-CMakeLists.txt.diff"]

    configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
