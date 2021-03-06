import os.path
import kaizen.rules

from kaizen.system import Copy, Configure, Delete

class Git(kaizen.rules.ConfigureRules):

    url = "http://git-core.googlecode.com/files/git-%(version)s.tar.gz"
    hash = { "md5" : "ceb1a6b17a3e33bbc70eadf8fce5876c",
             "sha1" : "42ec1037f1ee5bfeb405710c83b73c0515ad26e6" }
    version = "1.7.12"
    name = "git"

    depends = ["python", "gettext", "git-manpages", "perl", "openssl",
               "libcurl", "zlib", "libexpat"]

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
        Copy(os.path.join(self.build_path, "contrib", "completion",
                          "git-prompt.sh"),
             os.path.join(self.dest_path, "etc",
                          "bash_completion.d", "git-prompt")).run()
        Copy(os.path.join(self.rules_path, "contrib", "giteditor"),
             os.path.join(self.dest_path, "share", "git",
                          "contrib", "giteditor")).run()

    def distclean(self):
        Delete(self.build_path).run()
