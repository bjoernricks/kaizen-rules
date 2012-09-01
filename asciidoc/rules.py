import kaizen.rules

from kaizen.system import Copy

class Asciidoc(kaizen.rules.ConfigureRules):

    url = "http://downloads.sourceforge.net/project/asciidoc/asciidoc/%(version)s/asciidoc-%(version)s.tar.gz"
    hash = { "md5" : "44b872d9c300ffa5a8fe8b3c4d10957c",
             "sha1" : "f43f96d8599c3337baf12df18315ecc0b9e885c7" }
    version = "8.6.6"
    name = "asciidoc"

    def pre_configure(self):
        Copy(self.src_path + "/*", self.build_path).run()

    def distclean(self):
        pass
