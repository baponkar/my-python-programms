class Laser(object):

    def __init__(self):
        pass
    def does(self):
        #print("disintegrate")
        return 'disintegrate'

class Claw(object):
    def __init__(self):
        pass
    def does(self):
        #print("crush")
        return 'crush'

class SmartPhone(object):
    def __init__(self):
        pass

    def does(self):
       # print("ring")
        return 'ring'


class Robot():
    def __init__(self,laser,claw,smartphone):
        self.laser = laser
        self.claw = claw
        self.smartphone = smartphone

    def does(self):
        print(self.laser.does(),self.claw.does(),self.smartphone.does())

laser = Laser()
claw = Claw()
smartphone = SmartPhone()


robot = Robot(laser,claw,smartphone)

test = robot.does()
