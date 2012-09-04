import kaizen.rules

class Bzip2(kaizen.rules.Rules):

    url = "http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz"
    hash = { "md5" : "00b516f4704d4a7cb50a1d97e6e8e15b",
             "sha1" : "3f89f861209ce81a6bab1fd1998c0ef311712002" }
    version = "1.0.6"
    name = "bzip2"

    # not ready yet: bzip2 uses only a Makefile
