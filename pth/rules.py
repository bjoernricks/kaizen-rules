import kaizen.rules

class Pth(kaizen.rules.ConfigureRules):

    url = "ftp://ftp.gnu.org/gnu/pth/pth-%(version)s.tar.gz"
    hash = { "md5" : "9cb4a25331a4c4db866a31cbe507c793",
             "sha1" : "9a71915c89ff2414de69fe104ae1016d513afeee" }
    version = "2.0.7"
    name = "pth"
