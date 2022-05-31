import User
import Goal


class Scoreboard:
    def __init__(self):
        self.__scoreboard = {}
        self.FillTheScoreboard()
    def FillTheScoreboard(self):
        file = open("scores.txt", 'r')
        content = file.read()
        content = content[:-1]
        file.close()
        list_content = content.split(' ')
        i = 0
        while i < len(list_content):
            self.__scoreboard[list_content[i]] = int(list_content[i+1])
            i+=2
    def Display(self):
        for element in self.__scoreboard:
            print(element+ ": " + str(self.__scoreboard[element]))
    
    def Save(self, name, score):
        if name in self.__scoreboard:
            if self.__scoreboard[name] < score:
                self.__scoreboard[name] = score
        else:
            self.__scoreboard[name] = score
        file = open("scores.txt", 'w')
        for element in self.__scoreboard:
            file.write(element + " "+str(self.__scoreboard[element])+" ")
        file.close()
        