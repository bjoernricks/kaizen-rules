import kaizen.rules

class Gdbm(kaizen.rules.ConfigureRules):

    url = "ftp://ftp.gnu.org/gnu/gdbm/gdbm-%(version)s.tar.gz"
    hash = { "md5" : "88770493c2559dc80b561293e39d3570",
             "sha1" : "441201e9145f590ba613f8a1e952455d620e0860" }
    version = "1.10"
    name = "gdbm"

    depends = ["gettext"]
