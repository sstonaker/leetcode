class UndergroundSystem:

    def __init__(self):
        self.checked_in = {}  # id -> (startStation, time)
        self.total = {}  # (start, end) -> [totalTime, count]

    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.checked_in[id] = (startStation, t)

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        startStation, time = self.checked_in[id]
        route = (startStation, endStation)
        if route not in self.total:
            self.total[route] = [0, 0]
        self.total[route][0] += t - time
        self.total[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.total[(startStation, endStation)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
