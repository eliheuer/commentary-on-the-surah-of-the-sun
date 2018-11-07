# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os


# STATIC VARIABLE
W,H,M,F = 792,612,64,1         # WIDTH, HEIGHT, MARGIN, FRAMES
VAR_WGHT = 100                 # VARIABLE FONT WEIGHT
LINE_H = H/20                  # LINE HEIGHT
START_POS = 400


# SET FONT
font("fonts/Inter-UI-VF.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))

# GRID DRAWING FUNCTION
def grid(inc):
    stroke(0.8)
    stpX, stpY = 0, 0
    incX = (W-(M*2))/inc
    incY = (W-(M*2))/inc
    print("incX=", incX)
    for x in range(inc+1):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(inc+1):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY

# DRAW NEW PAGE
newPage(W, H)
fill(1)
rect(0, 0, W, H)
grid(20)

#Guides
stroke(1,0,0)
polygon((W/2, 0),(W/2, H))

# HEADLINE
fill(0)
tracking(0)
stroke(None)
fontSize(24)
fontVariations(wght=900)
text("Commentary on the  ",      (W/2+M, (START_POS)-(0*LINE_H)))
text("Surah of the Sun ",       (W/2+M, (START_POS)-(1*LINE_H)))

# Draw large type
fontSize(50)
for i in range(6):
    VAR_WGHT += 100
    fontVariations(wght=VAR_WGHT)
    print("VAR_WGHT=", VAR_WGHT) 
#    text("Variable Font", (M+10, (START_POS-M+3)-(i*40)))

# Dot
fill(1,0,0)
oval(M, M, (W-(M*2))/20, (W-(M*2))/20)

# Draw small type
fontVariations(wght=400)
fill(1)
fontSize(50)
tracking(-4)
text("A B C D E F G H I J ",      (M+440, (START_POS)-( 8*LINE_H/2)))

# Save PDF
saveImage("cover-design.pdf")
