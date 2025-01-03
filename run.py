# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import copy
import random

class GameBoard(object):
    def __init__(self, battleships, board_width, board_height):
        self.battleships = battleships
        self.shots = []
        self.board_width = board_width
        self.board_height = board_height
    # * Update battleship with any hits
    # * Save the fact that the shot was a hit or a miss
    def take_shot(self, shot_location):
        is_hit = False
        for b in self.battleships:            
            idx = b.body_index(shot_location)  
            if idx is not None:        
                is_hit = True
                b.hits[idx] = True                
                break
        #self.shots.append(Shot(shot_location, is_hit))
    def is_game_over(self):
        return all([b.is_destroyed() for b in self.battleships])
        for b in self.battleships:
            if not b.is_destroyed():
                return False
        # For each battleship, is it destroyed?
        # If yes for all, return True, else False
        


class Shot(object):
    def __init__(self, shot_location):
        for b in self.battleships:
            try:
                idx = b.body().index(shot_location)
                if shot_location in b. body():
                    is_hit = True
                    b.hits[idx] = True
            except ValueError:
                    pass

class Battleship(object):
    @staticmethod
    def build(head, length, direction):
        body = []
        for i in range(length):
            if direction == "N":
                el = (head[0], head[1] - i)
            elif direction == "S":
                el = (head[0], head[1] + i)
            if direction == "W":
                el = (head[0] - i, head[1])
            elif direction == "E":
                el = (head[0] + i, head[1])
            body.append(el)
        return Battleship(body, head, length, direction)

    def __init__(self,body, head, length, direction):
        self.body = body
        self.head = head
        self.length = length
        self.direction = direction
        self.hits = [False] * len(body)

    def body_index(self, location):        
        try:
            return self.body.index(location)
        except ValueError:
            return None
    def is_destroyed(self):            
        return all(self.hits)


class Player(object):
    def __init__(self, name, shot_function):
        self.name = name
        self.shot_function = shot_function

    

def render(game_board, show_battleships=False):
    header = "+" + "_" * game_board.board_width + "+"
    print(header)
     # construct empty board
    board = []
    for _ in range(game_board.board_width):
        row = []
        for y in range (game_board.board_height):
            board.append([None for _ in range(game_board.board_height)])            

    if show_battleships:        
        # Add the battleships to the board
        for b in game_board.battleships:
            for x, y in b.body:
                board[x][y] = "O"
            
    # Add the shots to the board
    for sh in game_board.shots:
        x, y = sh.location
        if sh.is_hit:
            ch = "X"
        else:
            ch = "."
        board[x][y] = ch

    for y in range(game_board.board_height):
        row = []
        for x in range(game_board.board_width):
            row.append(board[x][y] or " ")
        print("|" + "".join(row) + "|") 

    print(header)
    

def render_battleships(board_width, board_height, battleships):
    header = "+" + "_" * board_width + "+"
    print(header)

    # construct empty board
    board = []
    for _ in range(board_width):
        row = []
        for y in range (board_height):
            board.append([None for _ in range(board_height)])            
            
    # Add the battleships to the board
    for b in battleships:
        for x, y in b.body:
            board[x][y] = "O"
            
    for y in range(board_height):
        row = []
        for x in range(board_width):
            row.append(board[x][y] or " ")
        print("|" + "".join(row) + "|")

    print(header)

def get_computer_shot(game_board):
    x = random.randint(0, game_board.board_width - 1)
    y = random.randint(0, game_board.board_height - 1)
    return (x, y)

def get_human_shot(game_board):
    inp = input("Where do you want to shoot?\n")
    xstr, ystr = inp.split(",")
    x = int(xstr)
    y = int(ystr)
    return (x, y)

if __name__ == "__main__":


    battleships = [
        Battleship.build((1,1), 2, "N"),
        # Battleship.build((5,8), 5, "N"),
        # Battleship.build((2,3), 4, "E")
    ]    
    game_boards = [
        GameBoard(battleships, 10,10),
        GameBoard(copy.deepcopy(battleships), 10,10)
    ]

    # player_names = [
    #     "JOhn",
    #     "Thomas"
    # ]

    players = [
        Player("Jack", get_human_shot),
        Player("Robert", get_computer_shot)
    ]

    offensive_idx = 0
    while True:
        # defensive player is the non-offensive one
        defensive_idx = (offensive_idx +1) % 2

        defensive_board = game_boards[defensive_idx]
        offensive_player = players[offensive_idx]

        print("%s YOUR Turn!" % offensive_player.name)
        shot_location = offensive_player.shot_function(defensive_board)        

        defensive_board.take_shot(shot_location)      
        render(defensive_board)

        if defensive_board.is_game_over():
            print("%s WINS!" % offensive_player.name)
            break
        #offensivr plyer becomes the previous defensive player
        # print(offensive_idx)
        # print(defensive_idx)
        offensive_idx = defensive_idx
        




