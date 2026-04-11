class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs)):
            if(len(strs[i]) < 10):
                add = "00" + str(len(strs[i]))
            elif(len(strs[i]) < 100):
                add = "0" + str(len(strs[i]))
            else:
                add = str(len(strs[i]))
            result +=  add + "*" + strs[i]
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 3
        while i<len(s):
            if( s[i] == '*'):
                result.append(s[i+1:i+1+int(s[i-3:i])])
                i += int(s[i-3:i])
            i += 1
        
        return result

    # def encode(self, strs: List[str]) -> str:
    #     result = ""
    #     for s in strs:
    #         result += f"{len(s)}:{s}"
    #     return result

    # def decode(self, s: str) -> List[str]:
    #     result = []
    #     i = 0
    #     while i < len(s):
    #         # Read length
    #         j = i
    #         while s[j] != ':':
    #             j += 1
    #         length = int(s[i:j])
    #         # Read actual string
    #         j += 1  # skip ':'
    #         result.append(s[j:j + length])
    #         i = j + length
    #     return result


        
