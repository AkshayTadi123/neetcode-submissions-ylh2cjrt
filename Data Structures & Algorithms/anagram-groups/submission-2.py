class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

       result = defaultdict(list)
       for string in strs:
            charCount = [0]*26
            for char in string:
                charCount[ord(char)-ord('a')]+=1
            key = tuple(charCount)
            result.setdefault(key, []).append(string)

       return result.values()


            

         

