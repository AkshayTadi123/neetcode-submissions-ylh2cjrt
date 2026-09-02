class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        index = 0
        val = None

        while not val:
            for i in range(len(strs)):

                if not val and index<len(strs[0]):
                    val = strs[0][index]

                if index in range(len(strs[i])) and strs[i][index] == val:
                    continue
                else:
                    return res
            
            res += strs[0][index]
            index += 1
            val = None