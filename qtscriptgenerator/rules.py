import jam.session

from jam.system import Command, Make, Copy, Mkdirs, Quilt

class Qtscriptgenerator(jam.session.MakeSession):

    url = "http://qtscriptgenerator.googlecode.com/files/qtscriptgenerator-src-%(version)s.tar.gz"
    hash = { "md5" : "9f82b0aa212f7938de37df46cd27165c",
             "sha1" : "4c1078f26b196156e857c17c9d11a66cfea66f00" }
    version = "0.2.0"
    name = "qtscriptgenerator-src"

    depends = ["qt4", "phonon"]

    patchsystem = Quilt

    build_path = "%(src_path)s"

    build_args = ["PREFIX=%(prefix)s", "BUILDDIR=%(build_path)s"]

    def destroot(self):
        bin_dir = self.dest_path + "/bin"
        plugin_dir = self.dest_path + "/lib/qt4/"
        Mkdirs(bin_dir).run()
        Mkdirs(plugin_dir).run()
        Copy(self.build_path + "/plugins", plugin_dir).run()
        Copy(self.build_path + "/generator/generator",
             bin_dir + "/qs_generator").run()
        Copy(self.build_path + "/qtbindings/qs_eval/qs_eval", bin_dir).run()
