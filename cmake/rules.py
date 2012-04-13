import jam.session

from jam.system import Delete, Quilt

class Cmake(jam.session.ConfigureSession):

    url = "http://www.cmake.org/files/v2.8/cmake-%(version)s.tar.gz"
    hash = { "md5" : "e1b237aeaed880f65dec9c20602452f6",
             "sha1" : "d206182b454f4d1ddeb0f11d7d1be8a66e5c2464" }
    version = "2.8.7"
    name = "cmake"

    depends = ["bzip2", "ncurses", "libcurl", "libexpat", "zlib"]

    configure_args = ["--mandir=/share/man", "--docdir=/share/doc/cmake",
                      "--system-libs", "--datadir=/share/cmake",
                      "--no-system-libarchive"]

    patchsystem = Quilt

    def distclean(self):
        Delete(self.build_path).run()
