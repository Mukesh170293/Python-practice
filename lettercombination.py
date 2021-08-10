class Solution:
    def letterCombinations(self, digits):
        combinations = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        result = []
        if(len(digits) == 0):
            return []
        elif(len(digits) == 1):
            return combinations[digits]
        elif(len(digits) == 2):
            result = [x+y for x in combinations[digits[0]] for y in combinations[digits[1]]]
        elif(len(digits) == 3):
            result = [x+y for x in combinations[digits[0]] for y in combinations[digits[1]]]
            result = [x+y for x in combinations[digits[2]] for y in result]
        elif(len(digits) == 4):
            result = [x+y for x in combinations[digits[0]] for y in combinations[digits[1]]]
            result = [x+y for x in combinations[digits[2]] for y in result]
            result = [x+y for x in combinations[digits[3]] for y in result]
        return result


s = Solution()
print(s.letterCombinations("2345"))
