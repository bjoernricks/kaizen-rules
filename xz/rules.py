import jam.session

class Xz(jam.session.ConfigureSession):

    url = "http://tukaani.org/xz/xz-5.0.3.tar.bz2"
    hash = { "md5" : "8d900b742b94fa9e708ca4f5a4b29003",
             "sha1" : "79661fd1c24603437e325d76732046b1da683b32" }
    version = "5.0.3"
    name = "xz"

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
