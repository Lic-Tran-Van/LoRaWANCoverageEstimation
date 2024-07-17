import csv #Base donnée
from random import random

import GatewaysModule
import ManageDataModule.TransformCSV
from GatewaysModule import Gateways
from ManageDataModule import ManageDataUtile

#Return the following tab:  [SNR,  RSSI,longitude,latitude,Altitude,Gateway_Lat,Gateway_Long,Gateway_Alt, Gateway_Id]
def get_list_data_per_Gateway(id):
    rows=[]
    file = open('ManageDataModule/Données.CSV')
    file2=open('ManageDataModule/DonnéesV2.CSV')
    file3=open('ManageDataModule/DonnéesV3.CSV')
    file4=open('ManageDataModule/DonnéesV4.CSV')
    file5=open('ManageDataModule/DonnéesV5.CSV')
    file6=open('ManageDataModule/DonnéesV6.CSV')
    def rowsAppendRow(rows,file):
        type(file)
        csvreader = csv.reader(file)
        rowTemp=[]
        for row in csvreader:
            rowTemp.append(row)
        rowTemp.pop(0)
        rowTemp.pop(0)
        rowTemp.pop()
        rowTemp.pop()
        for row in rowTemp :
            rows.append(row)
        return rows
    #rows= rowsAppendRow(rows,file)
    rows = rowsAppendRow(rows, file2)
    rows = rowsAppendRow(rows, file3)
    rows = rowsAppendRow(rows, file4)
    rows= rowsAppendRow(rows,file5)
    rows=rowsAppendRow(rows,file6)
    rows.pop(0)
    SNR = []
    RSSI = []
    Gateway_Lat = []
    Gateway_Long = []
    Gateway_Alt = []
    Altitude = []
    latitude = []
    longitude = []
    Gateway_Id=[]
    for row in rows:
        if row[4]==id:
            Gateway_Id.append(row[4])
            Gateway_cord=GatewaysModule.Gateways.getGateWayCoord(id)
            Gateway_Lat.append(Gateway_cord[0])
            Gateway_Long.append(Gateway_cord[1])
            Gateway_Alt.append(Gateway_cord[2])
            SNR.append(row[8])
            RSSI.append(row[9])
            Altitude.append(row[15])
            latitude.append(row[13])
            longitude.append(row[14])
    tab=[SNR,
            RSSI,
            longitude,
            latitude,
            Altitude,
            Gateway_Long,
            Gateway_Lat,
            Gateway_Alt,
            Gateway_Id]
    tab2=ManageDataModule.TransformCSV.NewCSVtoListData(id)
    tab=ManageDataModule.TransformCSV.addTab(tab,tab2)
    return tab


def toFloat(tab):
    for i in range(len(tab)):
        tab[i]=float(tab[i])
    return tab


def get_list_data():
    rows = []
    file = open('ManageDataModule/Données.CSV')
    file2 = open('ManageDataModule/DonnéesV2.CSV')
    file3 = open('ManageDataModule/DonnéesV3.CSV')
    file4 = open('ManageDataModule/DonnéesV4.CSV')
    file5= open('ManageDataModule/DonnéesV5.CSV')
    file6= open('ManageDataModule/DonnéesV6.CSV')
    def rowsAppendRow(rows, file):
        type(file)
        csvreader = csv.reader(file)
        rowTemp = []
        for row in csvreader:
            rowTemp.append(row)
        rowTemp.pop(0)
        rowTemp.pop()
        rowTemp.pop()
        for row in rowTemp:
            rows.append(row)
        return rows

    # rows= rowsAppendRow(rows,file)
    rows = rowsAppendRow(rows, file2)
    rows = rowsAppendRow(rows, file3)
    rows = rowsAppendRow(rows, file4)
    rows = rowsAppendRow(rows, file5)
    rows = rowsAppendRow(rows, file6)

    SNR = []
    RSSI = []
    rows.pop()
    rows.pop()
    Gateway_id = []
    Gateway_Lat = []
    Gateway_Long = []
    Gateway_Alt = []
    Altitude = []
    latitude = []
    longitude = []
    Gateway_Id=[]
    Gateway_cord = GatewaysModule.Gateways.getGatewaysNames()
    for row in rows:
        if (GatewaysModule.Gateways.isIn(row[4],Gateway_cord) and row[13]!='4/5'):
            if (16<float(row[13])<17 and 108<float(row[14])<109):
                Gateway_id.append(row[4])
                SNR.append(row[8])
                RSSI.append(row[9])
                Altitude.append(row[15])
                latitude.append(row[13])
                longitude.append(row[14])
    toFloat(SNR)
    toFloat(RSSI)
    toFloat(Altitude)
    toFloat(latitude)
    toFloat(longitude)

    for id in Gateway_id:
        Gateway_cord = GatewaysModule.Gateways.getGateWayCoord(id)
        Gateway_Lat.append(Gateway_cord[0])
        Gateway_Long.append(Gateway_cord[1])
        Gateway_Alt.append(Gateway_cord[2])

    return [SNR,
            RSSI,
            longitude,
            latitude,
            Altitude,
            Gateway_Long,
            Gateway_Lat,
            Gateway_Alt,
            Gateway_Id]

"""
#retourne une liste : [[X_train,Y_train],[X_test,Y_test]]
#Avec X_train=[[longitude,latitude,Altitude,Gateway_Long,Gateway_Lat,Gateway_Alt] * nombres de données*8/10]
#Y_train=[RSSI*nombres de données*8/10]
#X_Test=[[longitude,latitude,Altitude,Gateway_Long,Gateway_Lat,Gateway_Alt] * nombres de données*2/10]
#Y_train=[RSSI*nombres de données*2/10]
def getData():
    Data = get_list_data() #Retourne le tableau suivant:  [SNR, RSSI,longitude,latitude,Gateway_Long,Altitude,Gateway_Lat,Gateway_Alt]
    X = Data[2:8] #Toutes les données utiles pour calculer le RSSI
    Y = Data[1] #RSSI
    l = len(Y) #Nombre de données
    Ratio = 8 / 10 #ratio train/test
    X_test = []
    X_train = []
    Y_test = []
    Y_train = []
    for i in range(1,l-1): #Pour chaque donnée
        rand=random()
        if (rand<Ratio):
            X_train.append(ManageDataUtile.remplieX(X,i))
            Y_train.append(ManageDataUtile.remplieY(Y,i))
        else:
            X_test.append(ManageDataUtile.remplieX(X,i))
            Y_test.append(ManageDataUtile.remplieY(Y,i))
    return ([X_train,Y_train],[X_test,Y_test])
"""
#retourne une liste : [[X_train,Y_train],[X_test,Y_test]]
#Avec X_train=[[longitude,latitude,Altitude,Gateway_Long,Gateway_Lat,Gateway_Alt] * nombres de données*8/10]
#Y_train=[RSSI*nombres de données*8/10]
#X_Test=[[longitude,latitude,Altitude,Gateway_Long,Gateway_Lat,Gateway_Alt] * nombres de données*2/10]
#Y_train=[RSSI*nombres de données*2/10]
def getDataBYGATEWAYID(RSSIorSNR,id):
    Data = get_list_data_per_Gateway(id) #Retourne le tableau suivant:  [SNR, RSSI,longitude,latitude,Gateway_Long,Altitude,Gateway_Lat,Gateway_Alt]
    X = Data[2:8] #Toutes les données utiles pour calculer le RSSI
    Y=[]
    if (RSSIorSNR=="RSSI"):
        Y = Data[1] #RSSI
    elif(RSSIorSNR=="SNR"):
        Y= Data[0]
    else:
        for i in range(len(Data[0])):
            temp=[]
            temp.append(Data[0][i])
            temp.append(Data[1][i])
            Y.append(temp)
    IDs=Data[8]
    l = len(Y) #Nombre de données
    Ratio = 8 / 10 #ratio train/test
    X_test = []
    X_train = []
    Y_test = []
    Y_train = []
    for i in range(1,l-1):
        if IDs[i]==id:
            rand=random()
            if (rand<Ratio):
                X_train.append(ManageDataUtile.remplieX(X, i))
                if (RSSIorSNR=="RSSI"or RSSIorSNR=="SNR"):
                    Y_train.append(ManageDataUtile.remplieY(Y,i))
                else:
                    Y_train.append(ManageDataUtile.remplieTabY(Y, i))

            else:
                X_test.append(ManageDataUtile.remplieX(X, i))
                if(RSSIorSNR=="RSSI"or RSSIorSNR=="SNR"):
                    Y_test.append(ManageDataUtile.remplieY(Y,i))
                else:
                    Y_test.append(ManageDataUtile.remplieTabY(Y, i))
    return ([X_train,Y_train],[X_test,Y_test])