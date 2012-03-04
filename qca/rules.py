import jam.session

from jam.system import Configure, Make

class Qca(jam.session.ConfigureSession):

    url = "http://delta.affinix.com/download/qca/2.0/qca-%(version)s.tar.bz2"
    hash = { "md5" : "fc15bd4da22b8096c51fcfe52d2fa309",
             "sha1" : "9c868b05b81dce172c41b813de4de68554154c60" }
    version = "2.0.3"
    name = "qca"

    build_path = "%(src_path)s"

    configure_args = ["--no-framework"]

    depends = ["qt4"]

    def configure(self):
        # qca's configure doesn't support --src-dir
        args = self.configure_args
        args.append("--prefix=" + self.prefix)
        configure = Configure(args, self.configure_path, self.build_path,
                             self.debug)
        if self.configure_cc:
            configure.set_cc(self.configure_cc)
        if self.configure_cpp:
            configure.set_cpp(self.configure_cpp)
        if self.configure_cflags:
            configure.set_cflags(self.configure_cflags)
        if self.configure_cppflags:
            configure.set_cppflags(self.configure_cppflags)
        if self.configure_ldflags:
            configure.set_ldflags(self.configure_ldflags)
        if self.configure_libs:
            configure.set_libs(self.configure_libs)
        if self.configure_cxx:
            configure.set_cxx(self.configure_cxx)
        if self.configure_cxxflags:
            configure.set_cxxflags(self.configure_cxxflags)
        configure.run()

    def destroot(self):
        #qmake sucks! why not supporting DESTDIR???
        args = ["INSTALL_ROOT=" + self.dest_dir, "install"]
        Make(self.build_path, self.debug).run(args)

    def distclean(self):
        pass
