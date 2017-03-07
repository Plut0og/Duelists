class area():
    def __init__(self, startX, startY, width, height):
        self.start_x = startX
        self.start_y = startY
        self.width = width
        self.height = height

    def ckeckCollide(self, x, y):
        if(x > self.start_x and x < self.start_x + self.width):
            if(y > self.start_y and y < self.start_y + self.height):
                return True
        else:
            return False


class hitBox():
    def __init__(self, areas, target):
        self.areas = areas

    def checkCollide(self, x, y):
        for i, v in enumerate(self.areas):
            if(v.checkCollide):
                return True
            else:
                continue
        return False