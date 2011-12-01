import jam.session

class Libpng(jam.session.ConfigureSession):

    url = "http://sourceforge.net/projects/libpng/files/libpng15/1.5.6/libpng-1.5.6.tar.bz2"
    hash = { "md5" : "2107095191b0e8bd9a0f4f930c1948c3",
             "sha1" : "e0a24cc51ebc68939a5027ea4874d5f351a52647" }
    version = "1.5.6"
    name = "libpng"

    depends = ["zlib"]
