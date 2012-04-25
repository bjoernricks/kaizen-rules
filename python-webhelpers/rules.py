import jam.session

class Pythonwebhelpers(jam.session.PythonSession):

    url = "http://pypi.python.org/packages/source/W/WebHelpers/WebHelpers-1.3.tar.gz"
    hash = { "md5" : "32749ffadfc40fea51075a7def32588b",
             "sha1" : "5ef6e48aade8c625577def09cf670ef10d197911" }
    version = "1.3"
    name = "WebHelpers"

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
