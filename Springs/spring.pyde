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

def setup():
    size(300,300) # Sets the size of the window

    
def draw():
    background(234);  # Sets the background colour to (234, 234, 234)
    
    for k in range(len(balls)): # a loop to only make the balls interact with the one before and one after
        if k-1 >= 0:
            balls[k].interact(balls[k-1], 3.0, 30)
            line(balls[k].x, balls[k].y, balls[k-1].x, balls[k-1].y)
        if k+1 < len(balls):
            balls[k].interact(balls[k+1], 3.0, 30)
            line(balls[k].x, balls[k].y, balls[k+1].x, balls[k+1].y)
    
    for k in range(1,len(balls)): # loop through all ball-objects in the "balls"-array
        balls[k].applyForce(-balls[k].vx*0.2, -balls[k].vy*0.2) # a small air-resistance to stop the bouncing
        balls[k].applyForce(0, 10) # Applying a downwards force to each ball.
        balls[k].update(0.1) # Updating the position of each ball, dt = 0.1
        balls[k].show() # tell the ball to show itself on the screen.
    
    if len(balls) > 0: # if the list is empty, do nothing.
        balls[0].show() # do not update() the first ball, only show it.
    
    if mousePressed:
        if mouseButton == RIGHT: # checks if the right mouse button was activated
            for b in balls: # for every ball-object in the balls-array
                l = dist(mouseX, mouseY, b.x, b.y) # calculate the distance to the ball-object from the mouse
                if l < 20: # check if the distance is smaller than 20 pixels
                    f = 50 # set the force-strength
                    b.applyForce(f*(mouseX - pmouseX), f*(mouseY - pmouseY)) # apply a force in the direction the mouse is moving
                    
            fill(200,50,50) # set the colour to red
            ellipse(mouseX, mouseY, 30,30) # draws an ellipse at the mouse


def mouseClicked():
    
     if mouseButton == LEFT:  # checks if the left-mouse button was activated
            b = Ball(mouseX, mouseY, 10) # creates a new ball at the location of the mouse
            balls.append(b) # adds the new ball-object to the balls-array
    