import jam.session

class Sqlite3(jam.session.ConfigureSession):

    url = "http://www.sqlite.org/sqlite-autoconf-3070701.tar.gz"
    hash = { "md5" : "554026fe7fac47b1cf61c18d5fe43419",
             "sha1" : "ee405037ab49f46f657a9b314e66eec6009d5fc6" }
    version = "3.7.7.1"
    name = "sqlite"

    src_path = "%(src_dir)s/%(name)s-autoconf-3070701"

    configure_cppflags = ["-DSQLITE_ENABLE_FTS3",
                          "-DSQLITE_ENABLE_FTS3_PARENTHESIS",
                          "-DSQLITE_ENABLE_RTREE", 
                          "-DSQLITE_ENABLE_UNLOCK_NOTIFY",
                          "-DSQLITE_ENABLE_COLUMN_METADATA",
                          "-DSQLITE_ENABLE_FTS4",
                         ] 

    configure_args = ["--enable-readline", "--enable-threadsafe",
                      "--enable-dynamic-extensions",]

