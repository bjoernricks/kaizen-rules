import jam.session

class Pythondecorator(jam.session.PythonSession):

    url = "http://pypi.python.org/packages/source/d/decorator/decorator-3.3.2.tar.gz"
    hash = { "md5" : "446f5165af67eb0fcd8fd28abd259e86",
             "sha1" : "56925abc3c4dcd95016ebdbc40e38d1a6a2ad644" }
    version = "3.3.2"
    name = "decorator"

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
