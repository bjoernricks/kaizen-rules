import kaizen.rules

class Pythonmarkupsafe(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/M/MarkupSafe/MarkupSafe-%(version)s.tar.gz"
    hash = { "md5" : "4e7c4d965fe5e033fa2d7bb7746bb186",
             "sha1" : "81e0c898c289721d5b1aa70ffc0dfc35886ea92a" }
    version = "0.15"
    name = "MarkupSafe"
