import kaizen.rules

class Pythonsouth(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/S/South/South-%(version)s.tar.gz"
    hash = { "md5" : "6089871449006d45d06c409b42d8bd44",
             "sha1" : "651f0fdedf009fe01ab8fc7d5ebe4b38a228826d" }
    version = "0.7.6"
    name = "South"

    depends = ["python-django"]
