# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def render(board_width, board_height, shots):
    header = "+" + "_" * board_width + "+"
    print(header)

    shots_set = set(shots)
    for y in range(board_height):
        row = []
        for x in range(board_width):
            if (x,y) in shots:
                ch = "X"
            else:
                ch = " "
            row.append(ch)
        print("|" + "".join(row) + "|")

    for i in range(board_height):
        print("|" + " " * board_width + "|")

if __name__ == "__main__":
    shots = []

    while True:
        inp = input("Where do you want to shoot?\n")
        xstr,ystr = inp.split(",")
        x = int(xstr)
        y = int(ystr)

        shots.append((x,y))
        render(10, 10, shots)
        




