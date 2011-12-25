import jam.session

class Pth(jam.session.ConfigureSession):

    url = "ftp://ftp.gnu.org/gnu/pth/pth-2.0.7.tar.gz"
    hash = { "md5" : "9cb4a25331a4c4db866a31cbe507c793",
             "sha1" : "9a71915c89ff2414de69fe104ae1016d513afeee" }
    version = "2.0.7"
    name = "pth"

    # uncomment to set path to source directory
    # default is %(src_dir)s/%(name)s-%(version)s
    # src_path = ""

    # uncomment to set path to build directory (normally not necessary)
    # build_path = ""

    # uncomment to pass additional parameters to configure script
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
