import kaizen.rules

class Automoc4(kaizen.rules.CMakeRules):

    url = "ftp://ftp.kde.org/pub/kde/stable/%(name)s/%(version)s/%(name)s-%(version)s.tar.bz2"
    hash = { "md5" : "91bf517cb940109180ecd07bc90c69ec",
             "sha1" : "d864c3dda99d8b5f625b9267acfa1d88ff617e3a" }
    version = "0.9.88"
    name = "automoc4"

    # uncomment to set path to source directory
    # default is %(src_dir)s/%(name)s-%(version)s
    # src_path = ""

    # uncomment to set path to build directory (normally not necessary)
    # build_path = ""

    # uncomment to pass additional parameters to cmake
    # configure_args = [""]

    # uncomment to pass additional parameters to make
    # build_args = [""]

    # uncomment to add additonal patches 
    # all patches will be copied to %(downloadroot)s/%(session)s/patches
    # e.g. patches = ["01-patch.diff", "http://url.com/remotepatch.diff",
    #                ["http://url.com/abc.diff", "localname.diff"]]
    # patches = [""]

    # uncomment to add a dependency on an other session
    # depends = [""]
