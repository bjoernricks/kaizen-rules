import kaizen.rules

class Graphviz(kaizen.rules.ConfigureRules):

    url = "http://www.graphviz.org/pub/graphviz/stable/SOURCES/graphviz-2.28.0.tar.gz"
    hash = { "md5" : "8d26c1171f30ca3b1dc1b429f7937e58",
             "sha1" : "4725d88a13e071ee22e632de551d4a55ca08ee7d" }
    version = "2.28.0"
    name = "graphviz"

    # uncomment to set path to source directory
    # default is %(src_dir)s/%(name)s-%(version)s
    # src_path = ""

    # uncomment to set path to build directory (normally not necessary)
    # build_path = ""

    # uncomment to pass additional parameters to configure script
    # configure_args = [""]

    # uncomment to pass additional parameters to make
    # build_args = [""]

    # uncomment to add additonal patches
    # all patches will be copied to %(downloadroot)s/%(rules)s/patches
    # e.g. patches = ["01-patch.diff", "http://url.com/remotepatch.diff",
    #                ["http://url.com/abc.diff", "localname.diff"]]
    # patches = [""]

    # uncomment to add a dependency on an other rules
    # depends = [""]
