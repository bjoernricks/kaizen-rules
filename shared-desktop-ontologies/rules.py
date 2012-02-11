import jam.session

class Shareddesktopontologies(jam.session.CMakeSession):

    url = "http://downloads.sourceforge.net/project/oscaf/shared-desktop-ontologies/0.9/shared-desktop-ontologies-%(version)s.tar.bz2"
    hash = { "md5" : "8cd0950dc66eb5fbe560ac7fdb416e04",
             "sha1" : "c5dffbc58a5a694a36f7da4f7806e37cab459722" }
    version = "0.9.0"
    name = "shared-desktop-ontologies"

    depends = ["qt4", "automoc4", "docbook-xsl-ns"]
