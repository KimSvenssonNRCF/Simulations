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
        
        self.oldX = x
        self.oldY = y
        
        
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
        
        fraction = 0.3

        self.vx = self.vx*fraction + (self.x - self.oldX)/dt*(1-fraction)
        self.vy = self.vy*fraction + (self.y - self.oldY)/dt*(1-fraction)
        
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
        
        self.oldX = self.x
        self.oldY = self.y
        
        

    # hard solid sphere interaction
    # momentum conserved
    # http://www.gamasutra.com/view/feature/131424/pool_hall_lessons_fast_accurate_.php?page=3
    
    def interact(self, b, dt):

        # calculates the distance between balls
        l = dist(self.x, self.y, b.x, b.y)
        
        # if the distance is smaller than the sum of the radii
        # proceed to calculate the interactions
        if l < b.r + self.r and l != 0:
            
            # get the normal vector from the surface. 
            # The normal vector is the same as the direction vector
            # between the two balls
            dx = (self.x - b.x)/(l + 0.01)
            dy = (self.y - b.y)/(l + 0.01)
        
            # calculate the direction and magnitude of this ball velocity
            vl1 = dist(self.vx, self.vy, 0,0)
            dvx1 = (self.vx)/(vl1 + 0.01)
            dvy1 = (self.vy)/(vl1 + 0.01)
            
            # calculate the direction and magnitude of other ball velocity
            vl2 = dist(b.vx, b.vy, 0,0)
            dvx2 = (b.vx)/(vl2 + 0.01)
            dvy2 = (b.vy)/(vl2 + 0.01)
            
            # Calculates the overlap between ball 1 and 2
            dr = abs(b.r + self.r - l)
            
            # displaces the balls so that they don't overlap.
            self.x = self.x + dr*dx*b.m/(self.m + b.m)
            self.y = self.y + dr*dy*b.m/(self.m + b.m)
            b.x = b.x - dr*dx*self.m/(self.m + b.m)
            b.y = b.y - dr*dy*self.m/(self.m + b.m)
            
            # calculates the projection of the velocity vector on
            # the normal vector
            a1 = dvx1*dx + dvy1*dy
            a2 = dvx2*dx + dvy2*dy
            
            # calculates the force, based on the projections of the 
            # velocity vector and normal vector
            # This formula kan be obtained by setting the momentum before
            # and the momentum after the collision to be the same and
            # retrieving the new velocities.
            # the new velocities are muliplied by the mass and divided by dt.
            # this gives a Force, which is the magnitude of the force the particles
            # feels. These are then multiplied by the normal vector.
            F = (2.0*(a1 - a2)/(self.m + b.m))*self.m*b.m/dt
            
            self.applyForce(-F*dx, -F*dy)
            b.applyForce(F*dx, F*dy)
        
       