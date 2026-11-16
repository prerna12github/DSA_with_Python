class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:

        conword1 = ""
        conword2 = ""
        for i in range(len(word1)):
            conword1 = conword1 + word1[i]
        for j in range(len(word2)):
            conword2 = conword2 + word2[j]
        return conword1 == conword2        

        