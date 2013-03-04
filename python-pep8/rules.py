import kaizen.rules

class Pythonpep8(kaizen.rules.PythonRules):

    url = "https://pypi.python.org/packages/source/p/pep8/pep8-%(version)s.tar.gz"
    hash = { "md5" : "c48dc736e09f4f76362572c4e8b55be3",
             "sha1" : "ce93871c3f13c4cf5eec400bf36f5b04d1f72393" }
    version = "1.4.4"
    name = "pep8"
