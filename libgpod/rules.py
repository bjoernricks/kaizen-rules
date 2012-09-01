import kaizen.rules

from kaizen.system import Quilt, Delete

class Libgpod(kaizen.rules.ConfigureRules):

    url = "http://downloads.sourceforge.net/project/gtkpod/libgpod/libgpod-0.8/libgpod-%(version)s.tar.bz2"
    hash = { "md5" : "ff0fd875fa08f2a6a49dec57ce3367ab",
             "sha1" : "f9ba70cd6f00ae59cdc6a43cc72c409a4d27606e" }
    version = "0.8.2"
    name = "libgpod"

    patchsystem = Quilt
    depends = ["libxml2", "python", "taglib", "perl", "gettext", "libplist",
               "pkg-config", "glib2", "gdk-pixbuf", "sqlite3"]

    def post_destroot(self):
        Delete(self.destroot_path + "/lib").run()
        Delete(self.destroot_path + "/temp").run()
