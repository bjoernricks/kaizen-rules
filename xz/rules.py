import kaizen.rules

class Xz(kaizen.rules.ConfigureRules):

    url = "http://tukaani.org/xz/xz-%(version)s.tar.bz2"
    hash = { "md5" : "8d900b742b94fa9e708ca4f5a4b29003",
             "sha1" : "79661fd1c24603437e325d76732046b1da683b32" }
    version = "5.0.3"
    name = "xz"
