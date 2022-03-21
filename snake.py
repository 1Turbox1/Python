from asyncio.windows_events import NULL
import random, os, time, argparse, numpy, keyboard

point = 0
continuoslyGoUp = False
continuoslyGoDown = False
continuoslyGoLeft = False
continuoslyGoRight = False

def move(args, x, y):
    global continuoslyGoUp
    global continuoslyGoDown
    global continuoslyGoLeft
    global continuoslyGoRight

    if keyboard.is_pressed('w'):
        y -= 1
        continuoslyGoUp = True
        continuoslyGoDown = False
        continuoslyGoLeft = False
        continuoslyGoRight = False
    elif keyboard.is_pressed('s'):
        y += 1
        continuoslyGoDown = True
        continuoslyGoUp = False
        continuoslyGoLeft = False
        continuoslyGoRight = False
    elif keyboard.is_pressed('a'):
        x -= 1
        continuoslyGoLeft = True
        continuoslyGoRight = False
        continuoslyGoUp = False
        continuoslyGoDown = False
    elif keyboard.is_pressed('d'):
        x += 1
        continuoslyGoRight = True
        continuoslyGoLeft = False
        continuoslyGoUp = False
        continuoslyGoDown = False
    else:
        if continuoslyGoUp == True:
            y -= 1
        elif continuoslyGoDown == True:
            y += 1
        elif continuoslyGoLeft == True:
            x -= 1
        elif continuoslyGoRight == True:
            x += 1
        else:
            pass
    return x, y
    
def gameOver():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Game Over!
    """)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Game Over!
    """)
    exit()
    time.sleep(5000)
    
def checkPositions(args, board, x, y, randomX, randomY):
    global point
    if board[randomY][randomX] == " ":
        board[randomY][randomX] = "^"
    if x == randomX and y == randomY:
        point += 1
        randomX = random.randint(1, args.width - 2)
        randomY = random.randint(1, args.height - 2)
        args.refreshSpeed -= 0.002

    if board[y][x] == " " or board[y][x] == "^":
        board[y][x] = "@"
    if board[y][x] == "|" or board[y][x] == "_" or board[y][x] == "-":
            gameOver()
    return randomX, randomY, board[y][x], x, y
    

def refershBoard(args, x, y, randomX, randomY):
    board = numpy.empty((args.height, args.width), dtype = 'str')
    for i in range(args.height):
        for j in range(args.width):
            board[i][j] = " "
    for i in range(args.height):
        for j in range(args.width):
            if i == args.height-1:
                board[i][j] = "_"
            if  i == args.height - args.height:
                board[i][j] = "-"
            if j == args.width - args.width or j == args.width-1:
                board[i][j] = "|"

            randomX, randomY, board[y][x], x, y = checkPositions(args, board, x, y, randomX, randomY)
            print(str(board[i][j]), end=" ")
        print()
    return randomX, randomY

def start(args):
    playing = False
    global point
    x = args.startX
    y = args.startY
    point = 0
    randomX = random.randint(1, args.width - 2)
    randomY = random.randint(1, args.height - 2)
    while playing == False:
        x, y = move(args, x, y)
        print("Points:" + str(point) + " Position: " + str(x) + "," + str(y))
        randomX, randomY = refershBoard(args, x, y, randomX, randomY)
        time.sleep(args.refreshSpeed)
        os.system('cls' if os.name == 'nt' else 'clear')

def startingScreen():
    print("""
    Welcome to the Snake Game!
    """)
    time.sleep(2)

def main(args):
    startingScreen()
    os.system('cls' if os.name == 'nt' else 'clear')
    start(args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-width", "--width", help="width of the array", type=int, default=20)
    parser.add_argument("-height", "--height", help="height of the array", type=int, default=30)
    parser.add_argument("-refershSpeed", "--refreshSpeed", help="refresh speed of the game", type=float, default=0.008)

    args = parser.parse_args()

    parser.add_argument("-startX", "--startX", help="starting X position of the player", type=int, default=random.randint(2, args.width - 2))
    parser.add_argument("-startY", "--startY", help="starting Y position of the player", type=int, default=random.randint(2, args.height - 2))

    args = parser.parse_args()
    print(args)

    main(args)