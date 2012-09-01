import kaizen.rules

class Libmng(kaizen.rules.Rules):

    url = "http://downloads.sourceforge.net/project/libmng/libmng-devel/1.0.10/libmng-1.0.10.tar.gz"
    hash = { "md5" : "a464ae7d679781beebdf7440d144b7bd",
             "sha1" : "78ad516a1de79d00de720bf2a7c9afea2c896b09" }
    version = "1.0.10"
    name = "libmng"

    # uncomment to set path to source directory
    # default is %(src_dir)s/%(name)s-%(version)s
    # src_path = ""

    # uncomment to set path to build directory (normally not necessary)
    # build_path = ""

    # uncomment to pass additonal parameters to configure tool
    # configure_args = [""]

    # uncomment to pass additional parameters to the build tool
    # build_args = [""]

    # uncomment to add additonal patches 
    # all patches will be copied to %(downloadroot)s/%(session)s/patches
    # e.g. patches = ["01-patch.diff", "http://url.com/remotepatch.diff",
    #                ["http://url.com/abc.diff", "localname.diff"]]
    # patches = [""]

    # uncomment to add a dependency on an other session
    # depends = [""]
