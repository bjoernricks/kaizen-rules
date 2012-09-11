import kaizen.rules

class Docbook2x(kaizen.rules.ConfigureRules):

    url = "http://downloads.sourceforge.net/project/docbook2x/docbook2x/%(version)s/docbook2X-%(version)s.tar.gz"
    hash = { "md5" : "b9b76a6af198c4f44574cfd17a322f01",
             "sha1" : "7dc34d420f8aae2a0c0cdb39f52146ce005bf902" }
    version = "0.8.8"
    name = "docbook2x"

    depends = ["libxslt", "perl-xml-sax"]

    src_path = "%(src_dir)s/docbook2X-%(version)s"

    configure_args = ["--with-xslt-processor=libxslt"]
