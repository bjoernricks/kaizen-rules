import jam.session

class Raptor2(jam.session.ConfigureSession):

    url = "http://download.librdf.org/source/raptor2-%(version)s.tar.gz"
    hash = { "md5" : "1f07af81cbe3cf1bf0d1d250b18d9f93",
             "sha1" : "978f61579370914f22e162407539b8faa9891ed0" }
    version = "2.0.6"
    name = "raptor2"

    depends = ["libxml2", "pkg-config", "libxslt", "libcurl"]
