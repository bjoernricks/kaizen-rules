import kaizen.rules

class Clucenecore(kaizen.rules.CMakeRules):

    url = "http://downloads.sourceforge.net/project/clucene/clucene-core-unstable/2.3/clucene-core-%(version)s.tar.gz"
    hash = { "md5" : "48d647fbd8ef8889e5a7f422c1bfda94",
             "sha1" : "76d6788e747e78abb5abf8eaad78d3342da5f2a4" }

    branch = "clucene-src-2.3.3.4"

    version = "2.3.3.4"
    name = "clucene-core"

    depends = ["zlib", "boost"]
