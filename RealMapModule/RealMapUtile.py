import math
from math import *
import CalculModule.Calcul
import ManageDataModule.ManageData
import SignalPred
from ManageDataModule import ManageData
from PredPosModule import PredPos
from Learn_n_RSSIModule import Learn_n_RSSI

def DataReelToLatLongValue(RSSIorSNRorSIGNAL,GateWay):
    if (GateWay=="all"):
        data = ManageDataModule.ManageData.get_list_data()
    else :
        data=ManageDataModule.ManageData.get_list_data_per_Gateway(GateWay)
    # Retourne le tableau suivant:  [SNR,  RSSI,longitude,latitude,Altitude,Gateway_Lat,Gateway_Long,Gateway_Alt, Gateway_Id]
    l=len(data[0])
    tab=[]
    for i in range(l):
        Lat=float(data[3][i])
        Long=float(data[2][i])
        if(RSSIorSNRorSIGNAL=="RSSI"):
            Value=float(data[1][i])
        elif(RSSIorSNRorSIGNAL=="SNR"):
            Value=float(data[0][i])
        else:
            ValueRSSI=float(data[1][i])
            ValueSNR=float(data[0][i])
            if (ValueSNR)<0:
                Value=ValueRSSI-ValueSNR
            else :
                Value=ValueRSSI
        tab.append([Lat,Long,Value])
    return tab

def DataPredToLatLongValue(SNRorRSSIorSIGNAL,GateWay):
    data=ManageDataModule.ManageData.get_list_data_per_Gateway(GateWay)
    alldata=ManageDataModule.ManageData.get_list_data()
    l=alldata[2]
    minLong=CalculModule.Calcul.mini(l)
    maxLong=CalculModule.Calcul.maxi(l)
    dlong=maxLong-minLong
    l=alldata[3]
    minLat=CalculModule.Calcul.mini(l)
    maxLat=CalculModule.Calcul.maxi(l)
    dlat=maxLat-minLat
    n = 50
    NombreDonnées = n ** 2
    ResTab = []
    ResTabRSSI= []
    ResTabSNR= []

    tabRSSI= ManageData.getDataBYGATEWAYID("RSSI",GateWay) #[[X_train,Y_train],[Y_train,Y_test]] #On ne s'interesse qu'à UNE gateway.
    n_tab_trainRSSI = Learn_n_RSSI.learn_n("RSSI",tabRSSI)  # [n *len(X_train)]) #Apprend n_tab grâce pour Y_train
    for i in range(n):
        for j in range(n):
            lat = (dlong * j) / n + minLat
            long = (dlong * i) / n + minLong
            RSSI = PredPos.predict_Exp(long, lat, tabRSSI, n_tab_trainRSSI, GateWay, "RSSI")
            ResTabRSSI.append([lat, long, RSSI])

    tabSNR= ManageData.getDataBYGATEWAYID("SNR",GateWay) #[[X_train,Y_train],[Y_train,Y_test]] #On ne s'interesse qu'à UNE gateway.
    n_tab_trainSNR= Learn_n_RSSI.learn_n("SNR",tabSNR)  # [n *len(X_train)]) #Apprend n_tab grâce pour Y_train
    for i in range(n):
        for j in range(n):
            lat = (dlong * j) / n + minLat
            long = (dlong * i) / n + minLong
            SNR = PredPos.predict_Exp(long, lat, tabSNR, n_tab_trainSNR, GateWay, "SNR")
            ResTabSNR.append([lat, long, SNR])

    for i in range(len(ResTabRSSI)):
        snr=ResTabSNR[i][2]
        rssi=ResTabRSSI[i][2]
        if snr<0:
            rssi=rssi-snr
        ResTab=ResTabRSSI
        ResTab[i][2]=rssi
    if(SNRorRSSIorSIGNAL=="RSSI"):
        return ResTabRSSI
    elif(SNRorRSSIorSIGNAL=="SNR"):
        return ResTabSNR
    else:
        return ResTab

"""
def DataPredToLongLatValueAll():
    data=ManageDataModule.ManageData.get_list_data()
    tab = ManageData.getData()  # [[X_train,Y_train],[Y_train,Y_test]] #On ne s'interesse qu'à UNE gateway.
    n_tab_train = Learn_n_RSSI.learn_n(tab)  # [n *len(X_train)]) #Apprend n_tab grâce pour Y_train
    l = data[2]
    minLong = CalculModule.Calcul.mini(l)
    maxLong = CalculModule.Calcul.maxi(l)
    dlong = maxLong - minLong
    l = data[3]
    minLat = CalculModule.Calcul.mini(l)
    maxLat = CalculModule.Calcul.maxi(l)
    dlat = maxLat - minLat
    n = 50
    NombreDonnées = n ** 2
    ResTab = []
    for i in range(n):
        for j in range(n):
            long = (dlong * i) / n + minLong
            lat = (dlong * j) / n + minLat
            RSSI = PredPos.predict_Exp(long, lat, tab, n_tab_train)
            ResTab.append([lat, long, RSSI])
    ResTab = scaleData(ResTab)
    return ResTab
"""
def scaleData(tab):
    #min=CalculModule.Calcul.mini(tab)
    #max=CalculModule.Calcul.maxi(tab)
    min = -130
    max = -70
    for i in range(len(tab)):
        tab[i]=((tab[i]-min)/(max-min))**(1/2)
    return tab

"""
def antiScaleData(tab):
    min=CalculModule.Calcul.mini(tab)
    max=CalculModule.Calcul.maxi(tab)
    for i in range(len(tab)):
        val=tab[i]
        a=math.sqrt(val)*(max-min)+min
        tab[i]=a
    return tab
"""


# Retourne :[AllDataReel, AllMaxDataPred]
def getMaxPredAllData(SNRorRSSIorSIGNAL):
    import pandas as pd
    import plotly.graph_objects as go
    allDataReel = []
    allDataPred = []
    DataMaxPred = []
    GateWaysId = ["7276ff002e0507da", "trungnam", "danangdrt"]
    for id in (GateWaysId):
        dataPred = DataPredToLatLongValue(SNRorRSSIorSIGNAL,id)
        dataReel = ManageDataModule.ManageData.get_list_data_per_Gateway(id)
        allDataReel+=dataReel  # [[Data1],Data2...,Data5]
        allDataPred.append(dataPred)
    # On va calculer le maximum des signals reçu par chaque gateway pour savoir si l'endroit est bien deservie par des gateways.
    for i in range(len(allDataPred[0])): #Pour chaque donnée
        temp = []
        for j in range(len(allDataPred)): #Pour chaque Gateway
            temp.append(allDataPred[j][i][2]) #allData=[Gateway[data[Long,lat,Value]]]
        maxInd = CalculModule.Calcul.maxiInd(temp)[1] #Indice ou on capte le mieux 'min et max inversés avec la valeur
        print(temp, maxInd)
        DataMaxPred.append(allDataPred[maxInd][i])
    return [allDataReel, DataMaxPred]






def getGateWaysCoord():
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
    return [[Gateway1Lat,Gateway2Lat,Gateway3Lat,Gateway4Lat,Gateway5Lat],[Gateway1Long,Gateway2Long,Gateway3Long,Gateway4Long,Gateway5Long]]
