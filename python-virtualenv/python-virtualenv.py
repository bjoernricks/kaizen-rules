import jam.session

class Pythonvirtualenv(jam.session.PythonSession):

    url = "http://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.6.4.tar.gz"
    hash = { "md5" : "1072b66d53c24e019a8f1304ac9d9fc5",
             "sha1" : "eeaae3a84d9076577996a02951afc78b8e947067" }
    version = "1.6.4"
    name = "virtualenv"

    # uncomment to set path to source directory
    # default is %(src_dir)s/%(name)s-%(version)s
    # src_path = ""

    # uncomment to set path to build directory (normally not necessary)
    # build_path = ""

    # uncomment to pass additonal parameters to configure script
    # args = [""]

    # uncomment to add additonal patches 
    # all patches will be copied to %(downloadroot)s/%(session)s/patches
    # e.g. patches = ["01-patch.diff", "http://url.com/remotepatch.diff"]
    # patches = [""]

    # uncomment to add a dependency on an other session
    # depends = [""]
