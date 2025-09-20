class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        s=set(sentence)
        for i in s:
            alphabets.remove(i)
        if alphabets==[]:
            return True
        else:
            return False

        