import jam.session

from jam.system import Quilt

class Generatorrunner(jam.session.CMakeSession):

    url = "http://www.pyside.org/files/%(name)s-%(version)s.tar.bz2"
    hash = { "md5" : "88425f176ffc3810307edabc381415c6",
             "sha1" : "2ed6a03228d20fb31cca6712c569c07dff325988" }
    version = "0.6.15"
    name = "generatorrunner"

    depends = ["qt4", "apiextractor"]

    patchsystem = Quilt

    configure_args = ["-DBUILD_TESTS=FALSE"]
