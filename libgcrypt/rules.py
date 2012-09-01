import kaizen.rules

class Libgcrypt(kaizen.rules.ConfigureRules):

    url = "ftp://ftp.gnupg.org/gcrypt/libgcrypt/libgcrypt-1.5.0.tar.bz2"
    hash = { "md5" : "693f9c64d50c908bc4d6e01da3ff76d8",
             "sha1" : "3e776d44375dc1a710560b98ae8437d5da6e32cf" }
    version = "1.5.0"
    name = "libgcrypt"


    depends = ["libgpg-error"]
