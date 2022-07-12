theBoard  ={'7': ' ' , '8': ' ' , '9': ' ',
            '4': ' ' , '5': ' ' , '6': ' ',
            '1': ' ' , '2': ' ' , '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print (board['7'] + '|' + board['8'] + '|' + board['9'])
    print ('-+-+-')
    print (board['4'] + '|' + board['5'] + '|' + board['6'])
    print ('-+-+-')
    print (board['1'] + '|' + board['2'] + '|' + board['3'])

player1 = input("would you prefer to be naughts or crosses? (O/X)")
if player1 == "O" or player1 == "naughts" or player1 =="o":
    player1 = "O"
elif player1 == "X" or player1 == "crosses" or player1 == "x":
    player1 = "X"

def game():
    
        turn = player1
        count = 0

        for i in range(10):
            printBoard(theBoard)
            print("it's your not turn," + turn + " move to which place?")

            move = input()

            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                print ("that place is already filled. \nMove to which place?")
                continue 

            if count >= 5:
                if theBoard['7'] == theBoard ['8'] == theBoard['9'] != ' ':
                    printBoard (theBoard)
                    print("\n Game Over. \n")
                    print(" ****" + turn + " won. ****")
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                    printBoard(theBoard)
                    print ("\n Game Over. \n")
                    print (" **** " + turn + " won. ****")
                    break
                elif theBoard ['1'] == theBoard['2'] == theBoard ['3']!= ' ':
                    printBoard(theBoard)
                    print("\n Game over. \n")
                    print (" **** " + turn + " won. ****")
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                    printBoard(theBoard)
                    print("\n Game Over. \n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                    printBoard(theBoard)
                    print("\n Game Over. \n")   
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                    printBoard(theBoard)
                    print("\n Game Over. \n")
                    print(" **** " + turn + " won. ****")
                    break
                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                    printBoard(theBoard)
                    print("\n Game Over \n")
                    print(" **** "  + turn + " won. ****")
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                    printBoard(theBoard)
                    print("\n Game Over \n")
                    print(" **** " + turn + " won. ****")
                    break

            if count == 9:
                print ("\n Game Over.\n")
                print("It's a Tie!")
                break

            if turn == "X":
                turn = "O"
            else:
                turn = "X"

        restart = input("Do you want to play again? (y/n)")
        if restart == "y" or restart == "Y":
            for key in board_keys:
                theBoard[key] = " "

            game()

if __name__ == "__main__":
    game()