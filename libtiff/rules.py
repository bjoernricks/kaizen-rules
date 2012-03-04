import jam.session

class Tiff(jam.session.ConfigureSession):

    url = "http://download.osgeo.org/libtiff/tiff-%(version)s.tar.gz"
    hash = { "md5" : "8fc7ce3b4e1d0cc8a319336967815084",
             "sha1" : "f40aab20fb2f609b5cbc1171c40b66a1445e3773" }
    version = "3.9.5"
    name = "tiff"

    depends = ["zlib", "libjpeg"]

    configure_args = ["--with-jpeg-include-dir=%(prefix)s/include",
                      "--with-jpeg-lib-dir=%(prefix)s/lib"]

