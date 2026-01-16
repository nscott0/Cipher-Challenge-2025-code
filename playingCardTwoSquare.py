# To be run in hillClimbWithMargin. Optimal conditions: margin = 0.1*length Chance to shuffle = 0.5

import random
from gridCiphers.polybiusGrid import polybiusGrid

class playingCardTwoSquare():
    def __init__(self,cipher):
        self._cipher = cipher

        self._halfLength = round(len(self._cipher)/2)

        self._grid1 = polybiusGrid([[0,1,2,3,4,5],[6,7,8,9,10,11],[12,13,14,15,16,17],[18,19,20,21,22,23],[24,25,26,27,28,29],[30,31,32,33,34,35]])
        self._grid2 = polybiusGrid([[36,37,38,39],[40,41,42,43],[44,45,46,47],[48,49,50,51]])

    def shuffle(self):
        if random.random() > 0.5:
            self.__shuffledGrid1 = True
            self._grid1.shuffle()
        else:
            self.__shuffledGrid1 = False
            self._grid2.shuffle()

    def undoShuffle(self):
        if self.__shuffledGrid1:
            self._grid1.undoShuffle()
        else:
            self._grid2.undoShuffle()

    def decipher(self):

        plainText = []

        for i in range(self._halfLength):
            coordinate1 = self._grid1.getCoordinatesOfCharacter(self._cipher[i*2])
            coordinate2 = self._grid2.getCoordinatesOfCharacter(self._cipher[i*2+1])

            plainText.append(self._grid1.getCharacterAtCoordinates(coordinate2[0],coordinate2[1])%26)
            plainText.append(self._grid2.getCharacterAtCoordinates(coordinate1[0]%4,coordinate1[1]%4)%26)

        return plainText
