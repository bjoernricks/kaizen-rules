import kaizen.rules

class Pythonhtml5lib(kaizen.rules.PythonRules):

    url = "http://html5lib.googlecode.com/files/html5lib-%(version)s.tar.gz"
    hash = { "md5" : "fe607f9917d81763e842f818f23464ee",
             "sha1" : "1645840a6dbd152c06aa513e04dfafe09a36703a" }
    version = "0.95"
    name = "html5lib"
