class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        if key not in self.store:
            return res

        l, r = 0, len(self.store[key]) - 1

        while l <= r:
            m = (l + r) // 2

            if self.store[key][m][1] <= timestamp:
                res = self.store[key][m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)