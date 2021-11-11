class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = ["a","e","i","o","u"]
        
        vowelsCopy = vowels[:]
        count = 0
        i = -1
        repeats = 1
        lastIndex = -1
    
        for n in range(len(word)):
            e = word[n]
            if e in vowelsCopy:
                vowelsCopy.remove(e)
                if i == -1:
                    i = n
                
                if not vowelsCopy:
                    count += 1
                    lastIndex = i + 1
                print(vowels, vowelsCopy)
            else:
                if vowelsCopy:
                    i = -1
                    vowelsCopy = vowels[:]
                    repeats = 1
                    lastIndex = -1
                    
                else:
                    if e in vowels:
                        if e in word[i: lastIndex + 1]:
                            repeats += 1
                            lastIndex = word.index(e, i, lastIndex + 1)
                            
                        count += repeats
                    print("____", count, repeats, lastIndex)
                        
        return count