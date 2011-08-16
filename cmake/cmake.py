import jam.session

class Cmake(jam.session.ConfigureSession):

    url = "http://www.cmake.org/files/v2.8/cmake-2.8.5.tar.gz"
    hash = { "md5" : "3c5d32cec0f4c2dc45f4c2e84f4a20c5",
             "sha1" : "8dd4c31cbccf1a297829a476a0ef79d1614ca368" }
    version = "2.8.5"
    name = "cmake"

    # uncomment to set path to source directory
    # default is %(src_dir)s/%(name)s-%(version)s
    # src_path = ""

    # uncomment to set path to build directory (normally not necessary)
    # build_path = ""

    args = ["--mandir=/share/man", "--docdir=/share/doc/cmake",
            "--system-libs", "--datadir=/share/cmake", "--no-system-libarchive"]

    # uncomment to add additonal patches 
    # all patches will be copied to %(downloadroot)s/%(session)s/patches
    # e.g. patches = ["01-patch.diff", "http://url.com/remotepatch.diff"]
    patches =  [["http://cmake.org/gitweb?p=cmake.git;a=patch;h=702538eaa3315f3fcad9f1daea01e6a83928967b",
                 "01-findqt4.diff"]]

