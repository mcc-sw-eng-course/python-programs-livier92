from tictac import *

if __name__ == '__main__':
    # This code starts up TK and creates a main window.
    mainWin = Tk()

    # This code creates an instance of the TTT object.
    ttt = TTT(mainWin)

    mainWin.title("Tic-Tac-Toe")

    # This line starts the main event handling loop and sets us on our way...
    mainWin.mainloop()