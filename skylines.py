
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: <REDACTED>
#    Student name: Sebastian Sherry
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files may be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  SKYLINES
#
#  This task tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function,
#  "draw_buildings".  You are required to complete this function
#  so that when the program is run it produces a drawing of a city
#  skyline, using data stored in a list to determine the number,
#  proportions and styles of the buildings.  See the instruction
#  sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#  



#-----Preamble and Test Data-----------------------------------------#
#
#

# Module provided
#
# You may use only the turtle graphics functions for this task

from turtle import *


# Given constants
#
# These constant values are used in the main program that sets up
# the drawing window - do not change any of these values

window_height = 600 # pixels
window_width = 1100 # pixels
half_width = window_width / 2 # maximum x coordinate in either direction
grass_depth = 75 # vertical depth of the "grass", in pixels
max_height = window_height - grass_depth # maximum positive y coordinate
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
font_size = 10 # size of characters in the grid, in pixels
grid_size = 50 # gradations for the x and y scales shown on the screen


# Test data
#
# The following six lists each describe the set of buildings forming a city
# skyline.  The first four lists are special cases intended to help
# you debug your code (and make it easy for us to mark it).  The final
# two cases produce "realistic" looking skylines and should be
# used only when you have all of your building definitions working.
#
# Each list element specifies one building in four parts:
#
#    [width, height, x_coord_centreline, building_style]
#
# The 'width' and 'height' are the width and height of the building's main
# structure (including the roof, but excluding "add-ons" such as chimneys,
# antennae, etc).  The 'x_coord_centreline' is the x coordinate
# of the building's midpoint or centreline.  The 'building_style' is the
# unique building style; each style should differ in terms of shape, colour and
# 'additional elements' (doors, windows, balconys, advertising signs, etc).


# Skyline No. 1: All buildings the same style; decreasing heights
# from left to right; no overlaps
skyline_1 = [[ 50, 490, -470, 'style_F'],
             [265, 440, -308, 'style_F'],
             [100, 390, -120, 'style_F'],
             [148, 340,    7, 'style_F'],
             [290, 290,  230, 'style_F'],
             [120, 240,  440, 'style_F']]

# Skyline No. 2: All six different building styles; decreasing heights
# from left to right; no overlaps
skyline_2 = [[ 50, 490, -470, 'style_A'],
             [265, 440, -308, 'style_B'],
             [100, 390, -120, 'style_C'],
             [148, 340,    7, 'style_D'],
             [290, 290,  230, 'style_E'],
             [120, 240,  440, 'style_F']]

# Skyline No. 3: Different building styles and sizes; symmetrically
# arranged with the highest in the middle; buildings touching
skyline_3 = [[ 50, 190, -455, 'style_A'],
             [260, 290, -300, 'style_B'],
             [100, 390, -120, 'style_C'],
             [140, 490,    0, 'style_E'],
             [100, 390,  120, 'style_C'],
             [260, 290,  300, 'style_B'],
             [50, 190,   455, 'style_A']]
               
# Skyline No. 4: Different styles; three 'layers' overlapped;
# increasing heights from left to right in each layer;
# decreasing heights from the furthest to the closest layer
skyline_4 = [[ 50, 400, -404, 'style_A'],
             [100, 430,  -60, 'style_A'],
             [160, 460,  300, 'style_B'],
             [ 40, 490,  460, 'style_B'],
             [170, 360,  400, 'style_C'],
             [250, 320,   85, 'style_C'],
             [160, 280, -200, 'style_D'],
             [170, 240, -420, 'style_D'],
             [164, 130, -380, 'style_E'],
             [300, 170,  -50, 'style_E'],
             [200, 210,  265, 'style_F'],
             [100, 250,  440, 'style_F']]

# Skyline No. 5: A more 'natural' looking Central Business
# District   
skyline_5 = [[ 45, 480, -160, 'style_D'],
             [150, 380, -200, 'style_A'],
             [100, 495,  -60, 'style_B'],
             [160, 450,  100, 'style_E'],
             [40,   490, 460, 'style_A'],
             [170, 390,  400, 'style_D'],
             [150, 360,   20, 'style_F'],
             [160, 280, -160, 'style_C'],
             [170, 440, -420, 'style_F'],
             [200, 300, -340, 'style_B'],
             [170, 100, -270, 'style_E'],
             [300, 170,  -50, 'style_D'],
             [200, 210,  265, 'style_C'],
             [100, 320,  440, 'style_F'],
             [130, 200, -420, 'style_A']]

# Skyline No. 6: Another 'realistic' CBD
skyline_6 = [[ 45, 460,  180, 'style_D'],
             [100, 495,  260, 'style_E'],
             [150, 380,  140, 'style_A'],
             [140, 430,  350, 'style_F'],
             [ 40, 490,  460, 'style_A'],
             [170, 350,  400, 'style_D'],
             [250, 240,  -10, 'style_F'],
             [160, 200, -160, 'style_B'],
             [170, 450, -420, 'style_F'],
             [200, 300, -340, 'style_D'],
             [170, 100, -270, 'style_F'],
             [300, 150,  -20, 'style_E'],
             [200, 210,  265, 'style_B'],
             [100, 300,  440, 'style_C'],
             [150, 200, -420, 'style_C']]

#***** If you want to create your own test data put it here

# Skyline 7: Compairing a single building in two extreme proportions 
skyline_7 = [[ 50, 490, -470, 'style_F'],
             [290, 290,  230, 'style_F']]

# Skyline 8: Debugging style F sizing error in certain skyline
skyline_8 = [[170, 100, -270, 'style_F'],
             [250, 240,  -10, 'style_F'],
             [140, 430,  350, 'style_F']]
#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the task by replacing the dummy function below with
#  your code

def draw_buildings(skyline):

    #-DEFINE FEATURE FUNCTIONS--------------------------------------------------------------------#
    def base(width, height, center, y = 0):        #Draws basic shape of all buildings, builds from BOTTOM LEFT
        goto((center - (width/2)), y)
        begin_fill()
        setheading(90)      #start left wall
        pendown()
        forward(height)

        setheading(0)       #roof
        forward(width)

        setheading(-90)     #right wall
        forward(height)
        
        setheading(180)     #floor
        forward(width)
        end_fill()
        penup()

    def windows(style, width, height, gwidth, gheight, wvert, whorz, crnxdefault, crny = -1):   #draws window grids. wvert = windows vertical, whroz = windows horizontal
        crnx = crnxdefault  #sets the bottom left starting x coordinate 
        if crny == -1:       #setting bottom left window height from ground
            crny = gheight
        
        if style == "A":    #window Colour
            color("Grey")
        elif style == "B":
            color("Black")
        elif style == "D":
            color("black")  
        elif style == "F":
            color("white")  

        for y in range(wvert):  #draw windows up building
            goto(crnx, crny)
            for x in range(whorz): #draw windows accross building
                goto(crnx, crny)
                setheading(90)
                pendown()
                begin_fill()
                forward(height)     #left side
                setheading(0)
                forward(width)      #top
                setheading(-90)
                forward(height)     #right
                setheading(180)
                forward(width)      #bottom
                end_fill()
                penup()
                
                crnx += width+(gwidth)  #Move to the next window accross 
                
            crnx = crnxdefault #reset window start x
            crny += height + gheight #Move to the next window up
        penup()

        if style == "A":    #window panels
            interval = height/16    #sets the distance between panel lines based on height for rescaling 
            color("black")
            for x in range(whorz):  #draw panels accross building
                for i in range(1,16): #draw windows up building 
                    goto(crnx, gheight + interval*i)   #goes to the location of the panel, y coordinate changes based on for loop
                    setheading(0)
                    pendown()
                    forward(width+1)        #+1 added to avoid the gap at the edge of the window
                    penup()
                    
                crnx += width+(gwidth) 
        penup()

        
    def windowsC(width, height, gwidth, gheight, wvert, whorz, crnxdefault, crny = 0):   #draws windows for Style C: Gothic style windows
        crnx = crnxdefault
        if crny == 0:       #setting bottom left window height from ground
            crny = gheight

        color("white")
        for y in range(wvert):  #draw windows up building
            goto(crnx, crny)
            for x in range(whorz): #draw windows accross building
                goto(crnx, crny)        #setup
                pendown()
                begin_fill()

                setheading(90)          #window cill
                forward(height*0.05)    
                setheading(0)
                forward(width)
                setheading(-90)
                forward(height*0.05)
                setheading(180)
                forward(width)
                end_fill()
                penup()

                arch((crnx + width*0.1), (crny + height*0.05), height*0.95, width*0.8, "white")  #draws window arch frame
                arch((crnx + width*0.2), (crny + height*0.05), height*0.8, width*0.6, "black")  #draws the window area 
                color("white")
              
                crnx += width+(gwidth) #Move to the next window accross 
                
            crnx = crnxdefault #reset window start x
            crny += height + gheight #Move to the next window up 

        penup()
      
    def windowsE(width, height, crnxdefault, crnydefault = 0):   #draws windows for Style E: Close together with different colours, draws from BOTTOM LEFT
        #constants
        crnx = crnxdefault
        crny = crnydefault
        whorz = 5
        wvert = 12
        wwidth=(width-2)/whorz
        wheight=(height-2)/wvert

        yellow_windows = [[1,2],[2,2],[3,2],        #defines which windows are a different colour, set so that the first colomn and row are postion 0
                          [3,3],[3,4],
                          [1,5],[2,5],[3,5],
                          [1,6],[1,7],[1,8],
                          [1,9],[2,9],[3,9]]
        
        color("Black")
        base(width, height, center, crny)
        crnx += 1       #adding 1 to both coordinates creates a 1px border around the windows 
        crny += 1
        goto(crnx, crny)
        for y in range(wvert):  #draw windows up building
            goto(crnx, crny)
            for x in range(whorz): #draw windows accross building
                if [x,y] in yellow_windows:
                    color("Yellow")
                else:
                    color("Dark Grey")
                goto(crnx, crny)
                setheading(90)
                pendown()
                begin_fill()
                forward(wheight)    #left   
                setheading(0)
                forward(wwidth)     #top
                setheading(-90)
                forward(wheight)    #right
                setheading(180)
                forward(wwidth)     #bottom
                end_fill()
                penup()
                
                crnx += wwidth      #Move to the next window accross 
                
            crnx = crnxdefault + 1 #reset window start x
            crny += wheight #Move to the next window up
        penup()

        crnx = crnxdefault  #resets to starting position
        cnry = crnydefault
        color("black")
        
        #Draws seperator lines between windows 
        for x in range(whorz): #draw lines vertically
            goto(crnx, crny)                
            setheading(-90)
            pendown()
            forward(height)
            penup()   
            crnx += wwidth 
            
        crnx = crnxdefault #resets to starting position
        cnry = crnydefault
        for y in range(wvert):  #draw lines horiztonally 
            goto(crnx, crny)                
            setheading(0)
            pendown()
            forward(width)
            penup()
            crny += -wheight

    def arch (startx, starty, structure_height, base, colour):   #Draws dome tops
        radius = (base/2)
        side = structure_height - radius #This is done to keep the arch top within the given paramiters
            
        goto(startx, starty) #draws main dome
        setheading(90)
        pendown()
        color(colour)
        begin_fill()
        forward(side)
        circle(-radius, 180)
        setheading(-90)
        forward(side)
        end_fill()
        penup()


    def doorC (width, height, center):      #draws door for building C: Stone Arch Door
        color("black")          #set colours

        base(width, height*0.05, center)         #setup steps
        arch(center - width/2, height*0.05, height*0.95, width, "grey")     #door trim
        color("black")          #set colours
        base(width*0.8, height*0.05, center, height*0.05)
        arch(center - ((width*0.8)/2), height*0.1, height*0.8, width*0.80, "brown")  #door
        penup()
        goto(center, height*0.9)            #gap between the doors
        setheading(-90)
        pendown()
        color("black") 
        forward(height*0.8)
        penup()
        goto(center - (width*0.1), height*0.5)         #door nobs
        dot(width*0.08)
        goto(center + (width*0.1), height*0.5)
        dot(width*0.08)
        
    def featuresD(width, height, center):       #adds the features of the building (balcony, LED sign, etc)                             
        interval = width*0.2
        fheight = height*0.08

        def glass(x,y):                     #draws the glass slits on the side of the building
            featyn = 1 
            color("white")
            goto(x,y)
            for i in range(1, 26):
                if featyn == 1:
                    setheading(90)
                    pendown()
                    forward(fheight)
                    penup()
                    featyn = 0
                else:
                    featyn = 1
                if i % 5 == 0:
                    y += fheight
                    x = center - width*0.4
                else:
                    x += interval 
                goto(x,y)

        def balcony(x,y):
            #variables
            interval = width*0.05
            support = height*0.05 + 1
            
            goto(x, y)
            setheading(0)
            color("#827E7F")    #Railing grey
            pendown()
            forward(width)
            penup()
            
            for i in range(0,21): #draws balcony supports 
                    goto(x, y)  
                    setheading(-90)
                    pendown()
                    forward(support)        
                    penup()
                    x += interval
                    
        def draw1 (x,y, width, height): #draws the 1 on the sign, builds from TOP LEFT
            goto(x,y)
            color("gold")
            pendown()
            begin_fill()
            setheading(0)
            forward(width*0.6)
            setheading(-90)
            forward(height*0.8)
            setheading(0)
            forward(width*0.4)
            setheading(-90)
            forward(height*0.2)
            setheading(180)
            forward(width)
            setheading(90)
            forward(height*0.2)
            setheading(0)
            forward(width*0.4)
            setheading(90)
            forward(height*0.6)
            setheading(180)
            forward(width*0.4)
            setheading(90)
            forward(height*0.2)
            end_fill()
            penup()

        def draw0 (x,y, width, height): #draws the 0 on the sign, builds from TOP LEFT
            goto(x,y)
            color("gold")
            begin_fill()
            pendown()
            setheading(0)
            forward(width)
            setheading(-90)
            forward(height)
            setheading(180)
            forward(width)
            setheading(90)
            forward(height)
            end_fill()
            penup()
            color("black")
            goto(x+width*0.2,y-height*0.2)
            begin_fill()
            pendown()
            setheading(0)
            forward(width*0.6)
            setheading(-90)
            forward(height*0.6)
            setheading(180)
            forward(width*0.6)
            setheading(90)
            forward(height*0.6)
            end_fill()
            penup()

        def draw4 (x,y, width, height): #draws the 4 on the sign, builds from TOP LEFT
            goto(x,y)
            color("gold")
            begin_fill()
            pendown()
            setheading(0)
            forward(width*0.2)
            setheading(-90)
            forward(height*0.4)
            setheading(0)
            forward(width*0.6)
            setheading(90)
            forward(height*0.4)
            setheading(0)
            forward(width*0.2)
            setheading(-90)
            forward(height)
            setheading(180)
            forward(width*0.2)
            setheading(90)
            forward(height*0.4)
            setheading(180)
            forward(width*0.8)
            setheading(90)
            forward(height*0.4)
            end_fill()
            penup()
            
            
        def sign (center, y,sign_width, sign_height):         #Draws the sign, builds from BOTTOM LEFT
            letter_width = (sign_width*0.7)/3
            color("black")
            base(sign_width, sign_height, center, y)
            draw1(center-(sign_width*0.45),y+sign_height*0.9,letter_width, sign_height*0.8)                  #draw numbers
            draw0((center-(sign_width*0.45)+letter_width+(sign_width*0.1)),y+sign_height*0.9,letter_width, sign_height*0.8)
            draw4((center-(sign_width*0.45)+letter_width*2+(sign_width*0.2)),y+sign_height*0.9,letter_width, sign_height*0.8)
            
            
        glass(center - width*0.4,0)
        color("#E0DCDC") #Light grey
        base(width, height*0.1, center, y = fheight*5)
        windows("D", width*0.20, height*0.08, width*0.175, 0, 1, 3, center - width*0.475,fheight*5 + height*0.01)
        balcony(center - width/2, height*0.45)
        glass(center - width*0.4, fheight*5 + height*0.1)
        sign(center, height*0.91, width*0.9, height*0.08)

    def draw6 (crnx, crny, height, width):  #draws the number 6 on the building. Used for style F. Draws from BOTTOM LEFT
        goto(crnx, crny)    #Goes to the Bottom left corner to start
        color("yellow")
        pendown()
        begin_fill()
        #left side
        setheading(90)
        forward(height)
        #top
        setheading(0)
        forward(width)
        #top "stem"
        setheading(-90)
        forward(height*0.2)
        setheading(180)
        forward(width*0.8)
        #down to bottom circle
        setheading(-90)
        forward(height*0.2)
        #bottom circle (frame)
        setheading(0)
        forward(width*0.8)
        setheading(-90)
        forward(height*0.6)
        setheading(180)
        forward(width)
        end_fill()
        penup()
        
        #bottom circle (gap)
        color("#E35DCF")    #purple
        base((width*0.6),(height*0.2), crnx + (width*0.5), crny + (height*0.2)) #Draws the gap using the base function, as both are polygons 
        
        
    #-DEFINE ROOF FUNCTIONS--------------------------------------------------------------------#
    def roofA (width, roof_base, spire_height, center):  #draws roof type A: Radio Antennas

        def spire (spire_height, width, start_height, center):    #Draws Spire
            goto(center - (width/2), start_height)      #Stars bottom left
            pendown()
            begin_fill()
            goto(center, spire_height + start_height)         #goes to the tip
            goto(center + (width/2), start_height)      #goes to bottom right
            end_fill()
            penup()

        color("black")      #Set colour
        spire (spire_height, (width*0.3), roof_base, center)  #Center spire
        spire (spire_height*0.75, (width*0.2), roof_base, center - (width*0.4))  #left spire
        spire (spire_height*0.75, (width*0.2), roof_base, center + (width*0.4))  #right spire
        
        for i in [-1,1]:    #Draws wires from center spire to both the roof and left/right spires. List is used for the for loop to draw both the left and right sides
            goto(center, roof_base+spire_height)
            pendown()
            goto(center + (width*0.225)*i, roof_base)      #Center spire to left/right roof
            penup()
            goto(center, roof_base+spire_height)
            pendown()
            goto(center + (width*0.4)*i, roof_base+(spire_height*0.75))      #Center spire to left/right spire
            penup()
            
        goto(center, roof_base+spire_height)                   #center light
        color("red")
        pendown()
        dot(width*0.05)
        penup()

    def roofB (width, roof_base, height, center):  #draws roof type B: Empire state inspired staggering 
        angles = [0, 90, 0, 90, 0, -90, 0 , -90, 0]  #roof section angles
        distances = [(width*0.15), (height*0.05), (width*0.15), (height*0.05), (width*0.4), (height*0.05),(width*0.15) ,(height*0.05), (width*0.15)] #roof section distances

        goto((center - (width/2)), roof_base)       #go to starting point
        pendown()
        begin_fill()
        for i in range(len(angles)):
            setheading(angles[i])
            forward(distances[i])
        end_fill()
        penup()

    def roofC (width, roof_base, height, center): #draws roof type C: "Gothic" triangle roof overhang
        goto(center - ((width*0.8)/2), roof_base)
        color("#B87F85")    #Roof Grey/Red
        setheading(180)
        begin_fill()
        forward(width*0.1)
        goto(center - ((width*0.8)/2), height)
        setheading(0)
        forward(width*0.8)
        goto(center + ((width)/2), roof_base)
        setheading(180)
        forward(width*0.1)
        end_fill()

    def roofE (width, roof_base, height, center): #draws roof type E: Triangle with Vinyl Record inside
        if ((height*0.7)) > (width/2):        #Sets the vinyl's diameter
            diameter = width/2
        else:
            diameter = (height*0.7)

        goto(center - (width/2), roof_base)     #Draws triangle
        color("#16B83C") #green
        begin_fill()
        pendown()
        goto(center, height+roof_base)
        goto(center + ((width)/2), roof_base)
        goto(center - (width/2), roof_base)
        end_fill()
        penup()

        goto(center, roof_base+height*0.35)
        dot(diameter, "black")          #Draws the vinyl's base
        dot(diameter*0.28, "gold")      #Draws the vinyl's center
        dot(diameter*0.05, "black")     #Draws the vinyl's center hole

    #-DEFINE BUILDING FUNCTIONS--------------------------------------------------------------------#
    def draw_styleA(width, height, center):
        color("black")
        wwidth = width*0.2                          #window width
        wheight = height*0.70                       #window height
        gwidth = width*0.2                          #gap between windows horizontally
        gheight = height*0.075                      #gap between windows vertically
        
        base(width, height*0.85, center)                #draw base
        roofA(width, height*0.85, height*0.15, center)  #draw roof       
        windows("A", wwidth, wheight, gwidth, gheight, 1, 2, (center - (width/2)) + (width*0.2)) #draw windows
    
    def draw_styleB(width, height, center):
        #constants
        color("#878686") #Dark Grey
        wwidth = width*0.09                         #window width 
        wheight = height*0.05                       #window height
        gwidth = width*0.0657                       #gap between windows horizontally
        gheight = height*0.025                     #gap between windows vertically
        
        base(width, (height*0.9), center)           #draw base
        roofB(width, height*0.9, height, center)    #draw roof 
        windows("B", wwidth, wheight, gwidth, gheight, 12, 6, (center - (width/2)) + gwidth, height*0.01 ) #draw windows

    def draw_styleC(width, height, center):
        #constants
        color("#CF1D32")       #Dark red
        wwidth = width*0.2                          #window width
        wheight = height*0.1                        #window height
        gwidth = width*0.2                          #gap between windows horizontally
        gheight = height*0.06                       #gap between windows vertically

        base((width*0.8), (height*0.9), center)         #draws base
        roofC(width, (height*0.9), height, center)      #draws window
        windowsC(wwidth, wheight, gwidth, gheight, 5, 2, (center - (width*0.3)), height*0.1) #draw windows
        doorC(gwidth, height*0.09, center)

    def draw_styleD(width, height, center):
        color("Dark Blue")
        base(width, height, center)                     #draw base and roof
        featuresD(width, height, center)                #draws building features
        
    def draw_styleE(width, height, center):
        color("#16B83C")        #green
        body_height = height*0.9                #The building height without the triangle roof

        base(width, body_height, center)                                                     #Draws base
        windowsE(width*0.9, body_height*0.9, center - (width*0.45),body_height*0.05)    #Draws windows
        roofE(width, body_height, height - body_height, center)                         #Draws roof

    def draw_styleF(width, height, center):
        #constants
        color("#E35DCF")    #purple
        wwidth = width*0.78                    #window width
        wheight = height*0.15                  #window height
        gheight = height*0.04                  #gap between windows vertically

        base(width*0.2, height, center - width*0.4)     #builds the taller side of the building. Center adjusted so the building is drawn in the right position
        base(width*0.8, height*0.8, center + width*0.1) #builds the main structure of the building. Center adjusted so the building is drawn in the right position
        windows("F", width*0.1, height*0.76, 0, 0, 1, 1, center - width*0.45, 0) #Draws the window on the taller side
        windows("F", wwidth, wheight, 0, gheight, 4, 1, center - width*0.3) #Draws windows on the main body of the building
        draw6(center - width*0.45, height*0.85, height*0.1, width*0.1)  #Draws the 6 on the building
        
    #DRAW SKYLINE--------------------------------------------------------------------------------------------#
    for building in skyline:    #get buildings
        width = building[0]     #get building specs
        height = building[1]
        center = building[2]
        style = building[3]
        style = style[-1]       #simplify type selection

        if style == "A":
            draw_styleA(width,height,center)
        elif style == "B":
            draw_styleB(width,height,center)
        elif style == "C":
            draw_styleC(width,height,center)
        elif style == "D":
            draw_styleD(width,height,center)
        elif style == "E":
            draw_styleE(width,height,center)
        elif style == "F":      #currently test
            draw_styleF(width,height,center)

        
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the drawing environment, ready for you
# to start drawing your buildings.  You may not change any of
# this code except the lines marked '*****'
    
# Set up the drawing window with coordinate (0, 0) at the
# centre of the "grass"
setup(window_width, window_height)
setworldcoordinates(-half_width, -grass_depth, half_width, max_height)
title('Skylines')

# Draw as quickly as possible by minimising animation
hideturtle()     #***** You may comment out this line while debugging
                 #***** your code, so that you can see the turtle
speed('fastest') #***** You may want to change the drawing speed
                 #***** while debugging your code

# Decide whether or not to draw the grid numbers
grid_on = True   #***** Make this False to avoid drawing the
                 #***** coordinates to produce a prettier picture

# Colour the sky                    
bgcolor('sky blue')

# Draw the grass
penup()
fillcolor('lawn green')
goto(-half_width, 0)
begin_fill()
forward(window_width)
right(90)
forward(grass_depth)
right(90)
forward(window_width)
end_fill()

# Draw x coordinates along the bottom of the screen (to aid
# debugging and marking)
if grid_on:
    for x_coord in range(-half_width + grid_size, half_width, grid_size):
        goto(x_coord, -grass_depth + offset)
        write('| ' + str(x_coord), font=('Arial', font_size, 'normal'))

# Draw y coordinates on the left-hand edge of the screen (to aid
# debugging and marking)
if grid_on:
    for y_coord in range(-grid_size, max_height, grid_size):
        goto(-half_width + offset, y_coord - offset)
        write(y_coord, font=('Arial', font_size, 'normal'))       

# Call the function to draw a skyline (using one of the lists
# skyline_1 to skyline_6)
draw_buildings(skyline_6) #***** Change the argument for different tests
    
# Exit gracefully
hideturtle()
done()

#
#--------------------------------------------------------------------#




