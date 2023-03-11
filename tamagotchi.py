import math as m
from picographics import PicoGraphics, DISPLAY_INKY_PACK
import network


display = PicoGraphics(display=DISPLAY_INKY_PACK)

def arc(display,x,y,r,t1,t2):
    #interval = 2*np.pi*r
    r=r-0.5
    for i in range(t1*10,t2*10,1):
         
        xi = int(r*m.cos(i*2*3.14/360.0/10)+x)
        yi = int(-1*r*m.sin(i*2*3.14/360.0/10)+y)
        
        display.pixel(xi,yi)
    return

def rectRound(display,x1,y1,x2,y2,r,d=1):
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
        arc(display,x1+r,y1+r,r,90,180)
        arc(display,x2-r,y1+r,r,0,90)
        arc(display,x1+r,y2-r,r,180,270)
        arc(display,x2-r,y2-r,r,270,360)
        x1 = x1+1
        x2 = x2-1
        y1 = y1+1
        y2 = y2-1
        r = r-1
    return

def scanNetworks(num):
    wlan = network.WLAN()
    wlan.active(True)
    
    output = [ssid[0] for ssid in wlan.scan()]
    
    return output[0:num]

class container:
    '''
    divisions = (1,1,1) #(rows,cols,lineWeight)
    frame = (0,0,10,10,0,1) #(x1,y1,x2,y2,r,lineWeight) - rounded box
    headers = (0,0,0,0,1) #(left,right,top,bottom,lineWeight) - size
    cellDims = (10,10) #(w,h)
    headerDims = ((0,10),(0,10),(10,0),(10,0)) #(l,r,t,b).*(w,h)
    '''
    def __init__(self,frame=(0,0,10,10,0,1),divs=(1,1,1),heads=(0,0,0,0,1)):
        self.frame = frame
        self.divisions = divs
        self.headers = heads
        
        self.refreshDims()
    
    def refreshDims(self):
        frameWidth = abs(self.frame[0]-self.frame[2])
        headerWidth = abs(self.headers[0]+self.headers[1])
        frameHeight = abs(self.frame[1]-self.frame[3])
        headerHeight = abs(self.headers[2]+self.headers[3])
        
        self.cellDims = (int((frameWidth-headerWidth)/self.divisions[1]),int((frameHeight-headerHeight)/self.divisions[0]))
        self.headerDims = ((self.headers[0]-self.headers[4],frameHeight-headerHeight),(self.headers[1]-self.headers[4],frameHeight-headerHeight),(self.headers[2]-self.headers[4],frameWidth-headerWidth),(self.headers[3]-self.headers[4],frameWidth-headerWidth))
    
    def getCellLocation(self,coords):
        self.refreshDims()
        return ((self.headers[0]+coords[0]*self.cellDims[0]+self.frame[0]),(self.headers[2]+coords[1]*self.cellDims[1]+self.frame[1]))
    
    def draw(self,display):
        #frame first
        rectRound(display,*self.frame)
        #headers 
        #left
        if not(self.headers[0]==0):
            for i in range(self.headers[4]):
                x1 = self.frame[0]+self.headers[0]-i
                y1 = self.frame[1]
                x2 = x1
                y2 = self.frame[3]
                display.line(x1,y1,x2,y2)
        #right
        if not(self.headers[1]==0):
            for i in range(self.headers[4]):    
                x1 = self.frame[2]-self.headers[1]+i
                y1 = self.frame[1]
                x2 = x1
                y2 = self.frame[3]
                display.line(x1,y1,x2,y2)
        #top
        if not(self.headers[2]==0):
            for i in range(self.headers[4]):
                x1 = self.frame[0]
                y1 = self.frame[1]+self.headers[2]-i
                x2 = self.frame[2]
                y2 = y1
                display.line(x1,y1,x2,y2)
        #bottom
        if not(self.headers[3]==0):
            for i in range(self.headers[4]):
                x1 = self.frame[0]
                y1 = self.frame[3]-self.headers[3]+i
                x2 = self.frame[2]
                y2 = y1
                display.line(x1,y1,x2,y2)
        
        #divisions
        #rows
        for i in range(self.divisions[0]-1):
            x1 = self.frame[0]+self.headers[0]
            y1 = self.frame[1]+self.headers[2]+(i+1)*self.cellDims[1]
            x2 = self.frame[2]-self.headers[1]
            y2 = y1
            display.line(x1,y1,x2,y2)
        #cols
        for i in range(self.divisions[1]-1):
            x1 = self.frame[0]+self.headers[0]+(i+1)*self.cellDims[0]
            y1 = self.frame[1]+self.headers[2]
            x2 = x1
            y2 = self.frame[3]-self.headers[3]
            display.line(x1,y1,x2,y2)
    
    def writeCell(self,display,coords,value):
        (x,y) = self.getCellLocation(coords)
        value = str(value)      
        display.set_pen(15)
        display.rectangle(x+self.frame[4]-1,y+self.frame[4]-3,self.cellDims[0]-2*self.frame[4]+4-self.frame[4],self.cellDims[1]-2)
        display.set_font("bitmap8")
        display.set_pen(0)
        
        x += 2 + self.frame[5]
        y = int(y + self.frame[5] + (self.cellDims[1]-8)/2) - 1
        shortened = False
        
        
        while display.measure_text(value,1) > self.cellDims[0] - 6:
            value = value[:-1]
            shortened = True
        
        if shortened:
            value = value[:-3] + "..."
            
        display.text(value,x,y,self.cellDims[0]-6,1)
        
    def writeColumn(self,display,column,values):
        for i in range(self.divisions[0]):
            self.writeCell(display,(column,i),values[i])
            
    def writeHeader(self,display,side,value):
        if side == 1:
            x = self.frame[0] + self.frame[5] + self.headers[0] + self.headers[4] + 2
            y = int(self.frame[1] + self.frame[5] + (self.headers[2]-8)/2)
            width = self.frame[2] - self.frame[0] - self.headers[0] - self.headers[1]
            display.set_pen(15)
            display.rectangle(x-1,y-1,width-(4+self.frame[4]),10)
            display.set_font("bitmap8")
            display.set_pen(0)
        display.text(value,x,y,width,1)
        
class scrollingList:
    
    def __init__(self,contents=[],window = 0):
        self.contents = contents
        self.window = window + 1
        self.index = 0
        
        while window > len(contents):
            self.contents.append('')
        if window >= 1:
            self.viewable = contents[0:window]
        else:
            self.viewable = []
            
    def updateContents(self,contents):
        self.contents = contents
        while self.window > len(contents)+1:
            self.contents.append(0)
        if self.window >= 1:
            self.viewable = contents[0:self.window]
        else:
            self.viewable = []
    def scroll(self,interval):
        self.index += interval
        
        if self.index > len(self.contents)-1:
            self.index -= len(self.contents)
        elif self.index < 0:
            self.index += len(self.contents)
        self.viewable = []
        
        for i in range(self.window):
            if self.index + i < len(self.contents):
                self.viewable.append(self.contents[self.index + i])
            else:
                self.viewable.append(self.contents[self.index + i - len(self.contents)])
                
                
