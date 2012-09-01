import kaizen.rules

class Gpgme(kaizen.rules.ConfigureRules):

    url = "ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-%(version)s.tar.bz2"
    hash = { "md5" : "90afa8436ce2b2683c001c824bd22601",
             "sha1" : "7d19a95a2239da13764dad7f97541be884ec5a37" }
    version = "1.3.1"
    name = "gpgme"

    depends = ["libassuan", "gnupg2", "libgpg-error"]

    configure_args = ["--with-gpg=%(prefix)s/bin/gpg2"]

