#
# Written by: Kim Svensson
#             Lund University 2018
#
# The ideas in this simulation are an amalgamation of
# many different simulations and courses.
#
# Use this code as is.


from ball import Ball  # Imports the Ball-class from the ball.py tab

balls = [] # Create an array to keep the ball-objects in.
history = [] # Create an array to save the history of the furthest ball.

def setup():
    size(300,300) # Sets the size of the window
    b1 = Ball(width/2 , 150, 10)
    balls.append(b1)
    b2 = Ball(width/2 , 150 - 80, 10)
    b2.m = 3.0
    balls.append(b2)
    b3 = Ball(width/2 +50, 150 - 80, 10)
    b3.m = 3.0
    balls.append(b3)
    
def draw():
    background(234);  # Sets the background colour to (234, 234, 234)
    
    for n in range(1000):
        
        balls[0].interact(balls[1], 10000.0, 80.0)
        balls[1].interact(balls[0], 10000.0, 80.0)
        balls[1].interact(balls[2], 10000.0, 50.0)
        balls[2].interact(balls[1], 10000.0, 50.0)
        
        for k in range(1,len(balls)): # loop through all ball-objects in the "balls"-array
            balls[k].applyForce(-balls[k].vx*0.01, -balls[k].vy*0.01) # a small air-resistance to stop the bouncing
            balls[k].applyForce(0, 10*balls[k].m) # Applying a downwards force to each ball.
            balls[k].update(0.0002) # Updating the position of each ball, dt = 0.0002
       
    # Draw lines between the balls in the balls-array.
    stroke(0, 255)
    for k in range(len(balls)): 
        if k+1 < len(balls):
            line(balls[k].x, balls[k].y, balls[k+1].x, balls[k+1].y)      
        
        
    drawHistory() # draws the history of the furthest ball
    stroke(0, 255)
    for k in range(len(balls)):
        balls[k].show() # tell the ball to show itself on the screen.
    

    if mousePressed:
        if mouseButton == RIGHT: # checks if the right mouse button was activated
            for b in balls: # for every ball-object in the balls-array
                l = dist(mouseX, mouseY, b.x, b.y) # calculate the distance to the ball-object from the mouse
                if l < 20: # check if the distance is smaller than 20 pixels
                    f = 50000 # set the force-strength
                    b.applyForce(f*(mouseX - pmouseX), f*(mouseY - pmouseY)) # apply a force in the direction the mouse is moving
                    
            fill(200,50,50) # set the colour to red
            ellipse(mouseX, mouseY, 30,30) # draws an ellipse at the mouse


# Draws the history of the furthest ball
def drawHistory(): 
    bn = Ball(balls[2].x, balls[2].y, 1.0) # create a copy of the furthest ball
    history.append(bn) # append the copy to the history-array
    if len(history) > 400: # if the history-array is longer than 400 points, remove the first one
        history.pop(0) # remove the first entry of the array
    for i in range(len(history) -1): # for loop over the history array
        stroke(0, map(i, 0, 400, 0, 255)) # map the transparancy to the position in the list
        line(history[i].x, history[i].y, history[i+1].x, history[i+1].y) # draw a line between two different points in the history-array
    
    
    
    