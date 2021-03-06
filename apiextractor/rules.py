import kaizen.rules

from kaizen.system import Quilt

class Apiextractor(kaizen.rules.CMakeRules):

    url = "http://www.pyside.org/files/%(name)s-%(version)s.tar.bz2"
    hash = { "md5" : "89a3dd539e98fccd0b3f8da881f60395",
             "sha1" : "da6bc41731d3f650e4cab4d0f9be7c72875106f4" }
    version = "0.10.9"
    name = "apiextractor"

    depends = ["python", "qt4", "libxml2", "libxslt"]

    patch_cmd = Quilt

    configure_args = ["-DBUILD_TESTS=FALSE"]
