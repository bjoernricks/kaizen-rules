import jam.session

class Libksba(jam.session.ConfigureSession):

    url = "ftp://ftp.gnupg.org/gcrypt/libksba/libksba-1.2.0.tar.bz2"
    hash = { "md5" : "e797f370b69b4dc776499d6a071ae137",
             "sha1" : "0c4e593464b9dec6f53c728c375d54a095658230" }
    version = "1.2.0"
    name = "libksba"

    depends = ["gettext", "libgpg-error", "libiconv"]
