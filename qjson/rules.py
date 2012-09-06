import kaizen.rules

class Qjson(kaizen.rules.CMakeRules):

    url = "http://downloads.sourceforge.net/project/qjson/qjson/0.7.1/qjson-%(version)s.tar.bz2"
    hash = { "md5" : "5a833ad606c164ed8aa69f0873366ace",
             "sha1" : "19bbef24132b238e99744bb35194c6dadece98f9" }
    version = "0.7.1"
    name = "qjson"

    src_path = "%(src_dir)s/%(name)s"

    depends = ["qt4"]
