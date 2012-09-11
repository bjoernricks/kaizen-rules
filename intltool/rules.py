import kaizen.rules

class Intltool(kaizen.rules.ConfigureRules):

    url = "https://launchpad.net/intltool/trunk/%(version)s/+download/intltool-%(version)s.tar.gz"
    hash = { "md5" : "23fbd879118253cb99aeac067da5f591",
             "sha1" : "7fddbd8e1bf94adbf1bc947cbf3b8ddc2453f8ad" }
    version = "0.50.2"
    name = "intltool"
    depends = ["perl", "perl-xml-sax"]
