import kaizen.rules

class Soprano(kaizen.rules.CMakeRules):

    url = "http://downloads.sourceforge.net/project/soprano/Soprano/%(version)s/soprano-%(version)s.tar.bz2"
    hash = { "md5" : "273c3403aeb6d8a43e78a4887f50a385",
             "sha1" : "55882adb68f90ec36b79ecf64206521226e74c8f" }
    version = "2.8.0"
    name = "soprano"

    depends = ["raptor2", "rasqal", "redland", "qt4", "libiodbc",
               "strigi"]

    runtime_depends = ["virtuoso"]

    configure_args = ["-DSOPRANO_DISABLE_SESAME2_BACKEND=ON",
                      "-DSOPRANO_DISABLE_CLUCENE_INDEX=ON",
                      "-DCMAKE_BUILD_TYPE=Release"]
