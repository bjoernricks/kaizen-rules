import os.path
import jam.session

from jam.system import Copy, Configure

class Git(jam.session.ConfigureSession):

    url =  "http://git-core.googlecode.com/files/git-%(version)s.tar.gz"
    hash = { "md5" : "e0b7afcc0e5e43bbb82f85598ae34bd8",
             "sha1" : "df91e2c32d6097ab1c9d0edc56dd8cecb4e9b686" }
    version = "1.7.6.4"
    name = "git"

    depends = ["python", "gettext", "git-manpages"]

    configure_args = [
                      "--with-gitconfig=etc/gitconfig",
                      "--with-gitattributes=etc/gitattributes",
                     ]

    def pre_configure(self):
        Copy(self.src_path, self.build_path).run()

    def post_destroot(self):
        Copy(os.path.join(self.build_path, "contrib", "completion",
                          "git-completion.bash"),
             os.path.join(self.dest_path, "etc",
                          "bash_completion.d", "git")).run()
        Copy(os.path.join(self.session_path, "contrib", "giteditor"),
             os.path.join(self.dest_path, "share", "git",
                          "contrib", "giteditor")).run()
