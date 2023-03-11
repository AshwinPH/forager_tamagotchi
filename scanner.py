import network

wlan = network.WLAN()
wlan.active(True)

def getNetworks(num):
    allNetworks = wlan.scan()
    SSIDs = list((str(x[0]).strip('b\'') for x in list(allNetworks) if (str(x[0]).strip('b\'') != '')))
    
    if len(SSIDs)-1 < num:
        num = len(SSIDs)-1
        
    return SSIDs[0:num]