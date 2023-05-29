class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = {"1": big, "2": medium, "3": small}

    def addCar(self, carType: int) -> bool:
        if self.spaces[str(carType)] > 0:
            self.spaces[str(carType)] -= 1
            return True
        return False
