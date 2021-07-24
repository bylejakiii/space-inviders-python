class Progress:
    def __init__(self):
        try:
            file = open('game_progress.bin', 'rb')
            a_val = []
            for line in file:
                s = line.decode()
                s = s[:-1]
                a_val.append(s)
            file.close
        except:
            a_val = ["1", "0"]  # odpowiednio: odblokowany lvl oraz game coins
            file = open('game_progress.bin', 'wb')
            for item in a_val:
                bt = (item + "\n").encode()
                file.write(bt)
            file.close()
        self.level = int(a_val[0])
        self.cash = int(a_val[1])

    def save_game(self):
        a_val = [str(self.level), str(self.cash)]
        file = open('game_progress.bin', 'wb')
        for item in a_val:
            bt = (item + "\n").encode()
            file.write(bt)
        file.close()


# values = ('1', '0')
# file = open('game.bin', 'wb')
# for item in values:
#     bt = (item + '\n').encode()
#     file.write(bt)
# file.close()
#
# f = open('game.bin', 'rb')
#
# for line in f:
#     s = line.decode()
#     print(s)
