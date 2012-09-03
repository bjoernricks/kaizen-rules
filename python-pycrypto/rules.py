import kaizen.rules

class Pythonpycrypto(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/p/pycrypto/pycrypto-%(version)s.tar.gz"
    hash = { "md5" : "783e45d4a1a309e03ab378b00f97b291",
             "sha1" : "1fe50712e0776b45900f8032357201239223ab7e" }
    version = "2.5"
    name = "pycrypto"
