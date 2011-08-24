import jam.session

class Cscope(jam.session.ConfigureSession):

    url = "http://downloads.sourceforge.net/project/cscope/cscope/15.7a/cscope-15.7a.tar.bz2"
    hash = { "md5" : "da43987622ace8c36bbf14c15a350ec1",
             "sha1" : "f6348694e5443769add851f97fd39365e93dc474" }
    version = "15.7a"
    name = "cscope"

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
    patches = ["01-ncurses.diff"]

    # uncomment to add a dependency on an other session
    # depends = [""]
