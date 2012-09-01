import kaizen.rules

class Pythonfunkload(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/f/funkload/funkload-%(version)s.tar.gz"
    hash = { "md5" : "d2e5e5098e332c75b02825ed4318e49c",
             "sha1" : "48ada07dfa951f5dd9bc1555f25fb0b6f0bccd16" }
    version = "1.16.1"
    name = "funkload"

    depends = ["python-webunit", "python-docutils", "python-distribute"]
