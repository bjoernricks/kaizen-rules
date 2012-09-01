import kaizen.rules

class Xmlto(kaizen.rules.ConfigureRules):

    url = "https://fedorahosted.org/releases/x/m/xmlto/xmlto-%(version)s.tar.bz2"
    hash = { "md5" : "6b6267b1470f8571fe5f63a128970364",
             "sha1" : "5d1aecd59d519066f94b4591722767c4e41bdc0f" }
    version = "0.0.25"
    name = "xmlto"

    depends = ["getopt", "libxml2"]
