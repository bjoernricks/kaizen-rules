import jam.session

class Libpng(jam.session.ConfigureSession):

    url = "http://downloads.sourceforge.net/project/libpng/libpng15/1.5.5/libpng-1.5.5.tar.bz2"
    hash = { "md5" : "3270bf2990c3174ae939388398de751e",
             "sha1" : "be63517aa20e8539f0be07706326f5cb53c42e13" }
    version = "1.5.5"
    name = "libpng"

    depends = ["zlib"]
