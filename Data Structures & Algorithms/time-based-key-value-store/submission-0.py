class TimeMap:

    def __init__(self):
            self.map1 = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map1[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        temp = self.map1[key]
        closest = -1
        reqIndex = -1
        for i in range(len(temp)):
            if (temp[i][1] == timestamp):
                return temp[i][0]
            elif(temp[i][1]>timestamp):
                continue
            else:
                if closest<temp[i][1]:
                    reqIndex = i
                    closest = temp[i][1]
        if reqIndex == -1:
            return ""
        else:
            return temp[reqIndex][0]

