import jam.session

class Pythonnose(jam.session.PythonSession):

    url = "http://pypi.python.org/packages/source/n/nose/nose-1.1.2.tar.gz"
    hash = { "md5" : "144f237b615e23f21f6a50b2183aa817",
             "sha1" : "7525f7ef056af66cdbada010d4a8b96e63a193e8" }
    version = "1.1.2"
    name = "nose"

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
