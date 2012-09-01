import kaizen.rules

class Libmng(kaizen.rules.Rules):

    url = "http://downloads.sourceforge.net/project/libmng/libmng-devel/%(version)s/libmng-%(version)s.tar.gz"
    hash = { "md5" : "a464ae7d679781beebdf7440d144b7bd",
             "sha1" : "78ad516a1de79d00de720bf2a7c9afea2c896b09" }
    version = "1.0.10"
    name = "libmng"
