import kaizen.rules

class Pythonmccabe(kaizen.rules.PythonRules):

    url = "https://pypi.python.org/packages/source/m/mccabe/mccabe-%(version)s.tar.gz"
    hash = { "md5" : "c1012c7c24081471f45aab864d4e3805",
             "sha1" : "ff5593533a687b420d5cd402ab51643d57a0757e" }
    version = "0.2"
    name = "mccabe"
