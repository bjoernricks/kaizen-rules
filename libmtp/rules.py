import kaizen.rules

class Libmtp(kaizen.rules.ConfigureRules):

    url = "http://downloads.sourceforge.net/project/libmtp/libmtp/%(version)s/libmtp-%(version)s.tar.gz"
    hash = { "md5" : "6dc708757e3fd3ccce7445b4f2171263",
             "sha1" : "239c07afcb1ebd02b865050d0a31f5ff36b012d5" }
    version = "1.1.2"
    name = "libmtp"

    build_path = "%(src_path)s"

    depends = ["libusb-compat"]

    configure_cflags = ["-I%(prefix)s/include"]
