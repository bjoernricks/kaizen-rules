import kaizen.rules

from kaizen.system import Delete, Quilt

class Cmake(kaizen.rules.ConfigureRules):

    url = "http://www.cmake.org/files/v2.8/cmake-%(version)s.tar.gz"
    hash = { "md5" : "801f4c87f8b604f727df5bf1f05a59e7",
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
