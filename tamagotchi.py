class container:
    divisions = (1,1,1) #(rows,cols,lineWeight)
    frame = (0,0,10,10,0) #(x1,y1,x2,y2,r) - rounded box
    headers = (0,0,0,0,1) #(left,right,top,bottom,lineWeight) - size
    cellDims = (10,10) #(w,h)
    headerDims = ((0,10),(0,10),(10,0),(10,0)) #(l,r,t,b).*(w,h)
    display
    def __init__(self,disp,frame,divs,heads):
        self.display = disp
        self.frame = frame
        self.divisions = divs
        self.headers = heads
        
        self.cellDims = ((frame[0]-frame[
    
    def refreshDims(self):
        frameWidth = abs(self.frame[0]-self.frame[2])
        headerWidth = abs(headers[0]+headers[1])
        frameHeight = abs(self.frame[1]-self.frame[3])
        headerHeight = abs(headers[2]+headers[3])
        
        self.cellDims = (frameWidth-headerWidth