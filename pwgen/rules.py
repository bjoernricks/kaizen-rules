import kaizen.rules

class Pwgen(kaizen.rules.ConfigureRules):

    url = "http://downloads.sourceforge.net/project/pwgen/pwgen/%(version)s/pwgen-%(version)s.tar.gz"
    hash = { "md5" : "935aebcbe610fbc9de8125e7b7d71297",
             "sha1" : "43dc4fbe6c3bdf96ae24b20d44c4a4584df93d8e" }
    version = "2.06"
    name = "pwgen"
