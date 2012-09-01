import kaizen.rules

class Pythonformencode(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/F/FormEncode/FormEncode-%(version)s.tar.gz"
    hash = { "md5" : "da23d54af521d1feab12b4caf30e3111",
             "sha1" : "573359ec15934be9b1e74c11e1796b8df872c677" }
    version = "1.2.2"
    name = "FormEncode"
