import random
word_list = ["culo", "patacon", "atila", "macarse", "charly"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def ahorcado(word):
    wrong = 0
    stages = ["",
             "____________      1 error",
             "|           |     2 errores",
             "|           0     3 errores",
             "|          /|\    3 errores",
             "|           |     4 errores",
             "|          / \    5 errores",
             "|                 6 errores", 
              ]
    remaining_letters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Bienvenido/a al Ahorcado de tus apodos.")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Escribí una letra: "
        char = input(msg)
        char_upper = char.upper()
        if char_upper in remaining_letters:
            cind = remaining_letters.index(char_upper)
            board[cind] = char_upper
            remaining_letters[cind] = '$'
        else:
            wrong += 1
        print(("\n""Palabra:"+" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("Ganaste!!!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n""\n")
        print("Perdiste!!! La palabra era {}.".format(word))

word = get_word(word_list)
ahorcado(word)
