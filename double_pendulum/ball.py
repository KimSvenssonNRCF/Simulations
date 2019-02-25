#
# Written by: Kim Svensson
#             Lund University 2018
#
# The ideas in this simulation are an amalgamation of
# many different simulations and courses.
#
# Use this code as is.



# The Ball-class
# Keeps track of its:
#  position     (x,   y)
#  velocity     (vx, vy)
#  acceleration (ax, ay)
#  mass
#  radius
#
# it has the following methods:
#
#  show(self): 
#  - draws an ellipse in the window.
#  
#  applyForce(self, fx, fy): 
#  - calculates the acceleration from the forces fx and fy.
#
#  update(self, dt):
#  - calculates the new position of the ball using Eulers methods
#  - http://tutorial.math.lamar.edu/Classes/DE/EulersMethod.aspx
#  - It also calculates and applies a force to the ball if it touches 
#  - the edges of the window.

class Ball:
    
    def __init__(self, x, y, r):
        self.x = x 
        self.y = y
        self.r = r
        self.m = 1.0  
              
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        
        
    def show(self):
        fill(20,100,30)
        ellipse(self.x, self.y, self.r*2 , self.r*2)
        
        
    def applyForce(self, fx, fy):
        self.ax += fx/self.m
        self.ay += fy/self.m
        
        
    def update(self, dt):
        self.vx += self.ax*dt
        self.vy += self.ay*dt
        self.x += self.vx*dt
        self.y += self.vy*dt
        self.ax = 0
        self.ay = 0
        
        if self.x + self.r > width or self.x - self.r < 0:
            self.applyForce(-2*self.vx*self.m/dt, 0)
            if self.x + self.r > width:
                self.x = width - self.r
            else:
                self.x = self.r
                            
        if self.y + self.r > height or self.y - self.r < 0:
            self.applyForce(0, -2*self.vy*self.m/dt)
            if self.y + self.r > height:
                self.y = height - self.r
            else:
                self.y = self.r
        
        
    # Spring interaction
    # uses Hooke's Law: F = x*k
    def interact(self, b, k, dl):
        l = dist(self.x, self.y, b.x, b.y) # gets the distance between the two balls
        
        F = (dl - l)*k # calculates the magnitude of the force
        dx = (self.x - b.x)/(l + 0.01) # x-component of the direction
        dy = (self.y - b.y)/(l + 0.01) # y-component of the direction
        
        self.applyForce(F*dx, F*dy) # applies the force to this ball.
        
        