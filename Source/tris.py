## Partita a tris tra un'utente e un IA

from random import randint

# Definisco variabili quali label(array) e coordinate per griglia
label = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
letter_coord = "abc"
possible_move = [0, 2]

# Main
def main():
    print("Tris by TheSkymer")
    print()
    stop = False
    while not(stop): #la quale determina la vincita di una partita
        if not(iswin(label,3,"o")):
            first_input = botMove(possible_move, label)
            changeLabel(label, first_input, "x")
            print(" Bob moving..")
            printLabel(label)
            print()
            if "*" not in label[0] and "*" not in label[1] and "*" not in label[2]:
                print("draw")
                break
        if iswin(label,3, "x") == True:
            print("Bob win")
            break
        second_input = input("Player: ")
        changeLabel(label, second_input, "o")
        printLabel(label)
        print()
        if "*" not in label[0] and "*" not in label[1] and "*" not in label[2]:
            print("draw")
            break
        if iswin(label,3, "o") == True:
            print("Player two win")
        stop = iswin(label,3, "o")
        
## Cambia la griglia inserendo il simbolo(o-x) nella griglia
#  @param label griglia che deve essere modificata
#  @param move coordinata nella griglia(es 1a, 3b...)
#  @param simbol simbolo da inserire nella coordinata
#
def changeLabel(label, move, simbol):
    if type(move) == type(str()):
        index_coord = defineIndexCoord(move)
    elif type(move) == type(list()):
        index_coord = move
    else:
        return 0
    line = index_coord[0]
    element = index_coord[1]
    if label[line][element] == "*":
        label[line][element] = simbol
    else:
        print("Invalid move, penality!")

## Definisce la coordinata in ingresso
#  @param coord la coordinata es 2c
#  @return la posizione nell'array(label) come lista
#  contenente la lista e l'indice all'interno della lista
#
def defineIndexCoord(coord):
    index_coord = []
    if len(coord) == 2:
        index_coord.append(int(coord[0]) - 1)
        if coord[1] == "a":
            index_coord.append(0)
        elif coord[1] == "b":
            index_coord.append(1)
        else:
            index_coord.append(2)
    return index_coord
## Stampa la variabile label come fosse una griglia del tris
#  @param label l'array da stampare a mo di griglia-tris
#
def printLabel(label):
    count = 1
    for line in label:
        print(count, end="  ")
        for element in line:
            print(element + " ", end=" ")
        count = count + 1
        print()
    print(" ", end="  ")
    for letter in letter_coord:
        print(letter, end="  ")
## Determina se una partita deve terminare
#  @param label griglia tris
#
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

# IA Bob
def botMove(possible_move, label):
    bot_move_list = []
    player_move = win_move(label, "o")
    bot_move = win_move(label, "x")
    if type(bot_move) == type(list()) and label[bot_move[0]][bot_move[1]] == "*":
        bot_move_list = bot_move

    elif type(player_move) == type(list()) and label[player_move[0]][player_move[1]] == "*":
        bot_move_list = player_move
        
    else:
        index_casual_r = possible_move[randint(0,1)]
        casual_r = label[index_casual_r]
        move = possible_move[randint(0,1)]
        while casual_r[move] != "*":
            if casual_r[move] != "*":
                index_casual_r = possible_move[randint(0,1)]
                casual_r = label[index_casual_r]
                move = possible_move[randint(0,1)]
        bot_move_list = [index_casual_r, move]
    return bot_move_list

# Mossa vincente 3 mossa Bob nn va problema win_move nelle colonne
def win_move(label, sign):
    r_win = []
    # Righe
    r_position = 0
    for r in label:
        count = 0
        for s in r:
            if s == sign:
                count = count + 1
            if count == 2:
                for n in range(3):
                    if r[n] == "*":
                        r_win  = [r_position, n]
                        return r_win
        r_position = r_position + 1
    # Colonne
    for n in range(3):
        count = 0
        index = 0
        for r in label:
            if r[n] == sign:
                count = count + 1
            if count == 2:
                s_index = 0
                for r in label:
                    if r[n] == "*":
                        r_win = [s_index, n]
                        return r_win
                    s_index = s_index + 1
            index = index + 1

    # Diagonali
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
            if r[i] == sign:
                count = count + 1
            if i >= 0:
                i = i + 1
            else:
                i = i - 1
        if count == 2:
            r_win = [1, 1]
            return r_win
# Avvio programma
main()
