# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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
        return Battleship(body)

    def __init__(self,body):
        self.body = body
        self.hits = [False] * len(body)

    def body_index(self, location):        
        try:
            return self.body.index(location)
        except ValueError:
            return None
                

    #b = Battleship.build((1,1), 5, "S")
    #b2 = Battleship([(1,1), (2,1), (3,1),(4,1),(5,1)])

def render(board_width, board_height, shots):
    header = "+" + "_" * board_width + "+"
    print(header)

    shots_set = set(shots)
    for y in range(board_height):
        row = []
        for x in range(board_width):
            if (x,y) in shots_set:
                ch = "X"
            else:
                ch = " "
            row.append(ch)
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

if __name__ == "__main__":
    battleships = [
        Battleship.build((1,1), 2, "N"),
        Battleship.build((5,8), 5, "N"),
        Battleship.build((2,3), 4, "E")
    ]
    for b in battleships:
        print(b.body)
    
    game_board = GameBoard(battleships, 10,10)
    shots = [(1,1), (0,0), (5,7)]
    for sh in shots:
        game_board.take_shot(sh)

    for sh in game_board.shots:
        print(sh.location)
        print(sh.is_hit)
    for b in game_board.battleships:
        print(b.body)
        print(b.hits)

    exit(0)

    shots = []

    while True:
        inp = input("Where do you want to shoot?\n")
        xstr,ystr = inp.split(",")
        x = int(xstr)
        y = int(ystr)

        shots.append((x,y))
        render(10, 10, shots)
        




