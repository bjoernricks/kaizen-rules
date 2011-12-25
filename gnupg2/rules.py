import jam.session

class Gnupg(jam.session.ConfigureSession):

    url = "ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-2.0.18.tar.bz2"
    hash = { "md5" : "2f37e0722666a0fedbe4d9f9227ac4d7",
             "sha1" : "5ec2f718760cc3121970a140aeea004b64545c46" }
    version = "2.0.18"
    name = "gnupg"

    depends = ["libgpg-error",
               "libassuan",
               "pinentry",
               "libgcrypt",
               "libksba",
               "pth",
               "gettext",
               "zlib",
               "libiconv",
               "bzip2",
               "curl",
               "dirmngr",
               ]
