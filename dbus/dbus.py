import jam.session

class Dbus(jam.session.ConfigureSession):

    url = "http://dbus.freedesktop.org/releases/dbus/dbus-1.4.16.tar.gz"
    hash = { "md5" : "44a2a10678e7e50460879c3eb4453a65",
             "sha1" : "d6e6538cfc1ed71992f6786a6da55d815d995b5b" }
    version = "1.4.16"
    name = "dbus"

    # uncomment to set path to source directory
    # default is %(src_dir)s/%(name)s-%(version)s
    # src_path = ""

    # uncomment to set path to build directory (normally not necessary)
    # build_path = ""

    configure_args = ["--without-x", "--enable-launchd"]

    # uncomment to pass additional parameters to make
    # build_args = [""]

    # uncomment to add additonal patches 
    # all patches will be copied to %(downloadroot)s/%(session)s/patches
    # e.g. patches = ["01-patch.diff", "http://url.com/remotepatch.diff",
    #                ["http://url.com/abc.diff", "localname.diff"]]
    # patches = [""]

    # uncomment to add a dependency on an other session
    # depends = [""]
