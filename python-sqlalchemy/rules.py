import kaizen.rules

class Pythonsqlalchemy(kaizen.rules.PythonRules):

    url = "http://downloads.sourceforge.net/project/sqlalchemy/sqlalchemy/0.7.2/SQLAlchemy-%(version)s.tar.gz"
    hash = { "md5" : "234494800f2a0ac3ad7c06e0ffa4641e",
             "sha1" : "e41e822ba4b728ae139532d84bbb8b5043fb9116" }
    version = "0.7.2"
    name = "SQLAlchemy"
