import kaizen.rules

class Gawk(kaizen.rules.ConfigureRules):

    url = "http://ftp.gnu.org/gnu/gawk/gawk-4.0.0.tar.bz2"
    hash = { "md5" : "7cdc48e99b885a4bbe0e98dcf1706b22",
             "sha1" : "9e1b7d86b5e80c85e699c269d59d6711753c51d1" }
    version = "4.0.0"
    name = "gawk"

    depends = ["libiconv", "gettext"]
