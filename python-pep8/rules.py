import kaizen.rules

class Pythonpep8(kaizen.rules.PythonRules):

    url = "https://pypi.python.org/packages/source/p/pep8/pep8-%(version)s.tar.gz"
    hash = { "md5" : "a03bb494859e87b42601b61b1b043a0c",
             "sha1" : "33637f6cf409651826114baf2fd8bc68d144a86d" }
    version = "1.4.6"
    name = "pep8"
