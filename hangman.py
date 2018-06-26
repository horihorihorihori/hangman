import os
os.path.join("C:","Users","BYP001944","Desktop","python","st.txt")


def hangman(word):
    wrong = 0
    strages = ["",
               " ________     ",
               "|             ",
               "|    |        ",
               "|    0        ",
               "|   /|\       ",
               "|    /\       ",
               "|             "]
    reletters = list(word)
    board = ["_"] * len(word)
    win = False
    print ("ようこそ")
    
    while wrong < len(strages) -1:
        print("\n")
        msg = "文字入力"
        char = input(msg)
        if char in reletters:
            cind = reletters.index(char)
            board[char] = char
            reletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(strages[0:e]))
        if "_" not in board:
            print("win")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(strages[0:wrong+1]))
        print("NG anwser {}".format(word))

hangman("cat")
