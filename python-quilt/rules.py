import kaizen.rules

class PythonQuilt(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/p/python-quilt/python-quilt-%(version)s.tar.bz2"
    hash = { "md5" : "e7b11818c839c99a769d26b755ed6aed",
             "sha1" : "06f5559fae5d7b34081ad0ddb4c1a666db032e88" }
    version = "0.2"
    name = "python-quilt"

    depends = ["patch", "diffutils"]
