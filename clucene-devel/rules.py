import kaizen.rules

from kaizen.system.download import GitDownloader

class Clucenecore(kaizen.rules.CMakeRules):

    url = "git://clucene.git.sourceforge.net/gitroot/clucene/clucene"
    hash = { "md5" : "ba1a8f764a2ca19c66ad907dddd88352",
             "sha1" : "8bc505b64f82723c2dc901036cb0607500870973" }

    branch = "clucene-src-2.3.3.4"

    version = "2.3.3.4"
    name = "clucene-core"
