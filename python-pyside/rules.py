import jam.session

class Pyside(jam.session.CMakeSession):

    url = "http://www.pyside.org/files/%(name)s-qt4.7+%(version)s.tar.bz2"
    hash = { "md5" : "63d1104cf245d9eea307434c94e15443",
             "sha1" : "99a29555e1214f4e359e1e7e8ffb07031c9bfc10" }
    version = "1.0.9"
    name = "pyside"

    src_path = "%(src_dir)s/%(name)s-qt4.7+%(version)s"

    depends = ["python", "qt4", "shiboken", "generatorrunner"]

    configure_args = ["-DBUILD_TESTS=FALSE",]
