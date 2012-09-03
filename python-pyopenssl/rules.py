import kaizen.rules

class Pythonpyopenssl(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/p/pyOpenSSL/pyOpenSSL-%(version)s.tar.gz"
    hash = { "md5" : "767bca18a71178ca353dff9e10941929",
             "sha1" : "b4de25c5e4e9d9bc375c419071efc45fa96d5597" }
    version = "0.13"
    name = "pyOpenSSL"

    depends = ["openssl"]
