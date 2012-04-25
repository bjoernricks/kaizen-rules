import jam.session

class Pythonwebtest(jam.session.PythonSession):

    url = "http://pypi.python.org/packages/source/W/WebTest/WebTest-1.3.3.tar.gz"
    hash = { "md5" : "a35a8b6207a66e232a0fa7ee254dac76",
             "sha1" : "c0c55b110fdb00b06513849c5939dd83128af41c" }
    version = "1.3.3"
    name = "WebTest"

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
