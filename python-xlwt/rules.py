import kaizen.rules

class Pythonxlwt(kaizen.rules.PythonRules):

    url = "https://pypi.python.org/packages/source/x/xlwt/xlwt-%(version)s.tar.gz"
    hash = { "md5" : "ed4b529b883a60b1b887fa30f31823f3",
             "sha1" : "f56d3de29bc3f39c560660fd7aaecef6ad7cb5a4" }
    version = "0.7.2"
    name = "xlwt"
