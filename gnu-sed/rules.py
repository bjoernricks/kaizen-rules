import kaizen.rules

class GnuSed(kaizen.rules.ConfigureRules):

    url = "http://ftp.gnu.org/gnu/sed/sed-4.2.1.tar.bz2"
    hash = { "md5" : "7d310fbd76e01a01115075c1fd3f455a" }
    version = "4.2.1"
    name = "sed"

    configure_args = ["--program-prefix=g"]

