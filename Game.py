import Board
import User
import Goal
import os

class Game:
    def __init__(self, p_char, p_name, g_char):
        self.__UserObject = User.User(p_char, p_name)
        self.__GoalObject = Goal.Goal(g_char)
        self.__BoardObject = Board.Board()
    def Play(self):
        #starting pos
        self.__UserObject.SetPosition(2, 1)
        self.__GoalObject.SetPosition(0, 2)

        while self.__UserObject.GetPoints() < 4:
            os.system("cls")
            self.__BoardObject.Reset()
            print(self.__UserObject.GetPoints())
            self.__BoardObject.SetPosition(self.__UserObject.GetCharacter(), self.__UserObject.GetPosX(), self.__UserObject.GetPosY())
            self.__BoardObject.SetPosition(self.__GoalObject.GetCharacter(), self.__GoalObject.GetPosX(), self.__GoalObject.GetPosY())
            self.__BoardObject.Display()
            self.__UserObject.Move()
            if(self.CheckColision()):
                self.__UserObject.AddPoints()
                self.__GoalObject.Move()
            

    def CheckColision(self):
        if self.__GoalObject.GetPosX() == self.__UserObject.GetPosX() and self.__GoalObject.GetPosY() == self.__UserObject.GetPosY():
            return True
        else:
            return False