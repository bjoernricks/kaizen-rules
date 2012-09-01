import kaizen.rules

class Pythonnose(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/n/nose/nose-%(version)s.tar.gz"
    hash = { "md5" : "144f237b615e23f21f6a50b2183aa817",
             "sha1" : "7525f7ef056af66cdbada010d4a8b96e63a193e8" }
    version = "1.1.2"
    name = "nose"
