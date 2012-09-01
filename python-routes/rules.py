import kaizen.rules

class Pythonroutes(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/R/Routes/%(name)s-%(version)s.tar.gz"
    hash = { "md5" : "9740ff424ff6b841632c784a38fb2be3",
             "sha1" : "70b741ee898fe597e570b76cc20c06eeb5db1ec8" }
    version = "1.12.3"
    name = "Routes"
