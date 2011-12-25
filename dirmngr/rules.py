import jam.session

class Dirmngr(jam.session.ConfigureSession):

    url = "ftp://ftp.gnupg.org/gcrypt/dirmngr/dirmngr-1.1.0.tar.bz2"
    hash = { "md5" : "f2570f0248f5947daac200e85291b328",
             "sha1" : "a7a7d1432db9edad2783ea1bce761a8106464165" }
    version = "1.1.0"
    name = "dirmngr"

    depends = ["libgcrypt", "libassuan", "libksba", "gettext", "libiconv",
               "libgpg-error", "pth"]
