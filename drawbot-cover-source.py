# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os


# STATIC VARIABLE
W,H,M,F = 792,612,18,1         # WIDTH, HEIGHT, MARGIN, FRAMES
VAR_WGHT = 100                 # VARIABLE FONT WEIGHT
LINE_H = H/20                  # LINE HEIGHT
START_POS = 495


# SET FONT
font("Helvetica Neue Bold")
for axis, data in listFontVariations().items():
    print((axis, data))

# GRID DRAWING FUNCTION
def grid(inc):
    stroke(0, 0, 1, 0.2)
    stpY = 0
    incY = 18
#    for x in range(inc+1):
#        polygon((M+stpX, M), (M+stpX, H-M))
#        stpX += incX
    for y in range(34):
        polygon((0, stpY), (W, stpY))
        stpY += incY

# DRAW NEW PAGE
newPage(W, H)
fill(0.8)
rect(0, 0, W, H)
grid(20)

#Guides
stroke(1,0,0,0.5)
strokeWidth(2)
polygon((W/2, 0),(W/2, H))
polygon((W/2-(M*2), 0),(W/2-(M*2), H))
polygon((W/2+(M*2), 0),(W/2+(M*2), H))
polygon((M*2, 0),(M*2, H))
polygon((W-M*2, 0),(W-M*2, H))

# HEADLINE
fill(0)
#tracking(-1.5)
stroke(None)
fontSize(34)
fontVariations(wght=900)
text("Commentary on the",         (W/2+(M*2), (29*M)))
text("Surah of the Sun",       (W/2+(M*2), (27*M)))

# Draw large type
fontSize(50)
for i in range(6):
    VAR_WGHT += 100
    fontVariations(wght=VAR_WGHT)
    print("VAR_WGHT=", VAR_WGHT) 
#    text("Variable Font", (M+10, (START_POS-M+3)-(i*40)))

# Dot
fill(1,0.5,0)
stroke(1,0.5,0)

# X,Y,W,H
oval( (W/2)+(M*2) , (LINE_H*4)+2-(M*2) , (W/2)-(M*4) , (W/2)-(M*4) )

# Draw small type
fontVariations(wght=400)
fill(1)
fontSize(50)
tracking(-4)

# Save PDF
saveImage("cover-design.png")
