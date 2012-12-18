import kaizen.rules

class Pythonjedi(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/j/jedi/jedi-%(version)s.tar.gz"
    hash = { "md5" : "eaf183537b1fd2eb122b85c526dea729",
             "sha1" : "7c73072cf660f8117364ebcbf355ce7b6e3ec8bf" }
    version = "0.5b5"
    name = "jedi"
