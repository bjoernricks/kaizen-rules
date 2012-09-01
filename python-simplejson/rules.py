import kaizen.rules

class Pythonsimplejson(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/s/simplejson/simplejson-2.3.2.tar.gz"
    hash = { "md5" : "0863e016f682f06ead07dd9efad95194",
             "sha1" : "065cc782f0dade510596e565ea7d0e83b0e8b211" }
    version = "2.3.2"
    name = "simplejson"

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
