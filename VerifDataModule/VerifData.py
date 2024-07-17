import plotly
import sns as sns
from matplotlib import pyplot as plt

import CalculModule.Calcul
import ManageDataModule.ManageData


def showdataDensity(RSSIorSNR):
    RSSI=getRSSIorSNRById(RSSIorSNR,"trungnam")
    RSSI2 = getRSSIorSNRById(RSSIorSNR,"7276ff002e0507da")
    RSSI3 = getRSSIorSNRById(RSSIorSNR,"7276ff002e06029f")
    RSSI4=getRSSIorSNRById(RSSIorSNR,"rfthings-rak7240-79ed")
    RSSI5=getRSSIorSNRById(RSSIorSNR,"danangdrt")

    RSSITot=getTotalRSSI(RSSI,RSSI2,RSSI3,RSSI4,RSSI5)

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import kde
    if(RSSIorSNR=="RSSI"):
        min=-130
        max=-70
    elif(RSSIorSNR=="SNR") :
        min=-15
        max=15
    else :
        min=-145
        max=-55
    density = kde.gaussian_kde(RSSITot)
    x = np.linspace(min, max, 300)
    y = density(x)
    plt.plot(x, y, color='black')

    density = kde.gaussian_kde(RSSI5)
    x = np.linspace(min, max, 300)
    y = density(x)
    plt.plot(x, y, color='purple')

    density = kde.gaussian_kde(RSSI4)
    x = np.linspace(min, max, 300)
    y = density(x)
    plt.plot(x, y, color='yellow')


    density = kde.gaussian_kde(RSSI3)
    x = np.linspace(min, max, 300)
    y = density(x)
    plt.plot(x, y, color='green')


    density = kde.gaussian_kde(RSSI2)
    x = np.linspace(min, max, 300)
    y = density(x)
    plt.plot(x, y, color='red')


    density = kde.gaussian_kde(RSSI)
    x = np.linspace(min, max, 300)
    y = density(x)
    plt.plot(x, y, color='blue')
    plt.legend(['Total','danangdrt','rfthings-rak7240-79ed','7276ff002e06029f','7276ff002e0507da','trungnam'])

    if (RSSIorSNR=="RSSI"):
        plt.title("Density Plot of the RSSI")
    elif(RSSIorSNR=="SNR"):
        plt.title("Density Plot of the SNR")
    else:
        plt.title("Density Plot of the signal")

    plt.show()

def getRSSIorSNRById(RSSIorSNR,id):
    data=ManageDataModule.ManageData.get_list_data_per_Gateway(id)
    RSSI = [] #orSNR
    for i in range(len(data[1])):
        if (RSSIorSNR=="RSSI"):
            RSSI.append(float(data[1][i]))
        elif (RSSIorSNR=="SNR"):
            RSSI.append(float(data[0][i]))
        else :
            RSSIval=float(data[1][i])
            SNR=float(data[0][i])
            if SNR<0 :
                RSSIval=RSSIval+SNR
            RSSI.append(RSSIval)
    return RSSI

def getTotalRSSI(RSSI1,RSSI2,RSSI3,RSSI4,RSSI5):
    RSSI=[]
    for i in range(len(RSSI1)):
        RSSI.append(RSSI1[i])
    for i in range(len(RSSI2)):
        RSSI.append(RSSI2[i])
    for i in range(len(RSSI3)):
        RSSI.append(RSSI3[i])
    for i in range(len(RSSI4)):
        RSSI.append(RSSI4[i])
    for i in range(len(RSSI5)):
        RSSI.append(RSSI5[i])
    return RSSI

def seeDoublon(id):
    data=ManageDataModule.ManageData.get_list_data_per_Gateway(id)
    doublonsRSSI=[]
    doublonsComplet=[]
    for i in range(len(data[1])):
        for j in range(i):
            if i!=j:
                if(data[1][i]==data[1][j]):
                    doublonsRSSI.append([i,j])
                    if(data[2][i]==data[2][j] and data[3][i]==data[3][j]):
                        doublonsComplet.append([i,j])
                        print(j-i)
    return doublonsComplet, len(doublonsComplet)

def matriceCorr():
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    data=ManageDataModule.ManageData.get_list_data()
    SNR=data[0]
    RSSI=data[1]
    Long=data[2]
    Lat=data[3]
    Alt=data[4]
    Id=data[5]
    print(len(SNR))
    print(len(RSSI))
    print(len(Long))
    print(len(Lat))
    print(len(Alt))
    print(len(Id))
    employees_df = pd.DataFrame({
        'Alt': Alt,
        'Lat': Lat,
        'Long': Long,
        'RSSI': RSSI,
        'SNR' : SNR

    })
    print("The DataFrame of Employees is:")
    print(employees_df, "\n")

    corr_df = employees_df.corr()
    print("The correlation DataFrame is:")
    print(corr_df, "\n")
    corr_df = employees_df.corr(method='pearson')

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_df, annot=True)
    plt.show()

#Montre un graphique : RSSI/Distance
def distanceRSSI():
    data=ManageDataModule.ManageData.get_list_data()
    RSSI=data[1]
    TabDist=[]
    for i in range(len(RSSI)):
        lat=data[2][i]
        long=data[3][i]
        GatewayLat=data[5][i]
        GatewayLong=data[6][i]
        dist=CalculModule.Calcul.distance([lat,long],[GatewayLat,GatewayLong])
        TabDist.append(dist)
    plt.scatter(TabDist, RSSI)
    plt.title('RSSI en fonction de la distance')
    plt.xlabel('Distance')
    plt.ylabel('RSSI')
    plt.show()
    #[SNR, RSSI,, latitude, longitude Altitude, Gateway_Lat, Gateway_Long, Gateway_Alt, Gateway_Id]




