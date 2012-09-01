import kaizen.rules

class Taglibextras(kaizen.rules.CMakeRules):

    url = "http://www.kollide.net/~jefferai/taglib-extras-%(version)s.tar.gz"
    hash = { "md5" : "e973ca609b18e2c03c147ff9fd9e6eb8",
             "sha1" : "58af454ec230d494a75abd0aa78016a969f0c9ce" }
    version = "1.0.1"
    name = "taglib-extras"

    depends = ["taglib", "qt4"]
