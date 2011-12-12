import jam.session

class Asciidoc(jam.session.ConfigureSession):

    url = "http://downloads.sourceforge.net/project/asciidoc/asciidoc/%(version)s/%(version)s-8.6.6.tar.gz"
    hash = { "md5" : "44b872d9c300ffa5a8fe8b3c4d10957c",
             "sha1" : "f43f96d8599c3337baf12df18315ecc0b9e885c7" }
    version = "8.6.6"
    name = "asciidoc"
