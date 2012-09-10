import kaizen.rules

class Tmux(kaizen.rules.ConfigureRules):

    url = "http://downloads.sourceforge.net/project/tmux/tmux/tmux-%(version)s/tmux-%(version)s.tar.gz"
    hash = { "md5" : "3e37db24aa596bf108a0442a81c845b3",
             "sha1" : "8756f6bcecb18102b87e5d6f5952ba2541f68ed3" }
    version = "1.6"
    name = "tmux"

    depends = ["libevent", "ncurses"]
