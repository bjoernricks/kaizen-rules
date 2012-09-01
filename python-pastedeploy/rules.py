import kaizen.rules

class Pythonpastedeploy(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/P/PasteDeploy/PasteDeploy-1.5.0.tar.gz"
    hash = { "md5" : "f1a068a0b680493b6eaff3dd7690690f",
             "sha1" : "4bae6b28b5243af0e4c0f40b7f20037d1a0ae846" }
    version = "1.5.0"
    name = "PasteDeploy"

    depends = ["python-paste"]
