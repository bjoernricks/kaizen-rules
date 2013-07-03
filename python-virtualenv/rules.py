import kaizen.rules

class Pythonvirtualenv(kaizen.rules.PythonRules):

    url = "https://pypi.python.org/packages/source/v/virtualenv/virtualenv-%(version)s.tar.gz"
    hash = { "md5" : "07e09df0adfca0b2d487e39a4bf2270a",
             "sha1" : "b7d1704ec186a71c2fff1706896ecd294b708a55" }
    version = "1.9.1"
    name = "virtualenv"

