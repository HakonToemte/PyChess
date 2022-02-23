import pygame
from network import Network
import ast
import time

pygame.font.init()

width = 1000
height =1000

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")



class Timer:
    def __init__(self, textminutes, textseconds, x, y, color, width, height, textcolor):
        self.text = textminutes
        self.text2 = textseconds
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.textcolor = textcolor

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsansms", round(height/16))
        text = self.text
        text2 = self.text2
        text3 = font.render(":", 1, (177, 192, 232), False)
       # print(game.p1Timer, "Text")
        #text2 = self.text % 60
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2)*4,
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))
        win.blit(text2, (self.x + round(self.width / 2) - round(text.get_width() / 2)*(1/4),
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))
        win.blit(text3, (self.x + round(self.width / 2) - round(text.get_width() / 2)*2,
                         self.y + round(self.height / 2) - round(text.get_height() / 2)))



class Button:
    def __init__(self, text, x, y, color, width, height, name, special_x, special_y,text2nd, textcolor):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.name = name
        self.special_x = special_x
        self.special_y = special_y
        self.text2nd = text2nd
        self.textcolor = textcolor
        self.enpassant = False

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsansms", round(height/32))
        text = font.render(self.text, 1, self.textcolor)
        text2nd = font.render(self.text2nd, 1, self.textcolor)
        if self.special_x == 0 and self.special_y == 0:
            win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2),
                            self.y + round(self.height/2) - round(text.get_height()/2)))
        else:
            if self.special_x != 0 and self.special_y != 0:
                win.blit(text, (self.x + self.special_x, self.y + self.special_y))
            elif self.special_x != 0:
                win.blit(text, (self.x + self.special_x, self.y + round(self.height/2) - round(text.get_height()/2)))
            elif self.special_y != 0:
                win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), (self.y + self.special_y)))
        if self.text2nd != "0":
            win.blit(text2nd, (self.x + drawingcell[63].special_x, self.y + drawingcell[63].special_y)) #Kun for nederst til venstre hvor det er både bokstav og tall

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x - (cellwidth-self.width)/2 <= x1 <= self.x +(cellwidth - (cellwidth-self.width)/2) and \
                self.y - (cellheight-self.height)/2 <= y1 <= self.y+(cellheight - (cellheight-self.height)/2):
            return True
        else:
            return False




class Menu:
    def __init__(self, x, y, color, width, height, row, collumn):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.row = row
        self.collumn = collumn
        self.piecesize = 45

    def draw_menu(self, win):
        self.x = 0
        self.y = 0
        for piece in drawingpiece:
            if drawingpiece[piece].piece == "Pawn":
                if drawingpiece[piece].name[1] == 8 and player == 0:
                    self.x = drawingpiece[piece].x
                    self.y = drawingpiece[piece].y
                    if self.x + self.width > width:
                        self.x = width - self.width
                    elif self.y + self.height > height:
                        self.y = height - self.height
                elif drawingpiece[piece].name[1] == 1 and player == 1:
                    self.x = drawingpiece[piece].x
                    self.y = drawingpiece[piece].y
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        for choice in range(4):
            # 1 COLLUMN
            MenuChoices[choice+1].x = self.x
            MenuChoices[choice+1].y = self.y + (MenuChoices[choice+1].height * choice)
            # BOX TYPE
            #if choice <= 2:
            #    MenuChoices[choice+1].x = self.x + ((MenuChoices[choice+1].width) *choice)
            #    MenuChoices[choice+1].y = self.y
           # else:
            #    MenuChoices[choice+1].x = self.x
            #    MenuChoices[choice+1].y = self.y + ((MenuChoices[choice+1].height))

            #Draw
            win.blit(MenuChoices[choice+1].pieceimg, (MenuChoices[choice+1].x, MenuChoices[choice+1].y))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x - (cellwidth-self.width)/2 <= x1 <= self.x +(cellwidth - (cellwidth-self.width)/2) and \
                self.y - (cellheight-self.height)/2 <= y1 <= self.y+(cellheight - (cellheight-self.height)/2):
            return True
        else:
            return False

class MenuPiece:
    def __init__(self, x, y, pieceimg, width, height, piece):
        self.x = x
        self.y = y
        self.pieceimg = pieceimg
        self.width = width
        self.height = height
        self.piece = piece

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x - (cellwidth-self.width)/2 <= x1 <= self.x +(cellwidth - (cellwidth-self.width)/2) and \
                self.y - (cellheight-self.height)/2 <= y1 <= self.y+(cellheight - (cellheight-self.height)/2):
            return True
        else:
            return False


class Piece:
    def __init__(self, x, y, color, piece, width, height, name, pieceimage):
        self.x = x
        self.y = y
        self.color = color
        self.piece = piece
        self.width = width
        self.height = height
        self.name = name
        self.pieceimage = pieceimage
        self.moved = 0

    def drop(self, cell, player1Went, player2Went, currentplayer):
        t = time.perf_counter()
        game = n.send("get")
        movecastle = ((0, 0), (0, 0))
        pawnupgrade = "Nothing"
        check = 0
        kingspot = -1
        print("dropping1")
        if (player2Went and currentplayer == 0 and self.color == white) or (player1Went and currentplayer == 1 and
                                                                            self.color == black):
            #print(time.perf_counter()-t, "time1")
            t = time.perf_counter()
            if cell and cell.name != self.name and self.find_if_legal_move(self.name, cell.name, currentplayer, drawingpiece,0,self,cell.name):
                legal_move = self.find_if_legal_move(self.name, cell.name, currentplayer, drawingpiece, 0, self,
                                                     cell.name)
                #print("dropping2")
                for piece in drawingpiece:
                    if drawingpiece[piece].piece == "King":
                        if currentplayer == 0:
                            if drawingpiece[piece].color == white:
                                kingspot = drawingpiece[piece].name
                        if currentplayer == 1:
                            if drawingpiece[piece].color == black:
                                kingspot = drawingpiece[piece].name
                if kingspot != -1:
                    if currentplayer == 0:
                        for piece in drawingpiece:
                            if drawingpiece[piece].name != cell.name:
                                if drawingpiece[piece].color == black:
                                    if drawingpiece[piece].find_if_legal_move(drawingpiece[piece].name, kingspot, currentplayer, drawingpiece,1,self, cell.name):
                                        check = 1
                    if currentplayer == 1:
                        for piece in drawingpiece:
                            if drawingpiece[piece].name != cell.name:
                                if drawingpiece[piece].color == white:
                                    if drawingpiece[piece].find_if_legal_move(drawingpiece[piece].name, kingspot, currentplayer, drawingpiece,1 , self, cell.name):
                                        check = 1
                if self.piece == "King" and self.moved == 0:
                    if self.name[0] == cell.name[0]+2 or self.name[0] == cell.name[0]-2:
                        for piece in drawingpiece:
                            kingspot_plus1 = (self.name[0]+1, self.name[1])
                            kingspot_minus1 = (self.name[0]-1, self.name[1])
                            if currentplayer == 0:
                                if drawingpiece[piece].color == black:
                                    if drawingpiece[piece].find_if_legal_move(drawingpiece[piece].name, kingspot,
                                                                              currentplayer, drawingpiece, 1, self,
                                                                              kingspot):
                                        check = 1
                                    if self.name[0] == cell.name[0]-2:
                                        if drawingpiece[piece].find_if_legal_move(drawingpiece[piece].name, kingspot_plus1,currentplayer,drawingpiece,0, self, cell.name):
                                            check = 1
                                    if self.name[0] == cell.name[0]+2:
                                        if drawingpiece[piece].find_if_legal_move(drawingpiece[piece].name, kingspot_minus1,currentplayer,drawingpiece,0, self, cell.name):
                                            check = 1
                            if currentplayer == 1:
                                if drawingpiece[piece].color == white:
                                    if drawingpiece[piece].find_if_legal_move(drawingpiece[piece].name, kingspot,
                                                                              currentplayer, drawingpiece, 1, self,
                                                                              kingspot):
                                        check = 1
                                    if self.name[0] == cell.name[0]-2:
                                        if drawingpiece[piece].find_if_legal_move(drawingpiece[piece].name, kingspot_plus1,currentplayer,drawingpiece,0, self, cell.name):
                                            check = 1
                                    if self.name[0] == cell.name[0]+2:
                                        if drawingpiece[piece].find_if_legal_move(drawingpiece[piece].name, kingspot_minus1,currentplayer,drawingpiece,0, self, cell.name):
                                            check = 1

                #print(kingspot, " kingspot")
                #print(time.perf_counter()-t, "time2")
                #if check == 0:
                #print(check, " check")
                #print(game.bothconnected, "BOTHCONNECT")
                if game.bothconnected is True:
                    if check == 0:
                        #print(self.name, " Last")
                        heim = self.name
                        move = (self.name, cell.name) + movecastle
                        self.x = cell.x + cellwidth / 4
                        self.y = cell.y + cellheight / 4
                        self.name = cell.name
                        self.moved = 1
                        n.send("Moved")
                        print(legal_move, "legal")
                        if legal_move[1] != -1:
                            print("CAP1")
                            capture_piece(legal_move[1])
                        #print(move , " 3")
                        # sends move
                        if legal_move[0] and legal_move[2] == 1: # legal_move = (True, piece2cap, castle, rook_to_move, rook_move_to)
                            movecastle = (legal_move[3].name, legal_move[4].name)
                            move = (heim, cell.name) + movecastle
                            legal_move[3].x = legal_move[4].x + cellwidth / 4
                            legal_move[3].y = legal_move[4].y + cellheight / 4
                            legal_move[3].name = legal_move[4].name
                        if self.piece == "Pawn":
                            if currentplayer == 0:
                                if self.name[1] == 8:
                                    menu = 1
                                    while menu:
                                        self.pawn_upgrade()
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                pos = pygame.mouse.get_pos()
                                                if event.button == 1:
                                                    for piece in MenuChoices:
                                                        if MenuChoices[piece].click(pos) and game.connected():
                                                            menu = 0
                                                            pawnupgrade = MenuChoices[piece].piece
                                                            Transform_img_to = MenuChoices[piece].pieceimg
                                                            self.piece = pawnupgrade
                                                            self.pieceimage = Transform_img_to
                                                            n.send(str(move)+pawnupgrade)

                                else:
                                    n.send(str(move)+pawnupgrade)
                                    game.gamestarted = True

                            else:
                                if self.name[1] == 1:
                                    menu = 1
                                    while menu:
                                        self.pawn_upgrade()
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                pos = pygame.mouse.get_pos()
                                                if event.button == 1:
                                                    for piece in MenuChoices:
                                                        if MenuChoices[piece].click(pos) and game.connected():
                                                            menu = 0
                                                            pawnupgrade = MenuChoices[piece].piece
                                                            Transform_img_to = MenuChoices[piece].pieceimg
                                                            self.piece = pawnupgrade
                                                            self.pieceimage = Transform_img_to
                                                            n.send(str(move) + pawnupgrade)

                                else:
                                    n.send(str(move)+pawnupgrade)
                                    game.gamestarted = True

                        else:
                            n.send(str(move)+pawnupgrade)
                            game.gamestarted = True

                    else: #go home, check is in play
                        print("Wayou42")
                        self.x = drawingcell[name_to_cell(self.name, currentplayer)].x + cellwidth / 4
                        self.y = drawingcell[name_to_cell(self.name, currentplayer)].y + cellwidth / 4
                else:# go home, both players havent connected
                    print("Wayout3")
                    self.x = drawingcell[name_to_cell(self.name, currentplayer)].x + cellwidth / 4
                    self.y = drawingcell[name_to_cell(self.name, currentplayer)].y + cellwidth / 4
            else: #go home,invalid move
                print("Wayout2")
                self.x = drawingcell[name_to_cell(self.name, currentplayer)].x + cellwidth/4
                self.y = drawingcell[name_to_cell(self.name, currentplayer)].y + cellwidth/4
        else:
            print("wayout1")
            self.x = drawingcell[name_to_cell(self.name, currentplayer)].x + cellwidth / 4
            self.y = drawingcell[name_to_cell(self.name, currentplayer)].y + cellwidth / 4
        #vi har gjort trekket vårt, se etter motstanders trekk
        global updated
        updated = False
    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x - (cellwidth-self.width)/2 <= x1 <= self.x +(cellwidth - (cellwidth-self.width)/2) and \
                self.y - (cellheight-self.height)/2 <= y1 <= self.y+(cellheight - (cellheight-self.height)/2):
            return True
        else:
            return False
    def pawn_upgrade(self):
        game = n.send("get")
        width = 100
        height = 100
        row = 3
        collumn = 3
        pygame.time.delay(0)
        pygame.display.update()
        redrawWindow(win, game, player, 1)
    def movingpiece(self):
        game = n.send("get")
        cursor = pygame.mouse.get_pos()
        self.x = cursor[0] - self.width/2
        self.y = cursor[1] - self.height/2
        redrawWindow(win, game, player, 0)
    def find_square(self):
        for cell in drawingcell:
            if drawingcell[cell].x <= self.x + self.width/2 <= drawingcell[cell].x + drawingcell[cell].width:
                if drawingcell[cell].y <= self.y + self.height/2 <= drawingcell[cell].y + drawingcell[cell].height:
                    return drawingcell[cell]
    def update_enemy_move(self, home, newcell, pawnupgrade, player):
        pieceonspot = 0
        global updated
        if newcell:
            # En passant rule
            #resets every turn
            for cell in drawingcell:
                drawingcell[cell].enpassant = False
            if self.piece == "Pawn": #enemy pawn moved forward 2 steps
                if player == 0:
                    if self.name[1]-2 == drawingcell[newcell].name[1]:
                        drawingcell[newcell-8].enpassant = True
                if player == 1:
                    if self.name[1]+2 == drawingcell[newcell].name[1]:
                        drawingcell[newcell-8].enpassant = True
            r = dict(drawingpiece)
            for piece in r:
                pieceoncell = name_to_cell(r[piece].name, player)
                if pieceoncell == newcell:
                    pieceonspot = 1
                    print("CAP2")
                    capture_piece(piece)
            #if enemy used en passant
            if self.piece == "Pawn":
                if self.name[0] != drawingcell[newcell].name[0] and pieceonspot == 0:
                    print("en passant")
                    for piece in r:
                        if r[piece].name == drawingcell[newcell-8].name:
                            print("CAP3")
                            capture_piece(piece)
            if self.name != drawingcell[newcell].name:
                self.x = drawingcell[newcell].x + cellwidth / 4
                self.y = drawingcell[newcell].y + cellheight / 4
                self.name = drawingcell[newcell].name
                self.moved = 1
            if pawnupgrade != "Nothing":
                self.piece = pawnupgrade
                if self.color == white:
                    if pawnupgrade == "Bishop":
                        self.pieceimage = WBishop
                    elif pawnupgrade == "Knight":
                        self.pieceimage = WKnight
                    elif pawnupgrade == "Rook":
                        self.pieceimage = WRook
                    elif pawnupgrade == "Queen":
                        self.pieceimage = WQueen
                if self.color == black:
                    if pawnupgrade == "Bishop":
                        self.pieceimage = BBishop
                    elif pawnupgrade == "Knight":
                        self.pieceimage = BKnight
                    elif pawnupgrade == "Rook":
                        self.pieceimage = BRook
                    elif pawnupgrade == "Queen":
                        self.pieceimage = BQueen
        updated = True

    def find_if_legal_move(self, home, target, currentplayer, board, test, testpiece, test_target):
        true = 1
        rook_move_to = 0
        rook_to_move = 0
        x_diff = 0
        piece2destroy = -1
        test_home = testpiece.name
        castle = 0
        if test == 1:
            for piece in drawingpiece:
                if drawingpiece[piece].name == test_target:
                    piece2destroy = piece
            testpiece.name = test_target
            currentplayer = currentplayer +1
            currentplayer = currentplayer % 2
            if testpiece.piece == "King":
                target = testpiece.name
        piece2cap = -1
        #print(target, " kingspiot")
        r = dict(drawingpiece)
        if currentplayer == 0:
            if self.piece == "Pawn": #pawn logic
                if home[0] != target[0]: #not going straight, can only attack if there are enemies
                    true = 0
                    if home[0] == target[0]+1 or home[0] == target[0]-1:
                        if home[1] == target[1] - 1:
                            for piece in r:
                                if r[piece].name == target and r[piece].color == black:
                                    true = 1
                                    piece2cap = piece
                            if drawingcell[name_to_cell(target, currentplayer)].enpassant is True:
                                true = 1
                                for piece in r:
                                    if r[piece].name[1]+1 == target[1] and r[piece].name[0] == target[0]:
                                        piece2cap = piece
                else:
                    if home[1] == target[1]-1:
                        true = 1
                        for piece in r:
                            if r[piece].name == target:
                                true = 0
                    elif home[1] == target[1] - 2 and self.moved == 0:
                        true = 1
                        for piece in r:
                            if r[piece].name == target:
                                true = 0
                            if r[piece].name[0] == home[0] and r[piece].name[1] == home[1]+1:
                                true = 0
                    else:
                        true = 0
            elif self.piece == "Knight": #Knight logic
                if home[0] == target[0]:
                    true = 0
                else:
                    if home[0] == target[0]-1 or home[0] == target[0]+1:
                        if home[1] == target[1] -2 or home[1] == target[1] +2:
                            for piece in r:
                                if r[piece].name == target:
                                    if r[piece].color == black:
                                        true = 1
                                        piece2cap = piece
                                    else:
                                        true = 0
                        else:
                            true = 0
                    elif home[0] == target[0] -2 or home[0] == target[0]+2:
                        if home[1] == target[1]-1 or home[1] == target[1]+1:
                            for piece in r:
                                if r[piece].name == target:
                                    if r[piece].color == black:
                                        true = 1
                                        piece2cap = piece
                                    else:
                                        true = 0
                        else:
                            true = 0
                    else:
                        true = 0
            elif self.piece == "Bishop":
                x_diff = target[0]-home[0]
                y_diff = target[1]-home[1]
                gonnacapture = 0
                piecetocap = -1
                if home[0] == target[0]:
                    true = 0
                elif abs(x_diff) != abs(y_diff):
                    true = 0
                else:
                    for piece in r:
                        if r[piece].name == target:
                            if r[piece].color == black:
                                gonnacapture = 1
                                piece2cap = piece
                            else:
                                true = 0
                        else:
                            for i in range(1, abs(x_diff)):
                                if r[piece].name[0] == target[0] - (sign(x_diff)*i) and r[piece].name[1] == target[1] - \
                                        (sign(y_diff)*i):
                                    true = 0
                                    gonnacapture = 0
            elif self.piece == "Rook":
                x_move = target[0]-home[0]
                y_move = target[1]-home[1]
                pieceintheway = 0
                going2capture = 0
                piece2cap = -1
                if (x_move != 0 and y_move != 0) or (x_move == 0 and y_move == 0):
                    true = 0
                else:
                    if x_move != 0:
                        for piece in r:
                            for i in range(1, abs(x_move)):
                                if r[piece].name[0] == target[0]-(sign(x_move)*i) and r[piece].name[1] == target[1]:
                                    true = 0
                                    pieceintheway = 1
                            if r[piece].name == target:
                                if r[piece].color == black:
                                    going2capture = 1
                                    piece2cap = piece
                                else:
                                    true = 0
                    elif y_move != 0:
                        for piece in r:
                            for i in range(1, abs(y_move)):
                                if r[piece].name[1] == target[1]-(sign(y_move)*i) and r[piece].name[0]== target[0]:
                                    true = 0
                                    pieceintheway = 1
                            if r[piece].name == target:
                                if r[piece].color == black:
                                    going2capture = 1
                                    piece2cap = piece
                                else:
                                    true = 0
            elif self.piece == "Queen":
                true = 0
                pieceintheway = 0
                piece2cap = -1
                target_is_yourpiece = 0
                x_move = target[0] - home[0]
                y_move = target[1] - home[1]
                if (home[0] == target[0] or home[1] == target[1]) and not(home[0] == target[0] and home[1] == target[1]):
                    if home[0] != target[0]:
                        for piece in r:
                            for i in range(1, abs(x_move)):
                                if r[piece].name[0] == target[0]-(sign(x_move)*i) and r[piece].name[1] == target[1]:
                                    pieceintheway = 1
                            if pieceintheway == 0:
                                if r[piece].name == target:
                                    if r[piece].color == black:
                                        piece2cap = piece
                                    else:
                                        target_is_yourpiece = 1
                                        true = 0
                        if pieceintheway == 0 and target_is_yourpiece == 0:
                            true = 1
                    if home[1] != target[1]:
                        for piece in r:
                            for i in range(1, abs(y_move)):
                                if r[piece].name[1] == target[1]-(sign(y_move)*i) and r[piece].name[0] == target[0]:
                                    pieceintheway = 1
                            if pieceintheway == 0:
                                if r[piece].name == target:
                                    if r[piece].color == black:
                                        piece2cap = piece
                                    else:
                                        target_is_yourpiece = 1
                                        true = 0
                        if pieceintheway == 0 and target_is_yourpiece == 0:
                            true = 1
                elif home[0] != target[0] and home[1] != target[1]:
                    if abs(x_move) == abs(y_move):
                        for piece in r:
                            for i in range(1, abs(x_move)):
                                if r[piece].name[0] == target[0] - (sign(x_move) * i) and r[piece].name[1] == target[1] - \
                                        (sign(y_move) * i):
                                    pieceintheway = 1
                            if pieceintheway == 0:
                                if r[piece].name == target:
                                    if r[piece].color == black:
                                        piece2cap = piece
                                    else:
                                        target_is_yourpiece = 1
                                        true = 0
                        if pieceintheway == 0 and target_is_yourpiece == 0:
                            true = 1
            elif self.piece == "King":
                x_diff = target[0]-home[0]
                castle = 0
                y_diff = target[1]-home[1]
                pieceintheway = 0
                target_is_yourpiece = 0
                piece2cap = -1
                if abs(x_diff) > 1 or abs(y_diff) > 1:
                    true = 0
                    if (x_diff == 2 or x_diff == -2) and (y_diff == 0) and (self.moved == 0):
                        if (x_diff == 2 and drawingpiece[63].moved == 0) or (x_diff == -2 and drawingpiece[56].moved == 0):
                            true = 1
                        for piece in r:
                            if x_diff == 2:
                                if (r[piece].name[0] == home[0] + 1 or r[piece].name[0] == home[0] + 2) and r[piece].name[1] == home[1]:
                                    true = 0
                            if x_diff == -2:
                                if (r[piece].name[0] == home[0] - 1 or r[piece].name[0] == home[0] - 2 or r[piece].name[0]== home[0]-3) and r[piece].name[1] == home[1]:
                                    true = 0
                        if true == 1:
                            if x_diff == 2:
                                castle = 1
                                rook_to_move = drawingpiece[63]
                                rook_move_to = drawingcell[61]
                            if x_diff == -2:
                                castle = 1
                                rook_to_move = drawingpiece[56]
                                rook_move_to = drawingcell[59]
                else:
                    for piece in r:
                        if piece != piece2destroy:
                            if r[piece].name == target:
                                if r[piece].color == black:
                                    piece2cap = piece
                                else:
                                    target_is_yourpiece = 1
                                    true = 0
        if currentplayer == 1: ##player2
            if self.piece == "Pawn":
                if home[0] != target[0]:
                    true = 0
                    if home[0] == target[0]+1 or home[0] == target[0]-1:
                        if home[1] == target[1] + 1:
                            for piece in r:
                                if r[piece].name == target and r[piece].color == white:
                                    true = 1
                                    piece2cap = piece
                                if drawingcell[name_to_cell(target, currentplayer)].enpassant is True:
                                    true = 1
                                    for piece in r:
                                        if r[piece].name[1] - 1 == target[1] and r[piece].name[0] == target[0]:
                                            piece2cap = piece
                else:
                    if home[1] == target[1]+1:
                        true = 1
                        for piece in r:
                            if r[piece].name == target:
                                true = 0
                    elif home[1] == target[1] + 2 and self.moved == 0:
                        true = 1
                        for piece in r:
                            if r[piece].name == target:
                                true = 0
                            if r[piece].name[0] == home[0] and r[piece].name[1] == home[1]-1:
                                true = 0
                    else:
                        true = 0
            elif self.piece == "Knight":  # Knight logic
                if home[0] == target[0]:
                    true = 0
                else:
                    if home[0] == target[0] - 1 or home[0] == target[0] + 1:
                        if home[1] == target[1] - 2 or home[1] == target[1] + 2:
                            for piece in r:
                                if r[piece].name == target:
                                    if r[piece].color == white:
                                        true = 1
                                        piece2cap = piece
                                    else:
                                        true = 0
                        else:
                            true = 0
                    elif home[0] == target[0] - 2 or home[0] == target[0] + 2:
                        if home[1] == target[1] - 1 or home[1] == target[1] + 1:
                            for piece in r:
                                if r[piece].name == target:
                                    if r[piece].color == white:
                                        true = 1
                                        piece2cap = piece
                                    else:
                                        true = 0
                        else:
                            true = 0
                    else:
                        true = 0
            elif self.piece == "Bishop":
                x_diff = target[0]-home[0]
                y_diff = target[1]-home[1]
                gonnacapture = 0
                piece2cap = -1
                if home[0] == target[0]:
                    true = 0
                elif abs(x_diff) != abs(y_diff):
                    true = 0
                else:
                    for piece in r:
                        if r[piece].name == target:
                            if r[piece].color == white:
                                gonnacapture = 1
                                piece2cap = piece
                            else:
                                true = 0
                        else:
                            for i in range(1, abs(x_diff)):
                                if r[piece].name[0] == target[0] - (sign(x_diff)*i) and r[piece].name[1] == target[1] - \
                                        (sign(y_diff)*i):
                                    true = 0
                                    gonnacapture = 0
            elif self.piece == "Rook":
                x_move = target[0]-home[0]
                y_move = target[1]-home[1]
                pieceintheway = 0
                going2capture = 0
                piece2cap = -1
                if (x_move != 0 and y_move != 0) or (x_move == 0 and y_move == 0):
                    true = 0
                else:
                    if x_move != 0:
                        for piece in r:
                            for i in range(1, abs(x_move)):
                                if r[piece].name[0] == target[0]-(sign(x_move)*i) and r[piece].name[1] == target[1]:
                                    true = 0
                                    pieceintheway = 1
                            if r[piece].name == target:
                                if r[piece].color == white:
                                    going2capture = 1
                                    piece2cap = piece
                                else:
                                    true = 0
                    elif y_move != 0:
                        for piece in r:
                            for i in range(1, abs(y_move)):
                                if r[piece].name[1] == target[1]-(sign(y_move)*i) and r[piece].name[0]== target[0]:
                                    true = 0
                                    pieceintheway = 1
                            if r[piece].name == target:
                                if r[piece].color == white:
                                    going2capture = 1
                                    piece2cap = piece
                                else:
                                    true = 0
            elif self.piece == "Queen":
                true = 0
                pieceintheway = 0
                piece2cap = -1
                target_is_yourpiece = 0
                x_move = target[0] - home[0]
                y_move = target[1] - home[1]
                if (home[0] == target[0] or home[1] == target[1]) and not(home[0] == target[0] and home[1] == target[1]):
                    if home[0] != target[0]:
                        for piece in r:
                            for i in range(1, abs(x_move)):
                                if r[piece].name[0] == target[0]-(sign(x_move)*i) and r[piece].name[1] == target[1]:
                                    pieceintheway = 1
                            if pieceintheway == 0:
                                if r[piece].name == target:
                                    if r[piece].color == white:
                                        piece2cap = piece
                                    else:
                                        target_is_yourpiece = 1
                                        true = 0
                        if pieceintheway == 0 and target_is_yourpiece == 0:
                            true = 1
                    if home[1] != target[1]:
                        for piece in r:
                            for i in range(1, abs(y_move)):
                                if r[piece].name[1] == target[1]-(sign(y_move)*i) and r[piece].name[0] == target[0]:
                                    pieceintheway = 1
                            if pieceintheway == 0:
                                if r[piece].name == target:
                                    if r[piece].color == white:
                                        piece2cap = piece
                                    else:
                                        target_is_yourpiece = 1
                                        true = 0
                        if pieceintheway == 0 and target_is_yourpiece == 0:
                            true = 1
                elif home[0] != target[0] and home[1] != target[1]:
                    if abs(x_move) == abs(y_move):
                        for piece in r:
                            for i in range(1, abs(x_move)):
                                if r[piece].name[0] == target[0] - (sign(x_move) * i) and r[piece].name[1] == target[1] - \
                                        (sign(y_move) * i):
                                    pieceintheway = 1
                            if pieceintheway == 0:
                                if r[piece].name == target:
                                    if r[piece].color == white:
                                        piece2cap = piece
                                    else:
                                        target_is_yourpiece = 1
                                        true = 0
                        if pieceintheway == 0 and target_is_yourpiece == 0:
                            true = 1
            elif self.piece == "King":
                x_diff = target[0]-home[0]
                y_diff = target[1]-home[1]
                target_is_yourpiece = 0
                piece2cap = -1
                if abs(x_diff) > 1 or abs(y_diff) > 1:
                    true = 0
                    if (x_diff == 2 or x_diff == -2) and (y_diff == 0) and (self.moved == 0):
                        if (x_diff == 2 and drawingpiece[63].moved == 0) or (x_diff == -2 and drawingpiece[56].moved == 0):
                            true = 1
                        for piece in r:
                            if x_diff == 2:
                                if (r[piece].name[0] == home[0] + 1 or r[piece].name[0] == home[0] + 2) and r[piece].name[1] == home[1]:
                                    true = 0
                            if x_diff == -2:
                                if (r[piece].name[0] == home[0] - 1 or r[piece].name[0] == home[0] - 2 or r[piece].name[0]== home[0]-3) and r[piece].name[1] == home[1]:
                                    true = 0
                        if true == 1:
                            if x_diff == 2:
                                castle = 1
                                rook_to_move = drawingpiece[56]
                                rook_move_to = drawingcell[58]
                            if x_diff == -2:
                                castle = 1
                                rook_to_move = drawingpiece[63]
                                rook_move_to = drawingcell[60]
                else:
                    for piece in r:
                        if piece != piece2destroy:
                            if r[piece].name == target:
                                if r[piece].color == white:
                                    piece2cap = piece
                                else:
                                    target_is_yourpiece = 1
                                    true = 0
        if test == 1:
            testpiece.name = test_home
        if true == 1:
            return True, piece2cap, castle, rook_to_move, rook_move_to
        else:
            return False

def create_new_game():
    global drawingpiece
    global drawingcell
    global player
    global n
    global cellwidth
    global cellheight
    global MenuChoices
    global PawnMenu
    cellscollumns = 8
    cellgrid = 8 * 8
    drawingcell = {}
    drawingpiece = {}
    n = Network()
    player = int(n.getP())
    game = n.send("get")
    for cell in range(cellgrid):  # Makes chessgrid
        pieceimage = 0
        special_x = 0
        piece = ""
        special_y = 0
        text2nd = "0"
        name = ()
        text = ""
        textcolor = white
        cellwidth = height / 10  # 11 er et "tilfeldig" tall som bestemmer hvor stort rutenettet skal være på skjermen
        cellheight = height / 10
        collumn = cell - ((cell // 8) * 8)
        row = round((cell // 8) + 1)
        if player == 0:
            if row == 8:
                if collumn == 0:
                    text = "A"
                elif collumn == 1:
                    text = "B"
                elif collumn == 2:
                    text = "C"
                elif collumn == 3:
                    text = "D"
                elif collumn == 4:
                    text = "E"
                elif collumn == 5:
                    text = "F"
                elif collumn == 6:
                    text = "G"
                elif collumn == 7:
                    text = "H"
                special_x = cellwidth / 1.28  # 50 pixels in a 64x64
                special_y = cellheight / 1.28  # 50
            if collumn == 0:
                name = (1, (abs(row - 8) + 1))
                text += (str(abs(row - 8) + 1))
                special_x = cellwidth / 12.8  # 5
                special_y = cellheight / 12.8  # 5
            elif collumn == 1:
                name = (2, (abs(row - 8) + 1))
            elif collumn == 2:
                name = (3, (abs(row - 8) + 1))
            elif collumn == 3:
                name = (4, (abs(row - 8) + 1))
            elif collumn == 4:
                name = (5, (abs(row - 8) + 1))
            elif collumn == 5:
                name = (6, (abs(row - 8) + 1))
            elif collumn == 6:
                name = (7, (abs(row - 8) + 1))
            elif collumn == 7:
                name = (8, (abs(row - 8) + 1))
            if row == 8 and collumn == 0:
                text = (str(abs(row - 8) + 1))
                text2nd = "A"
        else:
            if row == 8:
                if collumn == 0:
                    text = "H"
                elif collumn == 1:
                    text = "G"
                elif collumn == 2:
                    text = "F"
                elif collumn == 3:
                    text = "E"
                elif collumn == 4:
                    text = "D"
                elif collumn == 5:
                    text = "C"
                elif collumn == 6:
                    text = "B"
                elif collumn == 7:
                    text = "A"
                special_x = cellwidth / 1.28  # 50
                special_y = cellheight / 1.28  # 50
            if collumn == 0:
                name = (8, (row))
                text += (str(abs(row)))
                special_x = cellwidth / 12.8  # 5
                special_y = cellheight / 12.8  # 5
            elif collumn == 1:
                name = (7, (row))
            elif collumn == 2:
                name = (6, (row))
            elif collumn == 3:
                name = (5, (row))
            elif collumn == 4:
                name = (4, (row))
            elif collumn == 5:
                name = (3, (row))
            elif collumn == 6:
                name = (2, (row))
            elif collumn == 7:
                name = (1, (row))
            if row == 8 and collumn == 0:
                text = (str(row))
                text2nd = "H"

        drawingcell[cell] = Button(text, ((width - (cellscollumns * cellwidth)) / 2) + (cellwidth * collumn),
                                   (cellheight * row), color, cellwidth, cellheight, name, special_x, special_y,
                                   text2nd,
                                   birch_desatured)
        special_x = 0
        special_y = 0
        text2nd = ""
        if drawingcell[cell].name[1] == 2 or drawingcell[cell].name[1] == 7:
            piece = "Pawn"
            textcolor = white
            pieceimage = WPawn
            if drawingcell[cell].name[1] == 7:
                textcolor = black
                pieceimage = BPawn

        else:
            if drawingcell[cell].name[0] == 1 or drawingcell[cell].name[0] == 8:  # Towers
                piece = "Rook"
                if drawingcell[cell].name[1] == 8:
                    textcolor = black
                    pieceimage = BRook
                if drawingcell[cell].name[1] == 1:
                    textcolor = white
                    pieceimage = WRook
            if drawingcell[cell].name[0] == 2 or drawingcell[cell].name[0] == 7:  # Knights
                piece = "Knight"
                if drawingcell[cell].name[1] == 8:
                    textcolor = black
                    pieceimage = BKnight
                if drawingcell[cell].name[1] == 1:
                    textcolor = white
                    pieceimage = WKnight
            if drawingcell[cell].name[0] == 3 or drawingcell[cell].name[0] == 6:  # Bishops
                piece = "Bishop"
                if drawingcell[cell].name[1] == 8:
                    textcolor = black
                    pieceimage = BBishop
                if drawingcell[cell].name[1] == 1:
                    textcolor = white
                    pieceimage = WBishop
            if drawingcell[cell].name[0] == 4:  # Queens
                piece = "Queen"
                if drawingcell[cell].name[1] == 8:
                    textcolor = black
                    pieceimage = BQueen
                if drawingcell[cell].name[1] == 1:
                    textcolor = white
                    pieceimage = WQueen
            if drawingcell[cell].name[0] == 5:  # Kings
                piece = "King"
                if drawingcell[cell].name[1] == 8:
                    textcolor = black
                    pieceimage = BKing
                if drawingcell[cell].name[1] == 1:
                    textcolor = white
                    pieceimage = WKing
        if cell < 16 or cell > 47:
            drawingpiece[cell] = Piece(drawingcell[cell].x + cellwidth / 4,
                                       drawingcell[cell].y + cellheight / 4, textcolor, piece, cellwidth / 2,
                                       cellheight / 2, name, pieceimage)

    ## Menu
    PawnMenu = Menu(0, 0, white, 80, 80, 1, 3)
    pieces = 4
    Brikketype = ""
    MenuChoices = {}
    MenuChoicePiece = 0
    for piece in range(1, pieces + 1):
        x = 0
        y = 0
        if player == 0:
            if piece == 1:
                MenuChoicePiece = WQueen
                Brikketype = "Queen"
            if piece == 2:
                MenuChoicePiece = WKnight
                Brikketype = "Knight"
            if piece == 3:
                MenuChoicePiece = WRook
                Brikketype = "Rook"
            if piece == 4:
                MenuChoicePiece = WBishop
                Brikketype = "Bishop"
        if player == 1:
            if piece == 1:
                MenuChoicePiece = BQueen
                Brikketype = "Queen"
            if piece == 2:
                MenuChoicePiece = BKnight
                Brikketype = "Knight"
            if piece == 3:
                MenuChoicePiece = BRook
                Brikketype = "Rook"
            if piece == 4:
                MenuChoicePiece = BBishop
                Brikketype = "Bishop"
        MenuChoices[piece] = MenuPiece(x, y, MenuChoicePiece, 80, 80, Brikketype)


def capture_piece(piece):
    if piece != -1:
        del drawingpiece[piece]

def name_to_cell(name, currentplayer):
    if currentplayer == 0:
        start = (1, 8)
    else:
        start = (8, 1)
    cellnumber = abs((name[0] - start[0]) + ((-name[1] + start[1]) * 8))
    return cellnumber

def aspect_scale(img, bx, by):
    """ Scales 'img' to fit into box bx/by.
     This method will retain the original image's aspect ratio """
    ix, iy = img.get_size()
    if ix > iy:
        # fit to width
        scale_factor = bx/float(ix)
        sy = scale_factor * iy
        if sy > by:
            scale_factor = by/float(iy)
            sx = scale_factor * ix
            sy = by
        else:
            sx = bx
    else:
        # fit to height
        scale_factor = by/float(iy)
        sx = scale_factor * ix
        if sx > bx:
            scale_factor = bx/float(ix)
            sx = bx
            sy = scale_factor * iy
        else:
            sy = by
    return pygame.transform.scale(img, (round(sx), round(sy)))

def sign(x):
    if x > 0:
        return 1.
    elif x < 0:
        return -1.
    elif x == 0:
        return 0.
    else:
        return x
def redrawWindow(win, game, p, pawn_menu):
    win.fill((128, 128, 128))
    #win.blit(Background, (0, 0))
    run = 1
    if not(game.connected()):
        font = pygame.font.SysFont("comicsansms", 80)
        text = font.render("Waiting for player..", 1, (255, 0, 0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsansms", 60)
        text = font.render("You are player " + str(p+1), 1, (0, 255, 255))
        win.blit(text, (80, 20))
        text = font.render("Opponents", 1, (0, 255, 255))
        win.blit(text, (380, 200))
        if game.bothWent():
            pass
        else:
            pass

        if p == 1:
            farge = 1
            text2part1Convers= game.p2Timer // 60
            text2part2Convers= game.p2Timer % 60
            text1part1Convers= game.p1Timer // 60
            text1part2Convers= game.p1Timer % 60
            text2part1 = font.render(str(text2part1Convers)[0:1], 1, (177, 192, 232), False)
            if text2part2Convers < 10:
                text2part2 = font.render("0"+str(text2part2Convers)[0:1], 1, (177, 192, 232), False)
            else:
                text2part2 = font.render(str(text2part2Convers)[0:2], 1, (177, 192, 232), False)
            text1part1 = font.render(str(text1part1Convers)[0:1], 1, (177, 192, 232), False)
            if text1part2Convers < 10:
                text1part2 = font.render("0"+str(text1part2Convers)[0:1], 1, (177, 192, 232), False)
            else:
                text1part2 = font.render(str(text1part2Convers)[0:2], 1, (177, 192, 232), False)
            timebox1 = Timer(text2part1, text2part2, 6*cellwidth, 9*cellheight, brown_desaturated, cellwidth*2, cellheight/2, white)
            timebox2 = Timer(text1part1, text1part2, 6*cellwidth, 0.5*cellheight, brown_desaturated, cellwidth*2, cellheight/2, white)
            timebox1.draw(win)
            timebox2.draw(win)
        else:
            farge = 1
            text1part1Convers= game.p1Timer // 60
            text1part2Convers= game.p1Timer % 60
            text2part1Convers= game.p2Timer // 60
            text2part2Convers= game.p2Timer % 60
            text1part1 = font.render(str(text1part1Convers)[0:1],1, (232, 190, 177), False)
            if text2part2Convers < 10:
                text2part2 = font.render("0" + str(text2part2Convers)[0:1], 1, (177, 192, 232), False)
            else:
                text2part2 = font.render(str(text2part2Convers)[0:2], 1, (177, 192, 232), False)
            text2part1 = font.render(str(text2part1Convers)[0:1],1, (255, 0, 0), False)
            if text1part2Convers < 10:
                text1part2 = font.render("0" + str(text1part2Convers)[0:1], 1, (177, 192, 232), False)
            else:
                text1part2 = font.render(str(text1part2Convers)[0:2], 1, (177, 192, 232), False)
            timebox1 = Timer(text2part1, text2part2, 6*cellwidth, 0.5*cellheight, brownish, cellwidth*2, cellheight/2, white)
            timebox2 = Timer(text1part1, text1part2, 6*cellwidth, 9*cellheight, brownish, cellwidth*2, cellheight/2, white)
            timebox1.draw(win)
            timebox2.draw(win)
        for cell in drawingcell:
            row = round((cell // 8) + 1)
            if (cell + row - farge) % 2 == 0:
                drawingcell[cell].color = (214, 220, 240)
                drawingcell[cell].textcolor = brown_desaturated
            else:
                drawingcell[cell].color = (34, 43, 43)
            drawingcell[cell].draw(win)
        for piece in drawingpiece:
            win.blit(drawingpiece[piece].pieceimage, (drawingpiece[piece].x - drawingpiece[piece].width/8,
                                                      drawingpiece[piece].y-drawingpiece[piece].height/4))
        if pawn_menu == 1:
            PawnMenu.draw_menu(win)
    pygame.display.update()
brown_desaturated = (185, 153, 77)
birch_desatured = (232, 216, 177)
birch = (248, 223, 161)
brownish = (205,133,63)
black = (0, 0, 0)
white = (255, 255, 255)
color = ()
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
purple = (255, 0, 255)
#startvalues
# images download
Background = pygame.image.load("Pictures/wood.png")
WBishop = pygame.image.load("Pictures/WhiteBishop.png")
BBishop = pygame.image.load("Pictures/BlackBishop.png")
WPawn = pygame.image.load("Pictures/WhitePawn.png")
BPawn = pygame.image.load("Pictures/BlackPawn.png")
WKing = pygame.image.load("Pictures/WhiteKing.png")
BKing= pygame.image.load("Pictures/BlackKing.png")
WKnight = pygame.image.load("Pictures/WhiteHorse.png")
BKnight = pygame.image.load("Pictures/BlackHorse.png")
WRook = pygame.image.load("Pictures/WhiteRook.png")
BRook = pygame.image.load("Pictures/BlackRook.png")
WQueen = pygame.image.load("Pictures/WhiteQueen.png")
BQueen = pygame.image.load("Pictures/BlackQueen.png")
Background.convert()
WBishop.convert()
BBishop.convert()
BRook.convert()
WRook.convert()
BPawn.convert()
WPawn.convert()
WKnight.convert()
BKnight.convert()
BQueen.convert()
WQueen.convert()
WKing.convert()
BKing.convert()
#Background = aspect_scale(Background, width, height)
WBishop = aspect_scale(WBishop, 76, 76)
BBishop = aspect_scale(BBishop, 80, 80)
BRook = aspect_scale(BRook, 80, 80)
WRook = aspect_scale(WRook, 80, 80)
BKing = aspect_scale(BKing, 80, 80)
WKing = aspect_scale(WKing, 80, 80)
BQueen = aspect_scale(BQueen, 80, 80)
WQueen = aspect_scale(WQueen, 80, 80)
BPawn = aspect_scale(BPawn, 80, 80)
WPawn = aspect_scale(WPawn, 80, 80)
WKnight = aspect_scale(WKnight, 80, 80)
BKnight = aspect_scale(BKnight, 80, 80) 
##########################
first = True
cellwidth = height / 10  # 11 er et "tilfeldig" tall som bestemmer hvor stort rutenettet skal være på skjermen
cellheight = height / 10
create_new_game()
#globals
if player == 0:
    updated = True
else:
    updated = False
def main():
    timer = 0
    held = 0
    brikke = -1
    run = True
    clock = pygame.time.Clock()
    print("You are player", player)

    while run:
        clock.tick(60)
        timer += 1
        timer = timer % 2
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game1")
            break
        if game.winner != "unkn":
            win_screen(game.winner)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.finished = True
                run = False
                pygame.QUIT()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if event.button == 1:
                    for piece in drawingpiece:
                        if drawingpiece[piece].click(pos) and game.connected():
                            held = 1
                            if player == 0:
                                brikke = piece
                            else:
                                brikke = piece
            if event.type == pygame.MOUSEBUTTONUP:
                if held == 1 and brikke != -1:
                    square = drawingpiece[brikke].find_square()
                    print("DROP1")
                    drawingpiece[brikke].drop(square, game.p1Went, game.p2Went, player)

                held = 0
        while held == 1:
            if brikke != -1:
                drawingpiece[brikke].movingpiece()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        if held == 1 and brikke != -1:
                            square = drawingpiece[brikke].find_square()
                            print("DROP2")
                            drawingpiece[brikke].drop(square, game.p1Went, game.p2Went, player)
                        held = 0
        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if player == 0:
            r = dict(drawingpiece)
            if move2 and updated is False:
                home = move2[1:7]
                hometup = ast.literal_eval(home)
                homecell = name_to_cell(hometup, player)
                target = move2[9:15]
                targettup = ast.literal_eval(target)
                targetcell = name_to_cell(targettup, player)
                # For castle cases only! ! ! ! ! ! !

                castlemove2_from = move2[17:23]
                castlemove2_to = move2[25:31]
                castle_move_from_tup = ast.literal_eval(castlemove2_from)
                castle_move_from_cell = name_to_cell(castle_move_from_tup, player)
                castle_move_to_tup = ast.literal_eval(castlemove2_to)
                castle_move_to_cell = name_to_cell(castle_move_to_tup, player)
                #PAwn upgrade cases only !!! ! ! !!
                pawnupgrade_to = move2[32:]
                for piece in r:
                    if r[piece].color == black:
                        if r[piece].name == hometup:
                            r[piece].update_enemy_move(homecell, targetcell, pawnupgrade_to, player)
                        if r[piece].name == castle_move_from_tup:
                            r[piece].update_enemy_move(castle_move_from_cell, castle_move_to_cell, pawnupgrade_to, player)
        if player == 1:
            r = dict(drawingpiece)
            if move1 and updated is False:
                home = move1[1:7]
                hometup = ast.literal_eval(home)
                homecell = name_to_cell(hometup, player)
                target = move1[9:15]
                targettup = ast.literal_eval(target)
                targetcell = name_to_cell(targettup, player)
                # For castle cases only! ! ! ! ! ! !

                castlemove1_from = move1[17:23]
                castlemove1_to = move1[25:31]
                castle_move_from_tup = ast.literal_eval(castlemove1_from)
                castle_move_from_cell = name_to_cell(castle_move_from_tup, player)
                castle_move_to_tup = ast.literal_eval(castlemove1_to)
                castle_move_to_cell = name_to_cell(castle_move_to_tup, player)
                #For pawnUpgrade cases only ! !! !
                pawnupgrade_to = move1[32:]
                for piece in r:
                    if r[piece].color == white:
                        if r[piece].name == hometup:
                            # print(hometup)
                            r[piece].update_enemy_move(homecell, targetcell, pawnupgrade_to, player)
                        if r[piece].name == castle_move_from_tup:
                            r[piece].update_enemy_move(castle_move_from_cell, castle_move_to_cell, pawnupgrade_to, player)
        pygame.time.delay(0)
        pygame.display.update()
        redrawWindow(win, game, player, 0)
    readycheck(False)

def readycheck(first):
    run = True
    first = first

    while run:
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsansms", 60)
        text = font.render("Click to play!", 1, (255, 0, 0))
        win.blit(text, (100, 200))
        pygame.display.update()
        try:
            if first is False:
                print("FIRST")
                create_new_game()
                first = True
        except:
            run = False
            print("Couldn't create new game")
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                n.send("Start") #player is ready, runs game.playerconnect(p)
                run = False
    main()

def win_screen(winner):
    print("WIN SCREEN")
    print(winner)
    t = time.perf_counter()
    while True:
        font = pygame.font.SysFont("comicsansms", 60)
        if winner == player:
            win.fill((34,139,34))
            text = font.render("You Won", 1, (0, 0, 0))
        else:
            win.fill((178,34,34))
            text = font.render("You Lost", 1, (0, 0, 0))
        win.blit(text, (100, 200))
        button = Button("New game", 500, 500, (105, 105, 105), 100, 100, "nothing", 0, 0, "0", (255, 255, 255))
        button.draw(win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if button.click(pos):
                    n.send("Nytt game")
                    readycheck(False)
if __name__ == "__main__":
    readycheck(True)
