import kaizen.rules

class Grantlee(kaizen.rules.CMakeRules):

    url = "http://downloads.grantlee.org/grantlee-%(version)s.tar.gz"
    hash = { "md5" : "0622ed30630a44b5fac0bfa7e176d3fe",
             "sha1" : "25560082ce53468fae227217d5da297dbcb9c16f" }
    version = "0.2.0"
    name = "grantlee"

    depends = ["qt4", "automoc4"]
