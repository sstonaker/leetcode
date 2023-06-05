class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        last = coordinates.pop()
        first = coordinates.pop()
        try:
            previous_slope = (last[1] - first[1]) / (last[0] - first[0])
        except ZeroDivisionError:
            previous_slope = 0
        while coordinates:
            first = coordinates.pop()
            try:
                slope = (last[1] - first[1]) / (last[0] - first[0])
            except ZeroDivisionError:
                slope = 0
            if slope != previous_slope:
                return False
        return True
