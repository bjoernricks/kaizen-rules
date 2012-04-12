import jam.session

class Freetype(jam.session.ConfigureSession):

    url = "http://downloads.sourceforge.net/project/freetype/freetype2/%(version)s/freetype-%(version)s.tar.gz"
    hash = { "md5" : "c15f6dc8ed190d67b89ae09aaf7896b4",
             "sha1" : "a96fcfc8e041d54c961322360d19fc7adf703286" }
    version = "2.4.9"
    name = "freetype"

    depends = ["bzip2", "zlib"]
