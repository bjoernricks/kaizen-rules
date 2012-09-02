import kaizen.rules

class Pythonpyliblzma(kaizen.rules.PythonRules):

    url =  "http://pypi.python.org/packages/source/p/pyliblzma/pyliblzma-%(version)s.tar.bz2"
    hash = { "md5" : "500f61116ee1ab4063b49c121786863a",
             "sha1" : "6240ec6f830f35f4087b8926a95c2074320b7ed5" }
    version = "0.5.3"
    name = "pyliblzma"

    depends = [ "pkg-config", "xz"]
