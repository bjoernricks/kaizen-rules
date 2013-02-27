import kaizen.rules

class Pythondjangodebugtoolbar(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/d/%(name)s/%(name)s-%(version)s.tar.gz"
    hash = { "md5" : "85c1c70a31f0a3a646a603214d235e9f",
             "sha1" : "79a79a92509e9d4090b892c53711f63824744191" }
    version = "0.9.4"
    name = "django-debug-toolbar"
