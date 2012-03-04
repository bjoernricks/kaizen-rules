import jam.session

from jam.system import Copy, Mkdirs

class Docbookxml(jam.session.Session):

    url = "http://www.oasis-open.org/docbook/xml/4.2/docbook-xml-4.2.zip"
    hash = { "md5" : "73fe50dfe74ca631c1602f558ed8961f",
             "sha1" : "5e3a35663cd028c5c5fbb959c3858fec2d7f8b9e" }
    version = "4.2"
    name = "docbook-xml"

    src_path = "%(src_dir)s"

    def destroot(self):
        files = ["calstblx.dtd", "catalog.xml", "dbcentx.mod", "dbgenent.mod",
                 "dbhierx.mod", "dbnotnx.mod", "dbpoolx.mod", "docbook.cat",
                 "docbookx.dtd", "soextblx.dtd", "ChangeLog", "README"]
        dirs = ["ent"]

        dest_path = self.dest_path + "/share/xml/docbook/" + self.version
        Mkdirs(dest_path).run()
        for item in files + dirs:
            Copy(self.src_path + "/" + item, dest_path).run()
