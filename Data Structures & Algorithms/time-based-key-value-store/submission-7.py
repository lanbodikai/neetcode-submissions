class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []

        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        res = ""
        values = self.timeMap[key]

        l = 0
        r = len(values) - 1

        while l <= r:
            mid = (l + r) // 2

            time, value = values[mid]

            if time <= timestamp:
                l = mid + 1
                res = value
            else:
                r = mid - 1

        return res