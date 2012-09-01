import kaizen.rules

class Clucenecore(kaizen.rules.CMakeRules):

    url = "http://downloads.sourceforge.net/project/clucene/clucene-core-stable/%(version)s/clucene-core-%(version)s.tar.bz2"
    hash = { "md5" : "ba1a8f764a2ca19c66ad907dddd88352",
             "sha1" : "8bc505b64f82723c2dc901036cb0607500870973" }
    version = "0.9.21b"
    name = "clucene-core"

    patches = ["patch-CMakeLists.txt.diff"]
