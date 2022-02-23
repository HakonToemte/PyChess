class Game:
    def __init__(self, id, playtime, timerincrement):
        self.p1Went = False
        self.p2Went = True
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0
        self.turn = 0
        self.bothconnected= False
        self.gamestarted = False
        self.getrealtime = False
        self.P1Readytostart = False
        self.P2Readytostart = False
        self.playtimep1 = playtime
        self.playtimep2 = playtime
        self.p1Timer = self.playtimep1
        self.p2Timer = self.playtimep2
        self.timer_increment = timerincrement
        self.finished = False
        self.winner = "unkn"

    def get_player_move(self, p):
        """
        :param p: p: [0,1]
        :return:    Move
        """
        #print(self.moves, "MOVES")
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
            self.p2Went = False
        else:
            self.p1Went = False
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def playerconnect(self, p):
        if p == 0:
            self.P1Readytostart = True
            if self.P2Readytostart is True:
                self.bothconnected = True
        elif p == 1:
            self.P2Readytostart = True
            if self.P1Readytostart is True:
                self.bothconnected = True

    def gamestart(self):
        self.gamestarted = True

    def win(self, p):
        self.winner = p

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False

