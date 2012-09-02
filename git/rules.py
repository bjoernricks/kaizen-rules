import os.path
import kaizen.rules

from kaizen.system import Copy, Configure

class Git(kaizen.rules.ConfigureRules):

    url =  ["https://github.com/git/git/tarball/v%(version)s",
            "git-%(version)s.tar.gz"]
    hash = { "md5" : "df20675abd4f9ae44a72c3b5c22a7243",
             "sha1" : "b5f61c57163208d6ab4e1926bfa070815bef3783" }
    version = "1.7.12"
    name = "git"

    depends = ["python", "gettext", "git-manpages", "perl", "openssl",
               "libcurl", "zlib", "libexpat"]

    src_path = "%(src_dir)s/git-git-14d20a7"

    configure_args = [
                      "--with-gitconfig=etc/gitconfig",
                      "--with-gitattributes=etc/gitattributes",
                     ]

    def pre_configure(self):
        Copy(self.src_path + "/*", self.build_path).run()

    def post_destroot(self):
        Copy(os.path.join(self.build_path, "contrib", "completion",
                          "git-completion.bash"),
             os.path.join(self.dest_path, "etc",
                          "bash_completion.d", "git")).run()
        Copy(os.path.join(self.rules_path, "contrib", "giteditor"),
             os.path.join(self.dest_path, "share", "git",
                          "contrib", "giteditor")).run()

    def distclean(self):
        Delete(self.build_path).run()
