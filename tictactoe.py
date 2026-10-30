
def printBoard(xState, yState):

    print(f"{'X' if xState[0] else 'O' if yState[0] else ' '} | {'X' if xState[1] else 'O' if yState[1] else ' '} | {'X' if xState[2] else 'O' if yState[2] else ' '}")
    print("--+---+--")
    print(f"{'X' if xState[3] else 'O' if yState[3] else ' '} | {'X' if xState[4] else 'O' if yState[4] else ' '} | {'X' if xState[5] else 'O' if yState[5] else ' '}")
    print("--+---+--")
    print(f"{'X' if xState[6] else 'O' if yState[6] else ' '} | {'X' if xState[7] else 'O' if yState[7] else ' '} | {'X' if xState[8] else 'O' if yState[8] else ' '}")


def checkWin(xState, yState):

    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for win in wins:

        if xState[win[0]] + xState[win[1]] + xState[win[2]] == 3:
            print("X Won the match!")
            return 1

        if yState[win[0]] + yState[win[1]] + yState[win[2]] == 3:
            print("Y Won the match!")
            return 0

    return -1


if __name__ == '__main__':

    xState = [0,0,0,0,0,0,0,0,0]
    yState = [0,0,0,0,0,0,0,0,0]

    turn = 1  # 1 for X and 0 for Y

    print("Welcome to Tic Tac Toe")

    while True:

        printBoard(xState, yState)

        if turn == 1:

            print("X's turn")
            value = int(input("Please enter a value from 0-8: "))

            if value < 0 or value > 8:
                print("Invalid position! Try again.")
                continue

            if xState[value] == 0 and yState[value] == 0:
                xState[value] = 1
                turn = 0
            else:
                print("Position already occupied! Try again.")
                continue

        else:

            print("Y's turn")
            value = int(input("Please enter a value from 0-8: "))

            if value < 0 or value > 8:
                print("Invalid position! Try again.")
                continue

            if xState[value] == 0 and yState[value] == 0:
                yState[value] = 1
                turn = 1
            else:
                print("Position already occupied! Try again.")
                continue

        cwin = checkWin(xState, yState)

        if cwin != -1:
            printBoard(xState, yState)
            break

        if sum(xState) + sum(yState) == 9:
            printBoard(xState, yState)
            print("It's a Draw!")
            break
