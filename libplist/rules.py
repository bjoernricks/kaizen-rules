import jam.session

class Libplist(jam.session.CMakeSession):

    url = "http://www.libimobiledevice.org/downloads/libplist-1.8.tar.bz2"
    hash = { "md5" : "2a9e0258847d50f9760dc3ece25f4dc6",
             "sha1" : "dea18ac31cc497dba959bdb459a2a49fb41664c3" }
    version = "1.8"
    name = "libplist"

    configure_args = ["-DENABLE_SWIG=OFF", "-DENABLE_CYTHON=OFF"]

    depends = ["libxml2"]
