import kaizen.rules

class Tomahawk(kaizen.rules.CMakeRules):

    url = ["https://github.com/tomahawk-player/tomahawk/tarball/%(version)s",
           "tomahawk-%(version)s.tar.gz"]
    hash = { "md5" : "f71bd3f12dc1f23c3e1e593bbd7af6ff",
             "sha1" : "b51ba08748ec8ea11eda413c9523023f69db93cf" }
    version = "0.5.5"
    name = "tomahawk"
    src_path = "%(src_dir)s/tomahawk-player-tomahawk-ce76c86"

    depends = ["qt4", "qjson", "sqlite3" , "taglib", "boost", "clucene-devel",
               "libechonest", "attica", "quazip", "qca", "kdelibs",
               "liblastfm"]
