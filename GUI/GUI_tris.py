## GUI tris

from tkinter import *  
from tkinter import ttk  
from functools import partial

# definisco valore segno
#(serve a determinare il simbolo del segno X o O) e label

sign_value = 0
array = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]

# main
def main():
    root = Tk()
    root.wm_iconbitmap("favicon.ico")
    app = App(root)

# determina la vittoria
def iswin(label, number_now, sign):
    finisch = False

    ''' Analizzo righe '''
    for r in label:
        count = 0
        symbol = r[0]
        for s in r:
            if s == symbol:
                count = count + 1
        if count == number_now and symbol == sign:
                finisch = True

    ''' Analizzo colonne '''
    for n in range(3):

        count = 0
        symbol = label[0][n]
        for r in label:
            if r[n] == symbol:
                count = count + 1
        if count == number_now and symbol == sign:
            finisch = True

    ''' Analizzo diagonali '''
    for n in range(2):
        if n == 0:
            i = 0
        else:
            i = -1
        if n == 0:
            symbol = label[0][n]
        else:
            symbol = label[0][n+1]
        count = 0
        for r in label:
            if r[i] == symbol:
                count = count + 1
            if i >= 0:
                i = i + 1
            else:
                i = i - 1
        if count == number_now and symbol == sign:
            finisch = True

    return finisch

# App
class App:  
    def __init__(self, root):
        root.geometry("150x100")
        self.frame = Frame(root)
        self.frame.pack(
            ipadx = "10m",
            ipady = "10m"
            )
        for pos in range(9):
            myrow, mycolumn = (pos // 3, pos % 3)
            self.p = Button(self.frame,
                            padx = 4,
                            pady = 4,
                            width = 4,
                            )
            self.p["command"] = partial(self.manageFrame, self.p, myrow, mycolumn, root)
            self.p.bind("<Return>", self.manageFrame)
            self.p.grid(column = mycolumn, row = myrow)
    
    def manageFrame(self, button, row, column, root):
        global sign_value#
        global label###### rendo globali sign_value e label

        # definisco variabile contenente il segno attuale
        sign = ""
        # Determino il segno
        if len(button["text"]) == 0:
            if sign_value % 2 == 0:
                button["text"] = "X"
            else:
                button["text"] = "O"
            sign = button["text"]
            sign_value = sign_value + 1
            

        # Inserisco il segno all'interno della matrice
        array[row][column] = button["text"]

        if iswin(array, 3, sign):
            root.destroy()
            print(sign + " player win")

# Avvio programma
if __name__ == "__main__":
    main()



