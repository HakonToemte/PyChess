import socket
import time
from _thread import *
import pickle
from game import Game
server = socket.gethostbyname(socket.gethostname()) # local ip, must be the same as on Network
port = 5555 #elaborate port must be same on Network

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))
s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0

def threaded_client(conn, p, gameId):
    global idCount
    global games
    conn.send(str.encode(str(p)))
    reply = ""
    counter = 0
    timesinceconnected = 0
    t = time.perf_counter()
    t1 = 0
    while True:
        try:

            data = conn.recv(4096).decode()
            if gameId in games:
                game = games[gameId]
                print(len(games), "games")
                if game.bothconnected is True and counter == 0:
                    t1 = time.perf_counter()
                if game.bothconnected is True:
                    timesinceconnected = ((time.perf_counter() - t1))
                    if game.gamestarted is False:
                        counter = 1
                        t = time.perf_counter()
                        if timesinceconnected > 3:
                            game.gamestart()
                    elif game.gamestarted is True:
                        if game.p1Went:
                            game.p2Timer = game.p2Timer - ((time.perf_counter()-t)/2)
                            t = time.perf_counter()
                        elif game.p2Went:
                            game.p1Timer = game.p1Timer - ((time.perf_counter()-t)/2)
                            t = time.perf_counter()
                        if game.p2Timer < 0:
                            game.win(0) #0 is player 1, clientside
                        if game.p1Timer < 0:
                            game.win(1) #1 is player 2, clientside

                if not data:
                    print("no data")
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data == "Start":
                        game.playerconnect(p)
                    elif data != "get":
                        if p == 0:
                            game.p1Timer += (game.timer_increment/2)
                        else:
                            game.p2Timer += (game.timer_increment/2)
                        if data == "Moved":
                            game.gamestart()
                        else:
                            game.play(p, data)
                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount/2 > len(games):
        games[gameId] = Game(gameId, (5*60), 10)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1
    print(idCount, "IDCOUNT")

    start_new_thread(threaded_client, (conn, p, gameId))
