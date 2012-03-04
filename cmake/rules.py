import jam.session

from jam.system import Delete, Quilt

class Cmake(jam.session.ConfigureSession):

    url = "http://www.cmake.org/files/v2.8/cmake-2.8.5.tar.gz"
    hash = { "md5" : "3c5d32cec0f4c2dc45f4c2e84f4a20c5",
             "sha1" : "8dd4c31cbccf1a297829a476a0ef79d1614ca368" }
    version = "2.8.5"
    name = "cmake"

    configure_args = ["--mandir=/share/man", "--docdir=/share/doc/cmake",
                      "--system-libs", "--datadir=/share/cmake",
                      "--no-system-libarchive"]

    patchsystem = Quilt

    def distclean(self):
        Delete(self.build_path).run()
