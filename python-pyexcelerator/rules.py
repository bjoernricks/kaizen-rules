import kaizen.rules

class Pythonpyexcelerator(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/p/pyExcelerator/pyexcelerator-%(version)s.tar.bz2"
    hash = { "md5" : "478c79a74be39d27eee9bd1b3032dffe",
             "sha1" : "3fed4c8e2a720a52ecea306aecdcf9d26e3deaa9" }
    version = "0.6.4.1"
    name = "pyexcelerator"
