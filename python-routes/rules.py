import jam.session

class Pythonroutes(jam.session.PythonSession):

    url = "http://pypi.python.org/packages/source/R/Routes/Routes-1.12.3.tar.gz"
    hash = { "md5" : "9740ff424ff6b841632c784a38fb2be3",
             "sha1" : "70b741ee898fe597e570b76cc20c06eeb5db1ec8" }
    version = "1.12.3"
    name = "Routes"

    # jam.session.PythonSession already depends on python
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
