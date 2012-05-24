import jam.session

class Pythonpastescript(jam.session.PythonSession):

    url = "http://pypi.python.org/packages/source/P/PasteScript/%(name)s-%(version)s.tar.gz"
    hash = { "md5" : "e08017f60f4ff9067d2b88d3c2a49717",
             "sha1" : "7fafeec284e4d13ddb6be717acee5cbfe6f1e1ec" }
    version = "1.7.4.2"
    name = "PasteScript"

    depends = ["python-pastedeploy"]
