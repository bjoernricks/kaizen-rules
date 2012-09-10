import kaizen.rules

class Libevent(kaizen.rules.ConfigureRules):

    url = "https://github.com/downloads/libevent/libevent/libevent-%(version)s-stable.tar.gz"
    hash = { "md5" : "94270cdee32c0cd0aa9f4ee6ede27e8e",
             "sha1" : "20bb4a1a296ac93c08dfc32ae19ab874cab67a0c" }
    version = "2.0.20"
    name = "libevent"

    src_path = "%(src_dir)s/libevent-%(version)s-stable"
