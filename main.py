from picographics import PicoGraphics, DISPLAY_INKY_PACK
from pimoroni import Button
import math as m
import time
import tamagotchi as tg

'''
def arc(x,y,r,t1,t2):
    #interval = 2*np.pi*r
    r=r-0.5
    for i in range(t1*10,t2*10,1):
         
        xi = int(r*m.cos(i*2*3.14/360.0/10)+x)
        yi = int(-1*r*m.sin(i*2*3.14/360.0/10)+y)
        
        display.pixel(xi,yi)
    return

def rectRound(x1,y1,x2,y2,r,d=1):
    if(abs(x1-x2)<2*r):
        r = int(abs(x1-x2)/2)
    elif(abs(y1-y2)<2*r):
        r = int(abs(y1-y2)/2)
    for i in range(d):
        
        #draw lines
        display.line(x1,y1+r,x1,y2-r)
        display.line(x2-1,y1+r,x2-1,y2-r)
        display.line(x1+r,y1,x2-r,y1)
        display.line(x1+r,y2-1,x2-r,y2-1)
        #draw arcs
        arc(x1+r,y1+r,r,90,180)
        arc(x2-r,y1+r,r,0,90)
        arc(x1+r,y2-r,r,180,270)
        arc(x2-r,y2-r,r,270,360)
        x1 = x1+1
        x2 = x2-1
        y1 = y1+1
        y2 = y2-1
        r = r-1
    return
'''
display = PicoGraphics(display=DISPLAY_INKY_PACK)
display.set_update_speed(2)

button_a = Button(12)
button_b = Button(13)
button_c = Button(14)

display.set_pen(15)
display.clear()


'''
display.set_pen(15)
display.clear()
display.set_pen(0)
#rectRound(0,0,296,128,10,2)
rectRound(0,96,168,128,10,2)
rectRound(188,0,296,24,10,2)
rectRound(188,24,296,24+68,10,2)
rectRound(168,92,296,128,10,2)
display.update()
'''
'''
sBF=(0,96,168,128,10,2)
sBH=(0,0,10,0,1)
sBD=(2,2,1)
statBox = tg.container(sBF,sBD,sBH)
display.set_pen(0)
statBox.draw(display)
'''
testFrame=(10,10,256,118,10,2)
testHeaders=(30,0,0,0,1)
testDivs=(6,4,1)
testBox=tg.container(testFrame,testDivs,testHeaders)
display.set_pen(0)
testBox.draw(display)



display.update()

