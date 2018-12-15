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
    b = Ball(width/2, height/2, 10)  # creates a ball at the middle of the window with radius 10  
    balls.append(b) # add the ball-object to the balls-array
    
    
def draw():
    background(234);  # Sets the background colour to (234, 234, 234)
    
    for b in balls: # loop through all ball-objects in the "balls"-array
        b.applyForce(0, 10) # Applying a downwards force to each ball.
        b.update(0.1) # Updating the position of each ball, dt = 0.1
        b.show() # tell the ball to show itself on the screen.
        
    
def mouseClicked():  # runs if any button on the mouse was clicked
    if mouseButton == LEFT:  # checks if the left-mousebutton was activated
        b = Ball(mouseX, mouseY, 10) # creates a new ball at the location of the mouse
        balls.append(b) # adds the new ball-object to the balls-array
    