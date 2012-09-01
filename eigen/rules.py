import kaizen.rules

class Eigen(kaizen.rules.CMakeRules):

    url = "http://bitbucket.org/eigen/eigen/get/%(version)s.tar.bz2"
    hash = { "md5" : "43070952464a5bf21694e082e7fb8fce",
             "sha1" : "f2c726897860b4ebc63f74f6097d315aacee1eaf" }
    version = "3.0.5"
    name = "eigen"

    src_path = "%(src_dir)s/eigen-eigen-6e7488e20373"

    depends = ["qt4", "pkg-config"]
