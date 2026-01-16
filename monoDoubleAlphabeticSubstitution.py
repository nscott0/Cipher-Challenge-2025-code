import random
class monoDoubleAlphabeticSubstitution():
    def __init__(self,cipher1,cipher2):
        self.__cipher1 = cipher1
        self.__cipher2 = cipher2
        self._key1 = {}
        self._key2 = {}
        for i in range(26):
            self._key1[i] = i
            self._key2[i] = i
        self._key1shuffled = False

    def printKey(self):
        print(self._key1,self._key2)

    def getKey(self):
        return self._key1,self._key2

    def getNumberOfKeys(self):
        return 2

    def injectKey(self,key1,key2):
        self._key1 = key1
        self._key2 = key2

    def shuffle(self):
        self._letters = random.sample(range(26), k=2)
        if random.random() < 0.5:
            self._key1[self._letters[0]],self._key1[self._letters[1]] = self._key1[self._letters[1]],self._key1[self._letters[0]]
            self._key1shuffled = True
        else:
            self._key2[self._letters[0]], self._key2[self._letters[1]] = self._key2[self._letters[1]], self._key2[self._letters[0]]
            self._key1shuffled = False

    def undoShuffle(self):
        if self._key1shuffled:
            self._key1[self._letters[0]],self._key1[self._letters[1]] = self._key1[self._letters[1]],self._key1[self._letters[0]]
        else:
            self._key2[self._letters[0]], self._key2[self._letters[1]] = self._key2[self._letters[1]], self._key2[self._letters[0]]

    def decipher(self):
        plainText = []
        for a in range(len(self.__cipher1)):
            plainText.append(self._key1[self.__cipher1[a]])
            plainText.append(self._key2[self.__cipher2[a]])
        return plainText
