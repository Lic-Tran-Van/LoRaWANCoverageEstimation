from matplotlib import pyplot as plt

from CalculModule import Calcul
from ManageDataModule import ManageData
from RSSI_Model_nModule import RSSI_Model_n
import Learn_n_RSSIModule


def verifiePredExp(id,RSSIorSNR):
    data= ManageData.getDataBYGATEWAYID(RSSIorSNR,id) #[[X_train,Y_train],[Y_train,Y_test]] #On ne s'interesse qu'à UNE gateway.
    n_tab_train = Learn_n_RSSIModule.Learn_n_RSSI.learn_n(RSSIorSNR,data)  # [n *len(X_train)]) #Apprend n_tab grâce pour Y_train
    #n_tab_test= #On Prédit les n en fonction des n les plus proches.
    dataPred=data[1][0] #Y_Test
    predit= RSSI_Model_n.RSSItabcalcExp(data, n_tab_train, RSSIorSNR) #Puissance du signal prédite (doit être de la taille Y_train)
    reel=(data[1][1]) #Puissance du signal réel Y_train
    reel.pop()
    res = Calcul.sort(reel, predit) #Reel est trié, prédit aussi de sorte à etre aligné avec reel
    reel = res[0]
    predit = res[1]
    DiffMoy = difMoy(reel, predit)
    DiffAbs= difAbs(reel, predit)
    #averagePREDIT=moving_average(predit, 30) : Courbe qui lisse les données
    #averageREEL=moving_average(reel,30)
    plt.plot(reel)
    plt.plot(predit)
    #plt.plot(averagePREDIT)
    #plt.plot(averageREEL)
    plt.show()
    return (DiffMoy, DiffAbs)


def difMoy(reel, predit):
    DiffMoy = 0
    for i in range(len(reel)-1):
        di=abs(predit[i])-abs(reel[i])
        DiffMoy+=abs(di)
    DiffMoy=DiffMoy/(len(reel)-1)
    return DiffMoy


def difAbs(reel, predit):
    DiffMoy = 0
    for i in range(len(reel) - 1):
        di = (predit[i]) - (reel[i])
        DiffMoy += (di)
    DiffMoy = DiffMoy / (len(reel) - 1)
    return DiffMoy

def difMin(reel, predit):
    min=100
    for i in range(len(reel)):
        val=abs(predit[i]-reel[i])
        if val<min :
            min=val
    return min

def difMax(reel, predit):
    max=0
    for i in range(len(reel)):
        val=abs(predit[i]-reel[i])
        if val>max :
            max=val
    return max

def print_dataset():
    # Use a breakpoint in the code line below to debug your script.
    print(ManageData.init_Dataset())  # Press Ctrl+F8 to toggle the breakpoint.