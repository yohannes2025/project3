# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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
    render_battleships(10, 10, battleships)
    exit(0)



    shots = []

    while True:
        inp = input("Where do you want to shoot?\n")
        xstr,ystr = inp.split(",")
        x = int(xstr)
        y = int(ystr)

        shots.append((x,y))
        render(10, 10, shots)
        




