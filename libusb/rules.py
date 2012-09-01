import kaizen.rules

class Libusb(kaizen.rules.ConfigureRules):

    url = "http://downloads.sourceforge.net/project/libusb/libusb-1.0/libusb-%(version)s/libusb-%(version)s.tar.bz2"
    hash = { "md5" : "37d34e6eaa69a4b645a19ff4ca63ceef",
             "sha1" : "5484397860f709c9b51611d224819f8ed5994063" }
    version = "1.0.8"
    name = "libusb"
