import kaizen.rules

class Pythonweberror(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/W/WebError/WebError-%(version)s.tar.gz"
    hash = { "md5" : "84b9990b0baae6fd440b1e60cdd06f9a",
             "sha1" : "6c8b4e77d93e1234cf1ef6d6b0dcad0a91a1af55" }
    version = "0.10.3"
    name = "WebError"
