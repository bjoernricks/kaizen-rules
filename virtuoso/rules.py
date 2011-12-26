import jam.session

class Virtuosoopensource(jam.session.ConfigureSession):

    url = "http://downloads.sourceforge.net/project/virtuoso/virtuoso/6.1.4/virtuoso-opensource-6.1.4.tar.gz"
    hash = { "md5" : "7110a0b4b171b84850d346f4fe648172",
             "sha1" : "39b2ad28e7ee58b5bca1ba8ff8365266dfa55fa7" }
    version = "6.1.4"
    name = "virtuoso-opensource"

    build_path = "%(src_path)s"

    depends = ["libiodbc",
               "openssl",
               "libxml2", 
               "zlib",
               "openldap",
               "gnu-awk",
               ]

    def distclean(self):
        pass
