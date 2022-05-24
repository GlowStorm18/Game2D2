import Board 
import Goal
import User
import os
class Game:
    def __init__(self,p_chr,p_name,g_chr):
        self.__userObject=User.User(p_chr,p_name)
        self.__GoalObject=Goal.Goal(g_chr)
        self.__BoardObject=Board.Board()

    def Play(self):
        while self.__userObject.GetPoints()>5:
            os.system("cls")
            self.__userObject.SetPosition(2,1)
            self.__GoalObject.SetPosition(0,2)
            self.__BoardObject.SetPosition(self.__userObject)
            self.__BoardObject.SetPosition(self.__GoalObject.GetCharacter(),self.__GoalObject.GetPosX(),self.__GoalObject.GetPosY())
            self.__BoardObject.Display()
            self.__userObject.Move()
            self.__GoalObject.Move()
            if(self.checkcollision()):
                self.__userObject.AddPoints()
                self.__GoalObject.Move()

    def checkcollision(self):
        if(self.__userObject.GetPosX() == self.__GoalObject.GetPosX()) and (self.__userObject.GetPosY() == self.__GoalObject.GetPosY()):
            return True
        else:
            return False