class animation():
    def __init__(self,num, length, frames):
        self.number = num
        self.length = length
        self.frames = frames
        self.currentFrame = 0
        self.iteration = 0

    def run(self):
        if(self.currentFrame  < self.length):
            self.currentFrame += 1
        else:
            self.iteration += 1
            self.currentFrame = 0
        return self.frames[self.currentFrame]