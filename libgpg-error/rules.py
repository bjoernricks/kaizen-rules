import kaizen.rules

class Libgpgerror(kaizen.rules.ConfigureRules):

    url = "ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-1.10.tar.bz2"
    hash = { "md5" : "736a03daa9dc5873047d4eb4a9c22a16",
             "sha1" : "95b324359627fbcb762487ab6091afbe59823b29" }
    version = "1.10"
    name = "libgpg-error"


    depends = ["libiconv", "gettext"]
