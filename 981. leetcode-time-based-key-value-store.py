class TimeMap:

    def __init__(self):
        self.hashmap = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.hashmap.get(key, [])
        


        left = 0
        right = len(values)

        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res 