import kaizen.rules

class Pythondecorator(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/d/decorator/decorator-%(version)s.tar.gz"
    hash = { "md5" : "446f5165af67eb0fcd8fd28abd259e86",
             "sha1" : "56925abc3c4dcd95016ebdbc40e38d1a6a2ad644" }
    version = "3.3.2"
    name = "decorator"
