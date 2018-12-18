#
# Written by: Kim Svensson
#             Lund University 2018
#
# The ideas in this simulation are an amalgamation of
# many different simulations and courses.
#
# Use this code as is.


from ball import Ball  # Imports the Ball-class from the ball.py tab

balls = [] # Create a array to keep the ball-objects in.


# sets the dimensions of the grid
# odd numbers are chosen to easily attach the edges using k%2 == 0
w = 41 # nr of balls in the x-direction
h = 41 # nr of balls in the y-direction
s = (300-60)/w # distance between the balls, spring equilibrium distance

def setup():
    size(300,300) # Sets the size of the window
    
    # Creates a grid of balls and store them in the balls-array
    for x in range(w):
        for y in range(h):
            b = Ball(x*(300-60)/w + 30, y*(300-60)/h + 30, 5)
            balls.append(b);
    

    
def draw():
    background(234);  # Sets the background colour to (234, 234, 234)
          
    
    # Loops through all the different balls in the grid
    # Does this 10 times per frame, to create a faster animation only the tenth step of 
    # the simulation is drawn.
    for u in range(10):     
        for k in range(w):
            for n in range(h):
                
                # extracts the index for the four neighbouring balls
                i = n + k*w
                i1 = n-1 + k*w
                i2 = n+1 + k*w
                i3 = n + (k-1)*w
                i4 = n + (k+1)*w
                
                # interacts with neighbour, if neighbour exists
                if k-1 >= 0:
                    balls[i].interact(balls[i3], 1000/s, s)

                if k+1 < w:
                    balls[i].interact(balls[i4], 1000/s, s)

                if n-1 >= 0:
                    balls[i].interact(balls[i1], 1000/s, s)

                if n+1 < h:
                    balls[i].interact(balls[i2], 1000/s, s)

        for k in range(w):
            for n in range(h):
                i = k + n*w
                if n%2 != 0 or k != 0:
                    balls[i].applyForce(-balls[i].vx*0.2, -balls[i].vy*0.2) # a small air-resistance to stop the bouncing
                    balls[i].applyForce(0, 10*balls[i].m) # Applying a downwards force to each ball.
                    balls[i].update(0.02) # Updating the position of each ball, dt = 0.02
           
    
    
    #Separate the drawing of the simulation from the physics of the simulation
    #instead of drawing the balls, only the springs between the balls are drawn
    for k in range(w):
        for n in range(h):            
            
            i = n + k*w
            i1 = n-1 + k*w
            i2 = n+1 + k*w
            i3 = n + (k-1)*w
            i4 = n + (k+1)*w
            
            #Draws a line if a ball exists
            if k-1 >= 0:
                line(balls[i].x, balls[i].y, balls[i3].x, balls[i3].y)
            if k+1 < w:
                line(balls[i].x, balls[i].y, balls[i4].x, balls[i4].y)
            if n-1 >= 0:
                line(balls[i].x, balls[i].y, balls[i1].x, balls[i1].y)
            if n+1 < h:
                line(balls[i].x, balls[i].y, balls[i2].x, balls[i2].y)


    
    if mousePressed:
        if mouseButton == RIGHT: # checks if the right mouse button was activated
            for b in balls: # for every ball-object in the balls-array
                l = dist(mouseX, mouseY, b.x, b.y) # calculate the distance to the ball-object from the mouse
                if l < 20: # check if the distance is smaller than 20 pixels
                    f = 105 # set the force-strength
                    b.applyForce(f*(mouseX - pmouseX), f*(mouseY - pmouseY)) # apply a force in the direction the mouse is moving
                    
            fill(200,50,50) # set the colour to red
            ellipse(mouseX, mouseY, 30,30) # draws an ellipse at the mouse



    