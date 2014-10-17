#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import random

def drawBoard(board):
    # This function prints out the board that it was passed.

    os.system('clear')
    # board[6x7]
    # "board" is a matrix with 6 rows and 7 columns of strings
    print('| ' +board[5][0]+ ' | ' +board[5][1]+ ' | ' +board[5][2]+ ' | ' +board[5][3]+ ' | ' +board[5][4]+ ' | ' +board[5][5]+ ' | ' +board[5][6]+ ' |')
    print('-----------------------------')
    print('| ' +board[4][0]+ ' | ' +board[4][1]+ ' | ' +board[4][2]+ ' | ' +board[4][3]+ ' | ' +board[4][4]+ ' | ' +board[4][5]+ ' | ' +board[4][6]+ ' |')
    print('-----------------------------')
    print('| ' +board[3][0]+ ' | ' +board[3][1]+ ' | ' +board[3][2]+ ' | ' +board[3][3]+ ' | ' +board[3][4]+ ' | ' +board[3][5]+ ' | ' +board[3][6]+ ' |')
    print('-----------------------------')
    print('| ' +board[2][0]+ ' | ' +board[2][1]+ ' | ' +board[2][2]+ ' | ' +board[2][3]+ ' | ' +board[2][4]+ ' | ' +board[2][5]+ ' | ' +board[2][6]+ ' |')
    print('-----------------------------')
    print('| ' +board[1][0]+ ' | ' +board[1][1]+ ' | ' +board[1][2]+ ' | ' +board[1][3]+ ' | ' +board[1][4]+ ' | ' +board[1][5]+ ' | ' +board[1][6]+ ' |')
    print('-----------------------------')
    print('| ' +board[0][0]+ ' | ' +board[0][1]+ ' | ' +board[0][2]+ ' | ' +board[0][3]+ ' | ' +board[0][4]+ ' | ' +board[0][5]+ ' | ' +board[0][6]+ ' |')
    print('-----------------------------')
    print('| 1 | 2 | 3 | 4 | 5 | 6 | 7 |')
    print('')
def inputPlayerLetter():
    # Let's the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the
    # computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'x' or letter == 'O' or letter == 'o'):
#        print('Do you want to be X or O?')
#        letter = input().upper()
        letter = raw_input('Do you want to be X or O?\t')

    # the first element in the tuple is the player's letter, the second is
    # the computer's letter.
    if letter == 'X' or letter == 'x':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This function returns True if the player wants to play again, otherwise
    # it returns False.
#    print('Do you want to play again? (yes or no)')
#    return input().lower().startswith('y')
    again = raw_input('Do you want to play again? (y or n)\t')

    if again == 'Y' or again == 'y' or again == 'Yes' or again == 'yes':
        return True
    elif again == 'N' or again == 'n' or again == 'No' or again == 'no' or again == '':
        return False
    else:
        return False

def makeMove(board, letter, move):
    x = 0
    for i in range(len(board)):
        moveList = [x, move] 
        if isSpaceFree(board, moveList):
            board[int(moveList[0])][int(moveList[1])] = letter
            break
        else:
            x = x +1
######################### Arreglado isWinner(board, letter)        ####SEMI-Arreglado
def isWinner(board, letter):
    # Given a board and a player's letter, this function returns True if that
    # player has won. We use bo instead of board and le instead of letter so
    # we don't have to type as much.
    win = False
    #FOR HorizontalWin (ROW)
    x = 0
    for i in board:
        y = 0
        for j in board[x]:
            if y < 4 and win == False:
                if (board[x][y +0] == letter and board[x][y +1] == letter and board[x][y +2] == letter and board[x][y +3] == letter):
                    win = True
                else:
                    y = y +1
            else:
                j = len(board[x])
        x = x +1
    #FOR VerticalWin (COLUMN)                           ####REVISAR LINEA 87 (List index out of range)       ####SEMI-Arreglado
    y = 0
    for i in board[y]:
        x = 0
        for j in board:
            if x < 3 and win == False:
                if (board[x +0][y] == letter and board[x +1][y] == letter and board[x +2][y] == letter and board[x +3][y] == letter):
                    win = True
                else:
                    x = x +1
            else:
                j = len(board)
        y = y +1
    #TODO DiagonalWin
    return win
#    (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
#    (board[9] == letter and board[5] == letter and board[1] == letter) # diagonal
######################### Arreglado getBoardCopy(board)
def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    copyBoard = []
    for i in range(6):
        copyBoard.append([' '] * 7)
    x = 0
    for i in board:
        y = 0
        for j in board[x]:                              ####REVISAR LINEA 109 (List indices must be integers, not list)   ####SEMI-Arreglado
            copyBoard[x][y] = board[x][y]
            y = y +1
        x = x +1
    return copyBoard
######################### Arreglado isSpaceFree(board, move)
def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[int(move[0])][int(move[1])] == ' '     ####REVISAR LINEA 119 ('int' object has no attribute '__getitem__')
######################### Arreglado getPlayerMove(board)
def getPlayerMove(board):
    # Let the player type in his move.
    x = 0
    move = raw_input('What is your next move? (1-7)\t')
    for i in range(len(board)):
        moveList = [x, (int(move) -1)]
        if move in '1 2 3 4 5 6 7'.split():
            if isSpaceFree(board, moveList) == True:
                return (int(move) -1)
            else:
                x = x +1
        else:
            move = raw_input('What is your next move? (1-7)\t')
############################################################################################### Arreglado hasta aquí
def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
#########################SEMI-Arreglado
def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and
    # return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    x = 0
    for i in range(len(board)):
        y = 0
        for j in range(len(board[x])):
            copy = getBoardCopy(board)
            move = [x, y]
            if isSpaceFree(copy, move):
                makeMove(copy, computerLetter, move)
                if isWinner(copy, playerLetter):
                    return move
            y = y +1
        x = x +1
    # Check if the player could win on his next move, and block them.
    x = 0
    for i in range(len(board)):
        y = 0
        for j in range(len(board[x])):
            copy = getBoardCopy(board)
            move = [x, y]
            if isSpaceFree(copy, move):
                makeMove(copy, playerLetter, move)
                if isWinner(copy, playerLetter):
                    return move
            y = y +1
        x = x +1
    # Try to take one of the corners, if they are free.  ##########
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
######################## Arreglado isBoardFull(board)       ####SEMI-Arreglado
def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise
    # return False.
    x = 0
    for i in range(len(board)):
        y = 0
        for j in range(len(board[x])):
            move = [x, y]
            if isSpaceFree(board, move):
                return False
            y = y +1
        x = x +1
    return True
################################################################### MAIN ###################################################################
os.system('clear')
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = []
    for i in range(6):
        theBoard.append([' '] * 7)

    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    wait = raw_input('\nPress Enter to continue');
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
################################################### Aqui PETA
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
#            move = getComputerMove(theBoard, computerLetter)
#            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break

os.system('clear')
