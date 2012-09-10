import kaizen.rules

class Virtuosoopensource(kaizen.rules.ConfigureRules):

    url = "http://downloads.sourceforge.net/project/virtuoso/virtuoso/%(version)s/virtuoso-opensource-%(version)s.tar.gz"
    hash = { "md5" : "3991149c570f3738c3e819ce603e487f",
             "sha1" : "03bc14b1627d16d76687f8b8659801966aab3fb4" }
    version = "6.1.6"
    name = "virtuoso-opensource"

    build_path = "%(src_path)s"

    depends = ["libiodbc",
               "openssl",
               "libxml2",
               "zlib",
               "openldap",
               "gnu-awk",
               ]

    configure_args = ["--disable-mono"]

    def distclean(self):
        Delete(self.src_path).run()
