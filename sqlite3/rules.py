import kaizen.rules

class Sqlite3(kaizen.rules.ConfigureRules):

    url = "http://www.sqlite.org/sqlite-autoconf-3071400.tar.gz"
    hash = { "md5" : "6464d429b1396a8db35864e791673b65",
             "sha1" : "7b429809918201555f4c0fa639183a1c663d3fe0" }
    version = "3.7.14"
    name = "sqlite"

    src_path = "%(src_dir)s/%(name)s-autoconf-3071400"

    configure_cppflags = ["-DSQLITE_ENABLE_FTS3",
                          "-DSQLITE_ENABLE_FTS3_PARENTHESIS",
                          "-DSQLITE_ENABLE_RTREE",
                          "-DSQLITE_ENABLE_UNLOCK_NOTIFY",
                          "-DSQLITE_ENABLE_COLUMN_METADATA",
                          "-DSQLITE_ENABLE_FTS4",
                         ]

    configure_args = ["--enable-readline", "--enable-threadsafe",
                      "--enable-dynamic-extensions",]

