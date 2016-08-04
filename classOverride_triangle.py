class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        pass
    
    def check_angles(self):
        if self.angle2 + self.angle2 +self.angle3 == 180:
            return True
        else:
            return False
            
class Equilateral(Triangle):
    """docstring for Equilateral"""
    angle = 60
    def __init__(self, angle1, angle2,angle3):
   		Triangle.__init__(self,angle1,angle2,angle3)
   		self.angle1 = self.angle
   		self.angle2 = self.angle
   		self.angle3 = self.angle

newTRI = Equilateral(80,70,80)

print newTRI.check_angles()
print newTRI.angle3

       
