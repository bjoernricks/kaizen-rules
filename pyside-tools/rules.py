import kaizen.rules

class Pysidetools(kaizen.rules.CMakeRules):

    url = "http://www.pyside.org/files/pyside-tools-0.2.13.tar.bz2"
    hash = { "md5" : "14d3a36df06d680357d7bc1960f19a6d",
             "sha1" : "4d05444300331518c3b66536aec3048454db3380" }
    version = "0.2.13"
    name = "pyside-tools"

    depends = ["python", "python-pyside", "qt4"]
