class Ball(object):
    def __init__(self, x,y,dx,dy,radius,color):
        self.x = x
        self.y = y
        self.dx = dx 
        self.dy = dy
        self.radius = radius
        self.color = color
    def position(self):
        return (self.x, self.y)
    def move(self):
        self.x += self.dx
        self.y += self.dy
    def get_color(self):
        return self.color
    def bounding_box(self):
        return (self.x-self.radius, 
                self.y-self.radius,\
                self.x+self.radius, \
                self.y+self.radius)
    
    def some_inside(self, max_x, max_y):
        if 0 < self.x + self.radius and \
              self.x - self.radius < max_x and \
              0 < self.y + self.radius and \
              self.y - self.radius < max_y:
            return True
        else:
            return False
        
    def check_and_reverse(self, max_x, max_y):
        if 0 >= self.x - self.radius or \
           self.x + self.radius >= max_x:
            self.dx = -(self.dx)
        if 0 >= self.y - self.radius or \
             self.y + self.radius >= max_y:
            self.dy = -(self.dy)