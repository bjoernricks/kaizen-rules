import jam.session

class Coreutils(jam.session.ConfigureSession):

    url = "http://ftp.gnu.org/gnu/coreutils/coreutils-%(version)s.tar.gz"
    hash = { "md5" : "f5e8bb4752ee2e876ddd99bda7471f35",
             "sha1" : "83b7e25661c439ecac55e99ff0dd816b9ff478a5" }
    version = "8.13"
    name = "coreutils"
