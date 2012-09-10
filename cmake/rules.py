import kaizen.rules

from kaizen.system import Delete, Quilt

class Cmake(kaizen.rules.ConfigureRules):

    url = "http://www.cmake.org/files/v2.8/cmake-%(version)s.tar.gz"
    hash = { "md5" : "6464d429b1396a8db35864e791673b65",
             "sha1" : "b96663c0757a5edfbddc410aabf7126a92131e2b" }
    version = "2.8.9"
    name = "cmake"

    depends = ["bzip2", "ncurses", "libcurl", "libexpat", "zlib"]

    configure_args = ["--mandir=/share/man", "--docdir=/share/doc/cmake",
                      "--system-libs", "--datadir=/share/cmake",
                      "--no-system-libarchive"]

    patch_cmd = Quilt

    def distclean(self):
        Delete(self.build_path).run()
