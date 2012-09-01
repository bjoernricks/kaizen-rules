import kaizen.rules

class Pythongitpython(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/G/GitPython/GitPython-%(version)s.tar.gz"
    hash = { "md5" : "849082fe29adc653a3621465213cab96",
             "sha1" : "b9f43c91452f3fe7e105ac54ce878ff20ea44f44" }
    version = "0.3.2.RC1"
    name = "GitPython"
