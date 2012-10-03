import kaizen.rules

class Fftw(kaizen.rules.ConfigureRules):

    url = "ftp://ftp.fftw.org/pub/fftw/fftw-%(version)s.tar.gz"
    hash = { "md5" : "6977ee770ed68c85698c7168ffa6e178",
             "sha1" : "11a8c31186ff5a7d686a79a3f21b2530888e0dc2" }
    version = "3.3.2"
    name = "fftw"

    configure_args = ["--enable-threads",
                      "--disable-fortran",
                      "--enable-shared",
                      "--enable-sse2"]

