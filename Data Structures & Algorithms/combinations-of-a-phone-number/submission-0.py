class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        hashmap = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
        result = []
        
        def helper(i, current_string):
            if(len(current_string) == len(digits)):
                result.append(current_string)
            else:
                for char in hashmap[digits[i]]:
                    helper(i+1, current_string + char)
        
        helper(0, "")
        return result



