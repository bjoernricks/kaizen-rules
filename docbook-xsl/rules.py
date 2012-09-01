import kaizen.rules

from kaizen.system import Copy, Mkdirs

class Docbookxsl(kaizen.rules.Rules):

    url = "http://downloads.sourceforge.net/project/docbook/docbook-xsl/%(version)s/docbook-xsl-%(version)s.tar.bz2"
    hash = { "md5" : "b5340507cb240cc7ce00632b9c40bff5",
             "sha1" : "dc9fa422c53e0a4f0e32b5c8ec896b39080bc14d" }
    version = "1.76.1"
    name = "docbook-xsl"

    def destroot(self):
        files = ["catalog.xml",
                 "VERSION"]

        dirs = ["common",
                "docsrc",
                "eclipse",
                "epub",
                "extensions",
                "fo",
                "highlighting",
                "html",
                "htmlhelp",
                "images",
                "javahelp",
                "lib",
                "manpages",
                "params",
                "profiling",
                "roundtrip",
                "slides",
                "template",
                "tools",
                "webhelp",
                "website",
                "xhtml",
                "xhtml-1_1",
                ]

        dest_path = self.dest_path + "/share/xsl/" + self.name
        Mkdirs(dest_path).run()
        for item in files + dirs:
            Copy(self.src_path + "/" + item, dest_path).run()
