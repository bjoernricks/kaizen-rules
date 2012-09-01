import kaizen.rules

class Pythondistribute(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/d/distribute/distribute-%(version)s.tar.gz"
    hash = { "md5" : "17722b22141aba8235787f79800cc452",
             "sha1" : "0670bdbba2be6892f67a6f946259776fa8331525" }
    version = "0.6.24"
    name = "distribute"
