class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        table = [[float('inf')]*(len(word2)+1) for i in range(len(word1)+1)]
        
        for i in range(len(word1)+1):
            table[i][len(word2)] = len(word1) - i
        
        for i in range(len(word2)+1):
            table[len(word1)][i] = len(word2) - i

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    table[i][j] = table[i+1][j+1]
                else:
                    table[i][j] = 1+ min(table[i+1][j+1], table[i+1][j], table[i][j+1])

        return table[0][0]