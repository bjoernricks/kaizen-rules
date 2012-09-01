import kaizen.rules

class Pythonmako(kaizen.rules.PythonRules):

    url = "http://www.makotemplates.org/downloads/Mako-%(version)s.tar.gz"
    hash = { "md5" : "532d7aa7ffbfd2873c1461a30431366a",
             "sha1" : "4bb85b58ccf947ce68418a446a38a753e90ce923" }
    version = "0.5.0"
    name = "Mako"

    depends = ["python-markupsafe"]
