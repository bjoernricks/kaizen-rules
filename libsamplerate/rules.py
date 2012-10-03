import kaizen.rules

class Libsamplerate(kaizen.rules.ConfigureRules):

    url = "http://www.mega-nerd.com/SRC/libsamplerate-%(version)s.tar.gz"
    hash = { "md5" : "1c7fb25191b4e6e3628d198a66a84f47",
             "sha1" : "e5fe82c4786be2fa33ca6bd4897db4868347fe70" }
    version = "0.1.8"
    name = "libsamplerate"

    depends = ["pkg-config"]
