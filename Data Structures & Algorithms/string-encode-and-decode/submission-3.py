class Solution:

    # def encode(self, strs: List[str]) -> str:
    #     result = ""
    #     for i in range(len(strs)):
    #         result += strs[i]
    #         if (i != (len(strs)-1)):
    #             result += "*"
    #     return result

    # def decode(self, s: str) -> List[str]:
    #     result = []
    #     start = 0
    #     end = len(s)
    #     if(s == ""):
    #         return result
    #     while('*' in s[start:end]):
    #         index = s[start:end].index('*')
    #         result.append(s[start:index+start])
    #         start = start + index+1 
    #     result.append(s[start:])
    #     return result

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{len(s)}:{s}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # Read length
            j = i
            while s[j] != ':':
                j += 1
            length = int(s[i:j])
            # Read actual string
            j += 1  # skip ':'
            result.append(s[j:j + length])
            i = j + length
        return result


        
