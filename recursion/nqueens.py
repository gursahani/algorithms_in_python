def printBoard(boardArr):
    for i in range(len(boardArr)):
        print(boardArr[i])


def fillBoard(boardArr):
    for i in range(len(boardArr)):
        boardArr[i]='Q'

boardArr = [["." for x in range(8)] for y in range(8)]
# printBoard(boardArr)

fillBoard(boardArr)
printBoard(boardArr)