import jam.session

class Taglib(jam.session.CMakeSession):

    url = "http://developer.kde.org/~wheeler/files/src/taglib-1.7.tar.gz"
    hash = { "md5" : "6a7e312668f153fa905a81714aebc257",
             "sha1" : "5138e1665182bc2171e298ff31518c9ad72ddf23" }
    version = "1.7"
    name = "taglib"

    configure_args = ["-DWITH_ASF=ON",
                      "-DWITH_MP4=ON",
                      "-DCMAKE_BUILD_TYPE=Release",
                      ]

    depends = ["zlib"]
