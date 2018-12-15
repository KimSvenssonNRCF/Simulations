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
    
    for b1 in balls:  # go through all ball-objects in the balls-array
        for b2 in balls: # go through all ball-objects in the balls-array again
            b1.interact(b2, 0.1) # make all ball-objects interact with every other ball object.
    
    
    for b in balls: # loop through all ball-objects in the "balls"-array
        b.applyForce(0, 10) # Applying a downwards force to each ball.
        b.update(0.1) # Updating the position of each ball, dt = 0.1
        b.show() # tell the ball to show itself on the screen.
        
        
    if mousePressed:
        if mouseButton == LEFT:  # checks if the left-mouse button was activated
            b = Ball(mouseX, mouseY, 10) # creates a new ball at the location of the mouse
            balls.append(b) # adds the new ball-object to the balls-array
    
        if mouseButton == RIGHT: # checks if the right mouse button was activated
            for b in balls: # for every ball-object in the balls-array
                l = dist(mouseX, mouseY, b.x, b.y) # calculate the distance to the ball-object from the mouse
                if l < 20: # check if the distance is smaller than 20 pixels
                    f = 50 # set the force-strength
                    b.applyForce(f*(mouseX - pmouseX), f*(mouseY - pmouseY)) # apply a force in the direction the mouse is moving
                    
            fill(200,50,50) # set the colour to red
            ellipse(mouseX, mouseY, 30,30) # draws an ellipse at the mouse
        
    


    
    
    
   
        
        
        
        
        