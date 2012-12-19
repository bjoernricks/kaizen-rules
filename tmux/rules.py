import kaizen.rules

class Tmux(kaizen.rules.ConfigureRules):

    url = "http://downloads.sourceforge.net/project/tmux/tmux/tmux-%(version)s/tmux-%(version)s.tar.gz"
    hash = { "md5" : "2c48fb9beb22eedba7a5de3b78dd0c03",
             "sha1" : "ee6942a1bc3fc650036f26921d80bc4b73d56df6" }
    version = "1.7"
    name = "tmux"

    depends = ["libevent", "ncurses"]
