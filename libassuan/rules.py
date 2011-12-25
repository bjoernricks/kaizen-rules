import jam.session

class Libassuan(jam.session.ConfigureSession):

    url = "ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-2.0.3.tar.bz2"
    hash = { "md5" : "179d1918325fdb928c7bd90b8a514fc7",
             "sha1" : "2bf4eba3b588758e349976a7eb9e8a509960c3b5" }
    version = "2.0.3"
    name = "libassuan"

    depends = ["libgpg-error", "pth"]
