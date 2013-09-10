import kaizen.rules

class Gnupg(kaizen.rules.ConfigureRules):

    url = "ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-1.4.14.tar.bz2"
    hash = { "md5" : "99dede468204cb6ee22de7e3e3772ab1",
             "sha1" : "6202181ba2871fb3448c751a573b4ae0c4770806" }
    version = "1.4.14"
    name = "gnupg"

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
    # all patches will be copied to %(downloadroot)s/%(rules)s/patches
    # e.g. patches = ["01-patch.diff", "http://url.com/remotepatch.diff",
    #                ["http://url.com/abc.diff", "localname.diff"]]
    # patches = [""]

    # uncomment to add a dependency on an other rules
    # depends = [""]
