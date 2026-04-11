class TimeMap:

    def __init__(self):
            self.map1 = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map1[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        temp = self.map1[key]
        res = ""
        l, r = 0, len(temp) - 1
        while l <= r:
            m = (l + r) // 2
            if temp[m][1] <= timestamp:
                res = temp[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
