import kaizen.rules

class Pythonwebhelpers(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/W/WebHelpers/WebHelpers-%(version)s.tar.gz"
    hash = { "md5" : "32749ffadfc40fea51075a7def32588b",
             "sha1" : "5ef6e48aade8c625577def09cf670ef10d197911" }
    version = "1.3"
    name = "WebHelpers"
