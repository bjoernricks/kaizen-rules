import kaizen.rules

class Libusbcompat(kaizen.rules.ConfigureRules):

    url = "http://downloads.sourceforge.net/project/libusb/libusb-compat-0.1/libusb-compat-%(version)s/libusb-compat-%(version)s.tar.bz2"
    hash = { "md5" : "570ac2ea085b80d1f74ddc7c6a93c0eb",
             "sha1" : "d5710d5bc4b67c5344e779475b76168c7ccc5e69" }
    version = "0.1.3"
    name = "libusb-compat"

    depends = ["libusb"]
