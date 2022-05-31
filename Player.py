class Player:
    def __init__(self, character):
        self._pos_x = 0
        self._pos_y = 0
        self._character = character
    def GetPosX(self):
        return self._pos_x
    def GetPosY(self):
        return self._pos_y
    def GetCharacter(self):
        return self._character
    def SetPosition(self, pos_x, pos_y):
        self._pos_x = pos_x
        self._pos_y = pos_y