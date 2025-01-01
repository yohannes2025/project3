# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high



if __name__ == "__main__":
    render(10,10)

    inp = input("Where do you want to shoot?\n")
    xstr,ystr = inp.split(",")
    x = int(xstr)
    y = int(ystr)
    print(x)
    print(y)
    print(x+y)




