import kaizen.rules

class Soprano(kaizen.rules.CMakeRules):

    url = "http://downloads.sourceforge.net/project/soprano/Soprano/%(version)s/soprano-%(version)s.tar.bz2"
    hash = { "md5" : "783fb07f9679f45e987aff7a17bef649",
             "sha1" : "d16231dc021bd66eebb9d1975ba075d2169a2617" }
    version = "2.7.4"
    name = "soprano"

    depends = ["raptor2", "rasqal", "redland", "clucene", "qt4", "libiodbc",
               "strigi"]

    runtime_depends = ["virtuoso"]

    configure_args = ["-DSOPRANO_DISABLE_SESAME2_BACKEND=ON",
                      "-DCMAKE_BUILD_TYPE=Release"]
