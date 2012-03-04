import jam.session

from jam.system import Copy, Mkdirs

class Docbookxslns(jam.session.Session):

    url = "http://downloads.sourceforge.net/project/docbook/docbook-xsl-ns/%(version)s/docbook-xsl-ns-%(version)s.tar.bz2"
    hash = { "md5" : "e5ba4bf03042761bad3d309c75a77d50",
             "sha1" : "61920b636f247eee4551939876c3c35829b051fd" }
    version = "1.76.1"
    name = "docbook-xsl-ns"


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

