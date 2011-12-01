import jam.session

class Shiboken(jam.session.CMakeSession):

    url = "http://www.pyside.org/files/%(name)s-%(version)s.tar.bz2"
    hash = { "md5" : "b98e7c35edef95a77594a6d1801c5875",
             "sha1" : "8f7629f5f91bec17b8a02655438a99f129b931eb" }
    version = "1.0.10"
    name = "shiboken"

    depends = ["python", "qt4", "apiextractor", "generatorrunner"]

    configure_args = ["-DBUILD_TESTS=FALSE"]
