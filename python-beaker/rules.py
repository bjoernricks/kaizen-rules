import jam.session

class Pythonbeaker(jam.session.PythonSession):

    url = "http://pypi.python.org/packages/source/B/Beaker/Beaker-1.6.2.tar.gz"
    hash = { "md5" : "455a264cb481ab07446f020c001dcdc5",
             "sha1" : "d3256b99f57ae99e042c9385068a0a515d0ebd64" }
    version = "1.6.2"
    name = "Beaker"

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
