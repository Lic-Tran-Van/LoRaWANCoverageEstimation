def getAllGatewayscoord():
    Gateway1Name = "7276ff002e0507da"
    Gateway1Lat = 16.11
    Gateway1Long = 108.273661
    Gateway1Alt = 812

    Gateway2Name = "trungnam"
    Gateway2Lat = 16.1089199
    Gateway2Long = 108.1275935
    Gateway2Alt = 2

    Gateway3Name = "7276ff002e06029f"
    Gateway3Lat = 16.07553058
    Gateway3Long = 108.2230598
    Gateway3Alt = 90

    Gateway4Name = "rfthings-rak7240-79ed"
    Gateway4Lat = 16.07484832106177
    Gateway4Long = 108.15411678280601
    Gateway4Alt = 10

    Gateway5Name = "danangdrt"
    Gateway5Lat = 16.0573461
    Gateway5Long = 108.2291504
    Gateway5Alt = 17

    Gateway1=[Gateway1Name,Gateway1Lat,Gateway1Long,Gateway1Alt]
    Gateway2=[Gateway2Name,Gateway2Lat,Gateway2Long,Gateway2Alt]
    Gateway3=[Gateway3Name,Gateway3Lat,Gateway3Long,Gateway3Alt]
    Gateway4=[Gateway4Name,Gateway4Lat,Gateway4Long,Gateway4Alt]
    Gateway5=[Gateway5Name,Gateway5Lat,Gateway5Long,Gateway5Alt]
    return ([Gateway1,Gateway2,Gateway3,Gateway4,Gateway5])

def getGateWayCoord(id):
    AllGatewaysCord=getAllGatewayscoord()
    Gateway_Lat = 0
    Gateway_Long = 0
    Gateway_Alt = 0
    for i in range(len(AllGatewaysCord)):
        if id==AllGatewaysCord[i][0]:
            Gateway_Lat=AllGatewaysCord[i][1]
            Gateway_Long=AllGatewaysCord[i][2]
            Gateway_Alt=AllGatewaysCord[i][3]
    return [Gateway_Lat, Gateway_Long, Gateway_Alt]

def getGatewaysNames():
    AllGatewaysCord=getAllGatewayscoord()
    Gatewaynames = []
    for i in range(len(AllGatewaysCord)):
        Gatewaynames.append(AllGatewaysCord[i][0])
    return Gatewaynames

def isIn(Gateway_id, tab):
    for i in range(len(tab)):
        if Gateway_id==tab[i]:
            return True
    return False