class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]

        result = [[1], [1, 1]]

        if numRows == 2:
            return result

        for i in range(2, numRows):
            temp = [1]

            for j in range(1, i):
                temp.append(result[i-1][j-1] + result[i-1][j])

            temp.append(1)
            result.append(temp)

        return result

