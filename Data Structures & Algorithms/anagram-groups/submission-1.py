class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = [[]]
        index = 0;
        result[0].append(strs[0])
        for element in strs[1:]:
            i = 0
            done = False
            while(i<=index):
                if(sorted(element) == sorted(result[i][0])):
                    result[i].append(element)
                    done = True
                i+=1

            if(done!=True):
                index += 1
                result.append([])
                result[index].append(element)

        return result


            

         

