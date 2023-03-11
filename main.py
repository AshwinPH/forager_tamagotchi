from picographics import PicoGraphics, DISPLAY_INKY_PACK
from pimoroni import Button
import math as m
import time
import tamagotchi as tg
import scanner

display = PicoGraphics(display=DISPLAY_INKY_PACK)
display.set_update_speed(2)

button_a = Button(12)
button_b = Button(13)
button_c = Button(14)

display.set_pen(15)
display.clear()


#statBox
sBF=(0,96,168,128,5,2)
sBH=(16,16,0,0,2)
sBD=(2,2,1)
statBox = tg.container(sBF,sBD,sBH)
display.set_pen(0)
statBox.draw(display)

#nameBox
nBF=(188,0,296,24,5,2)
nBH=(0,0,0,0,1)
nBD=(1,1,1)
nameBox=tg.container(nBF,nBD,nBH)
nameBox.draw(display)

#resourceBox
rBF=(188,24,296,96,5,2)
rBD=(5,1,1)
rBH=(0,0,16,0,2)
resBox=tg.container(rBF,rBD,rBH)
resBox.draw(display)
contents = tg.scrollingList(scanner.getNetworks(15),resBox.divisions[0])
resBox.writeColumn(display,0,contents.viewable)
resTitle = f"Networks - ({contents.index}-\"{contents.index+contents.window}\")/{len(contents.contents)}"
resBox.writeHeader(display,1,resTitle)

#inventoryBox
iBF=(168,96,296,128,5,2)
iBD=(2,10,1)
iBH=(16,0,0,0,2)
invenBox=tg.container(iBF,iBD,iBH)
invenBox.draw(display)
'''
testFrame=(10,10,256,118,10,2)
testHeaders=(30,0,0,0,2)
testDivs=(6,4,1)
testBox=tg.container(testFrame,testDivs,testHeaders)
display.set_pen(0)
testBox.draw(display)
'''


display.update()

while True:
    if button_c.read():
        contents.scroll(1)
        resBox.writeColumn(display,0,contents.viewable)
        resTitle = f"Networks - ({contents.index}-\"{contents.index+contents.window}\")/{len(contents.contents)}"
        resBox.writeHeader(display,1,resTitle)
        display.update()
        time.sleep(1)
    elif button_a.read():
        contents.scroll(-1)
        resBox.writeColumn(display,0,contents.viewable)
        resTitle = f"Networks - ({contents.index}-\"{contents.index+contents.window}\")/{len(contents.contents)}"
        resBox.writeHeader(display,1,resTitle)
        display.update()
        time.sleep(1)
    elif button_b.read():
        contents.updateContents(scanner.getNetworks(15))
        resBox.writeColumn(display,0,contents.viewable)
        resTitle = f"Networks - ({contents.index}-\"{contents.index+contents.window}\")/{len(contents.contents)}"
        resBox.writeHeader(display,1,resTitle)
        display.update()
        time.sleep(1)
    time.sleep(0.1)
