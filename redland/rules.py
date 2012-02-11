import jam.session

class Redland(jam.session.ConfigureSession):

    url = "http://download.librdf.org/source/redland-%(version)s.tar.gz"
    hash = { "md5" : "b0deb87f3c7d3237a3d587c1e0f2f266",
             "sha1" : "e93d6fafaeebdf9f15a1044be6f4a88270f007af" }
    version = "1.0.15"
    name = "redland"

    configure_args = ["--with-sqlite=yes", "--with-mysql=no",
                      "--with-postgresql=no", "--with-bdb=no"]

    depends = ["pkg-config", "libxml2", "libxslt", "raptor2", "rasqal"]
