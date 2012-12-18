import kaizen.rules

class Pythonbleach(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/b/bleach/bleach-%(version)s.tar.gz"
    hash = { "md5" : "6b4f76ae47c40f5170a3e674dc96281c",
             "sha1" : "c9c5ea22a1a2ef4c6804f9ed8138c2d9ad6a23d4" }
    version = "1.1.5"
    name = "bleach"

    depends = ["python-html5lib"]
