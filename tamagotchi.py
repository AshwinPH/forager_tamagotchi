import math as m
from picographics import PicoGraphics, DISPLAY_INKY_PACK

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
