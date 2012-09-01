import kaizen.rules

class Pythontempita(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/T/Tempita/Tempita-0.4.tar.gz"
    hash = { "md5" : "0abe015a72e748d0c6284679a497426c",
             "sha1" : "9528be505141f6b8454a4c5fefceeccf4dc7e28b" }
    version = "0.4"
    name = "Tempita"

    # kaizen.rules.PythonRules already depends on python
    # depends = ["python"]

    # uncomment to set path to source directory
    # default is %(src_dir)s/%(name)s-%(version)s
    # src_path = ""

    # uncomment to set path to build directory (normally not necessary)
    # build_path = ""

    # uncomment to pass additional parameters to setup.py script
    # build_args = [""]

    # uncomment to add additonal patches 
    # all patches will be copied to %(downloadroot)s/%(session)s/patches
    # e.g. patches = ["01-patch.diff", "http://url.com/remotepatch.diff"]
    # patches = [""]
