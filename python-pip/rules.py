import kaizen.rules

class Pythonpip(kaizen.rules.PythonRules):

    url = "https://pypi.python.org/packages/source/p/pip/pip-%(version)s.tar.gz"
    hash = { "md5" : "cbb27a191cebc58997c4da8513863153",
             "sha1" : "9c70d314e5dea6f41415af814056b0f63c3ffd14" }
    version = "1.3.1"
    name = "pip"
