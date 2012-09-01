import kaizen.rules

class Mscore(kaizen.rules.Rules):

    url = "http://sourceforge.net/projects/mscore/files/mscore/MuseScore-1.1/mscore-1.1.tar.bz2"
    hash = { "md5" : "68b43af92093a16f7f074c0eb560a867",
             "sha1" : "a4e3963b995bbadf0f9a9ecdb6134d58414fd6cc" }
    version = "1.1"
    name = "mscore"

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
    depends = ["qt4"]
