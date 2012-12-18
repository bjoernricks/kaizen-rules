import kaizen.rules

from kaizen.system.patch import Quilt

class Liblastfm(kaizen.rules.CMakeRules):

    url = ["https://github.com/eartle/liblastfm/tarball/%(version)s",
           "liblastfm-%(version)s.tar.gz"]
    hash = { "md5" : "0e724473cb39be89230fe27e285ce5f4",
             "sha1" : "3057babb1375b505b139e425b2db8b9fc5d5fdcb" }
    version = "1.0.1"
    name = "liblastfm"

    patch_cmd = Quilt

    src_path = "%(src_dir)s/eartle-liblastfm-9b4efb5"

    depends = ["qt4", "fftw", "libsamplerate"]
