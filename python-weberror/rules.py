import jam.session

class Pythonweberror(jam.session.PythonSession):

    url = "http://pypi.python.org/packages/source/W/WebError/WebError-0.10.3.tar.gz"
    hash = { "md5" : "84b9990b0baae6fd440b1e60cdd06f9a",
             "sha1" : "6c8b4e77d93e1234cf1ef6d6b0dcad0a91a1af55" }
    version = "0.10.3"
    name = "WebError"

    # jam.session.PythonSession already depends on python
    # depends = ["python"]

    # uncomment to set path to source directory
    # default is %(src_dir)s/%(name)s-%(version)s
    # src_path = ""

    # uncomment to set path to build directory (normally not necessary)
    # build_path = ""

    # uncomment to pass additional parameters to setup.py script
    # build_args = [""]

    # uncomment to add additonal patches 
    # all patches will be copied to %(downloadroot)s/%(session)s/patches
    # e.g. patches = ["01-patch.diff", "http://url.com/remotepatch.diff"]
    # patches = [""]
