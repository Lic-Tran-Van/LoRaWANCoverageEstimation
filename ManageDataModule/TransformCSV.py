"""[SNR,
            RSSI,
            longitude,
            Altitude,
            Gateway_Long,
            Gateway_Lat,
            Gateway_Alt,
            Gateway_Id]
"""
import csv

def NewCSVtoListData(id):
    #15 : gatewayID
    #24:RSSI
    #26 :SNR
    #GatewayLat =26
    #GatewayLong=27
    #GatewayAlt=28
    #31: Lat
    #32 :long
    #33 :Alt
    rows=[]
    file3 = open('ManageDataModule/DonnéesV3.CSV')
    file4 = open('ManageDataModule/DonnéesV4.CSV')
    file5 = open('ManageDataModule/DonnéesV5.CSV')
    file6 = open('ManageDataModule/DonnéesV6.CSV')

    def rowsAppendRow(rows,file):
        type(file)
        csvreader = csv.reader(file)
        rowTemp=[]
        vu=False
        for row in csvreader:
            if vu==True:
                vu=False
                row+=a
            elif (len(row)<33):
                a=row
                vu=True
            else:
                rowTemp.append(row)
        rowTemp.pop(0)
        rowTemp.pop(0)
        rowTemp.pop()
        rowTemp.pop()
        for row in rowTemp :
            rows.append(row)
        return rows
    #rows= rowsAppendRow(rows,file)
    rows = rowsAppendRow(rows, file3)
    rows = rowsAppendRow(rows, file4)
    rows= rowsAppendRow(rows,file5)
    rows=rowsAppendRow(rows,file6)
    SNR = []
    RSSI = []
    Gateway_Lat = []
    Gateway_Long = []
    Gateway_Alt = []
    Altitude = []
    latitude = []
    longitude = []
    Gateway_Id = []
    rows.pop(0)
    for row in rows:
        if row[14]==id :
            Gateway_Id.append(row[14])
            Gateway_Lat.append(row[26])
            Gateway_Long.append(row[27])
            Gateway_Alt.append(row[28])
            SNR.append(row[25])
            RSSI.append(row[23])
            Altitude.append(row[33])
            latitude.append(row[31])
            longitude.append(row[32])
    tab=[SNR,RSSI,longitude,latitude,Altitude,Gateway_Long,Gateway_Lat,Gateway_Alt,Gateway_Id]
    tab=clearTab(tab)
    return (tab)

def addTab(tab1,tab2):
    tab1=clearTab(tab1)
    tab2=clearTab(tab2)
    for i in range(len(tab1)):
        for j in range(len(tab1[i])):
            tab2[i].append(tab1[i][j])
    return tab2

def clearTab(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])-1):
            if (tab[i][j]=='null'):
                print('none')
                for l in range(len(tab)):
                    tab[l].pop(j)
    return tab
