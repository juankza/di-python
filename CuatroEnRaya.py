#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import sys

def drawBoard(board):
    # This function prints out the board that it was passed
    # That "board" is a matrix with 6 rows and 7 columns of strings (6x7)
    os.system('clear')
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
    # Let's the player type which letter they want to be
    # Returns a list with the player's letter as the first item, and the computer's letter as the second
    letter = ''
    while not (letter == 'X' or letter == 'x' or letter == 'O' or letter == 'o'):
        letter = raw_input('Do you want to be X or O?\t')
    if letter == 'X' or letter == 'x':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False
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

def isWinner(board, letter):
    # Given a board and a player's letter, this function returns True checking if that player has won
    win = False
    # FOR HorizontalWin (ROW)
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
    # FOR VerticalWin (COLUMN)
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
    # IF DiagonalWin (LEFT-TO-RIGHT)
    if ((board[2][0] == letter and board[3][1] == letter and board[4][2] == letter and board[5][3] == letter) or
    (board[1][0] == letter and board[2][1] == letter and board[3][2] == letter and board[4][3] == letter) or
    (board[2][1] == letter and board[3][2] == letter and board[4][3] == letter and board[5][4] == letter) or
    (board[0][0] == letter and board[1][1] == letter and board[2][2] == letter and board[3][3] == letter) or
    (board[1][1] == letter and board[2][2] == letter and board[3][3] == letter and board[4][4] == letter) or
    (board[2][2] == letter and board[3][3] == letter and board[4][4] == letter and board[5][5] == letter) or
    (board[0][1] == letter and board[1][2] == letter and board[2][3] == letter and board[3][4] == letter) or
    (board[1][2] == letter and board[2][3] == letter and board[3][4] == letter and board[4][5] == letter) or
    (board[2][3] == letter and board[3][4] == letter and board[4][5] == letter and board[5][6] == letter) or
    (board[0][2] == letter and board[1][3] == letter and board[2][4] == letter and board[3][5] == letter) or
    (board[1][3] == letter and board[2][4] == letter and board[3][5] == letter and board[4][6] == letter) or
    (board[0][3] == letter and board[1][4] == letter and board[2][5] == letter and board[3][6] == letter)):
        win = True
    else:
        win = False
    # IF DiagonalWin (RIGHT-TO-LEFT)
    if ((board[2][6] == letter and board[3][5] == letter and board[4][4] == letter and board[5][3] == letter) or
    (board[1][6] == letter and board[2][5] == letter and board[3][4] == letter and board[4][3] == letter) or
    (board[2][5] == letter and board[3][4] == letter and board[4][3] == letter and board[5][2] == letter) or
    (board[0][6] == letter and board[1][5] == letter and board[2][4] == letter and board[3][3] == letter) or
    (board[1][5] == letter and board[2][4] == letter and board[3][3] == letter and board[4][2] == letter) or
    (board[2][4] == letter and board[3][3] == letter and board[4][2] == letter and board[5][1] == letter) or
    (board[0][5] == letter and board[1][4] == letter and board[2][3] == letter and board[3][2] == letter) or
    (board[1][4] == letter and board[2][3] == letter and board[3][2] == letter and board[4][1] == letter) or
    (board[2][3] == letter and board[3][2] == letter and board[4][1] == letter and board[5][0] == letter) or
    (board[0][4] == letter and board[1][3] == letter and board[2][2] == letter and board[3][1] == letter) or
    (board[1][3] == letter and board[2][2] == letter and board[3][1] == letter and board[4][0] == letter) or
    (board[0][3] == letter and board[1][2] == letter and board[2][1] == letter and board[3][0] == letter)):
        win = True
    else:
        win = False
    return win

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate
    copyBoard = []
    for i in range(6):
        copyBoard.append([' '] * 7)
    x = 0
    for i in board:
        y = 0
        for j in board[x]:
            copyBoard[x][y] = board[x][y]
            y = y +1
        x = x +1
    return copyBoard

def isSpaceFree(board, moveList):
    # Return true if the passed move is free on the passed board
    return board[int(moveList[0])][int(moveList[1])] == ' '

def getPlayerMove(board):
    # Let the player type in his move
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

def getRandomMove(board):
    # Returns a random valid move on the passed board
    # Returns None if there is no valid move
    canMove = []
    x = 0
    for i in range(len(board)):
        y = 0
        for j in range(len(board[x])):
            moveList = [x, y]
            if isSpaceFree(board, moveList) == True:
                canMove.append(int(moveList[1]))
            else:
                y = y +1
        x = x +1
    if len(canMove) != 0:
        return random.choice(canMove)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    ##### ComputerAI #####
    # First, check if we can win in the next move
    x = 0
    for i in range(len(board)):
        y = 0
        for j in range(len(board[x])):
            copy = getBoardCopy(board)
            moveList = [x, y]
            if isSpaceFree(copy, moveList) == True:
                makeMove(copy, computerLetter, y)
                if isWinner(copy, playerLetter):
                    return y
            y = y +1
        x = x +1
    # Check if the player could win on his next move to block them
    x = 0
    for i in range(len(board)):
        y = 0
        for j in range(len(board[x])):
            copy = getBoardCopy(board)
            moveList = [x, y]
            if isSpaceFree(copy, moveList) == True:
                makeMove(copy, playerLetter, y)
                if isWinner(copy, playerLetter):
                    return y
            y = y +1
        x = x +1
    # Computer does a random move
    move = getRandomMove(board)
    if move != None:
        return move

def isBoardFull(board):
    # Return True if every space on the board has been taken, otherwise return False
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

#################### MAIN FUNCTION ####################
while True:
    # Reset the board
    theBoard = []
    for i in range(6):
        theBoard.append([' '] * 7)

    os.system('clear')
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    waitUser = raw_input('\nPress Enter to continue...');
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            # Player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
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
            # Computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

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
