import kaizen.rules

class Pythonpsycopg2(kaizen.rules.PythonRules):

    url = "http://pypi.python.org/packages/source/p/psycopg2/psycopg2-%(version)s.tar.gz"
    hash = { "md5" : "639e014ea9ce3aa3306724f12d16d79b",
             "sha1" : "d8a98dbb4fed1a5871c658d2b35fe8c92293086a" }
    version = "2.4.4"
    name = "psycopg2"

    depends = ["postgresql"]
