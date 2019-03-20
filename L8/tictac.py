from tkinter import *
from tkinter import messagebox
import random

#We define a TTT class here:
class TTT():
    # It has an object variable called "board" that remembers
    # who has made what moves. We use a 9 element long 1D data structure
    # to make calculations easier. On-Screen, it's represented with a 3x3
    # grid.
    board = [ " ", " ", " ", " ", " ", " ", " ", " ", " "]


    #This is the constructor. It draws the window with the 9 buttons.
    def __init__(self, tkMainWin):
        frame = Frame(tkMainWin)
        frame.pack()
        self.huPlayer = "X"
        self.aiPlayer = "O"

        self.B00 = Button(frame)
        self.B00.bind("<ButtonRelease-1>", self.clicked)
        self.B00.grid(row=0,column=0)
        self.B00.config(width=10, height=5)

        self.B01 = Button(frame)
        self.B01.bind("<ButtonRelease-1>", self.clicked)
        self.B01.grid(row=0, column=1)
        self.B01.config(width=10, height=5)

        self.B02 = Button(frame)
        self.B02.bind("<ButtonRelease-1>", self.clicked)
        self.B02.grid(row=0, column=2)
        self.B02.config(width=10, height=5)

        self.B10 = Button(frame)
        self.B10.bind("<ButtonRelease-1>", self.clicked)
        self.B10.grid(row=1,column=0)
        self.B10.config(width=10, height=5)

        self.B11 = Button(frame)
        self.B11.bind("<ButtonRelease-1>", self.clicked)
        self.B11.grid(row=1, column=1)
        self.B11.config(width=10, height=5)

        self.B12 = Button(frame)
        self.B12.bind("<ButtonRelease-1>", self.clicked)
        self.B12.grid(row=1, column=2)
        self.B12.config(width=10, height=5)

        self.B20 = Button(frame)
        self.B20.bind("<ButtonRelease-1>", self.clicked)
        self.B20.grid(row=2,column=0)
        self.B20.config(width=10, height=5)

        self.B21 = Button(frame)
        self.B21.bind("<ButtonRelease-1>", self.clicked)
        self.B21.grid(row=2,column=1)
        self.B21.config(width=10, height=5)

        self.B22 = Button(frame)
        self.B22.bind("<ButtonRelease-1>", self.clicked)
        self.B22.grid(row=2,column=2)
        self.B22.config(width=10, height=5)

        # Set the text for each of the 9 buttons.
        # Initially, to all Blanks!
        self.redrawBoard()

    #This event handler (callback) will figure out which of the 9 buttons
    #were clicked, and call the "userMove" method with that move position.
    def clicked(self, event):
        if event.widget == self.B00:
            self.userMove(0)
        elif event.widget == self.B01 :
            self.userMove(1)
        elif event.widget == self.B02 :
            self.userMove(2)
        elif event.widget == self.B10 :
            self.userMove(3)
        elif event.widget == self.B11:
            self.userMove(4)
        elif event.widget == self.B12 :
            self.userMove(5)
        elif event.widget == self.B20 :
            self.userMove(6)
        elif event.widget == self.B21 :
            self.userMove(7)
        elif event.widget == self.B22 :
            self.userMove(8)

    #When a button signals that the user has tried to make a move by
    # clicking, we check to see if that move is valid. If it is, we
    # need to check to see if the user has won. If they have not, we
    # need to make our move, and check to see if the computer has won.
    # We also redraw the board after each move.
    def userMove(self, pos):

        #Is this a valid move?
        if self.board[pos] == " ":
            #Record the players move...
            self.board[pos] = "X"
            #Then redraw the board!
            self.redrawBoard()

            #Check to see if the user won!
            if self.playerWon(self.board, self.huPlayer):
                messagebox.showinfo("Game over", "Human won")
                self.gameOver()
            elif len(self.emptyIndexes(self.board)) == 0:
                messagebox.showinfo("Game over", "It is a tie!")
                self.gameOver()
            else:
                #Make our move!
                self.computerMove()

                #Check to see if the computer won!
                if self.playerWon(self.board, self.aiPlayer):
                    messagebox.showinfo("Game over", "AI won")
                    self.gameOver()

                #Then redraw the board!
                self.redrawBoard()

        else:   #Move is NOT valid! Don't do anything!
            messagebox.showwarning("Invalid Move","I'm sorry, that move is not valid!")



    # TODO: Make our move smarter!
    # This method will make a move for the computer.
    # It is VERY simplistic, as it just picks the first
    # valid move from an ordered list of preferred moves.
    def computerMove(self):
        emptySpaces = self.emptyIndexes(self.board)
        random.shuffle(emptySpaces)
        move = emptySpaces[0]
        self.board[move] = "O"
        return


    #This method will update the text displayed by
    # each of the 9 buttons to reflect the "board"
    # object variable.
    def redrawBoard(self):
        self.B00.config( text = self.board[0])
        self.B01.config( text = self.board[1])
        self.B02.config( text = self.board[2])
        self.B10.config( text = self.board[3])
        self.B11.config( text = self.board[4])
        self.B12.config( text = self.board[5])
        self.B20.config( text = self.board[6])
        self.B21.config( text = self.board[7])
        self.B22.config( text = self.board[8])

    #This method checks if user worn
    def playerWon(self, board, symbol):
        if (
                (board[0] == symbol and board[1] == symbol and board[2] == symbol) or
                (board[3] == symbol and board[4] == symbol and board[5] == symbol) or
                (board[6] == symbol and board[7] == symbol and board[8] == symbol) or
                (board[0] == symbol and board[3] == symbol and board[6] == symbol) or
                (board[1] == symbol and board[4] == symbol and board[7] == symbol) or
                (board[2] == symbol and board[5] == symbol and board[8] == symbol) or
                (board[0] == symbol and board[4] == symbol and board[8] == symbol) or
                (board[2] == symbol and board[4] == symbol and board[6] == symbol)
        ):
            return True
        else:
            return False

    #This method disable the buttons after game over
    def gameOver(self):
        self.B00.unbind("<ButtonRelease-1>")
        self.B00.config(state="disabled")
        self.B01.unbind("<ButtonRelease-1>")
        self.B01.config(state="disabled")
        self.B02.unbind("<ButtonRelease-1>")
        self.B02.config(state="disabled")
        self.B10.unbind("<ButtonRelease-1>")
        self.B10.config(state="disabled")
        self.B11.unbind("<ButtonRelease-1>")
        self.B11.config(state="disabled")
        self.B12.unbind("<ButtonRelease-1>")
        self.B12.config(state="disabled")
        self.B20.unbind("<ButtonRelease-1>")
        self.B20.config(state="disabled")
        self.B21.unbind("<ButtonRelease-1>")
        self.B21.config(state="disabled")
        self.B22.unbind("<ButtonRelease-1>")
        self.B22.config(state="disabled")

    # returns list of the indexes of
    # empty spots on the board function
    def emptyIndexes(self, board):
        arr = []
        for i, val in enumerate(board, start=0):
            if val == ' ':
                arr.append(i)
        return arr