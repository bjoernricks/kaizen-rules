import kaizen.rules

class Pythonbabel(kaizen.rules.PythonRules):

    url = "http://ftp.edgewall.com/pub/babel/Babel-0.9.6.tar.gz"
    hash = { "md5" : "f0edcad03dfdb5505f337ef1a7690325",
             "sha1" : "37810107bc36da21f44a50f0af3e75dcd2ca668d" }
    version = "0.9.6"
    name = "Babel"

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

    # uncomment to add a dependency on an other session
    # depends = [""]
