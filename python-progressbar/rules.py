import kaizen.rules

class Pythonprogressbar(kaizen.rules.PythonRules):

    url = "http://python-progressbar.googlecode.com/files/progressbar-%(version)s.tar.gz"
    hash = { "md5" : "4f904e94b783b4c6e71aa74fd2432c59",
             "sha1" : "aebb94b452990468c77090fb43b335cf0a724353" }
    version = "2.3"
    name = "progressbar"
