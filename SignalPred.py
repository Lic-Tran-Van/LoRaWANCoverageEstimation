from matplotlib import pyplot as plt

from CalculModule import Calcul
from ManageDataModule import ManageData
import Learn_n_RSSIModule
from RSSI_Model_nModule import RSSI_Model_n
from VerifPrediction import difMoy, difAbs, difMin, difMax


def signal(RSSI, SNR):
    if SNR <0 :
        return RSSI-SNR #RSSI est positif dans le programme au lieux de négatif.
    else :
        return RSSI


def copy(data):
    copy=[]
    for i in range(len(data)):
        tempi=[]
        for j in range(len(data[i])):
            tempj=[]
            for l in range(len(data[i][j])):
                templ=[]
                for k in range(len(data[i][j][l])):
                    templ.append(data[i][j][l][k])
                tempj.append(templ)
            tempi.append(tempj)
        copy.append(tempi)
    return copy




def showSignalPred(SNRorRSSIorSIGNAL,id):
    data = ManageData.getDataBYGATEWAYID(SNRorRSSIorSIGNAL, id)  # [[X_train,Y_train],[Y_train,Y_test]] #On ne s'interesse qu'à UNE gateway. Y_train a ici RSSI et SNR
    dataRSSI=copy(data)
    dataSNR=copy(data)
    for i in range(len(data[0][1])):
        dataRSSI[0][1][i]=data[0][1][i][1] #On recréer un tab RSSI classique
        dataSNR[0][1][i]=data[0][1][i][0]
    for i in range(len(data[1][1])):
        dataRSSI[1][1][i]=data[1][1][i][1] #On recréer un tab RSSI classique
        dataSNR[1][1][i]=data[1][1][i][0]

    n_tab_train_RSSI = Learn_n_RSSIModule.Learn_n_RSSI.learn_n("RSSI", dataRSSI)  # [n *len(X_train)]) #Apprend n_tab grâce pour Y_train
    # n_tab_test= #On Prédit les n en fonction des n les plus proches.
    dataPredRSSI = dataRSSI[1][0]  # Y_Test
    preditRSSI = RSSI_Model_n.RSSItabcalcExp(dataRSSI, n_tab_train_RSSI, "RSSI")  # Puissance du signal prédite (doit être de la taille Y_train)
    reelRSSI = (dataRSSI[1][1])  # Puissance du signal réel Y_train
    n_tab_train_SNR = Learn_n_RSSIModule.Learn_n_RSSI.learn_n("SNR",dataSNR)  # [n *len(X_train)]) #Apprend n_tab grâce pour Y_train
    # n_tab_test= #On Prédit les n en fonction des n les plus proches.
    dataPredSNR = dataSNR[1][0]  # Y_Test
    preditSNR = RSSI_Model_n.RSSItabcalcExp(dataSNR, n_tab_train_SNR, "SNR")  # Puissance du signal prédite (doit être de la taille Y_train)
    reelSNR = (dataSNR[1][1])  # Puissance du signal réel Y_train

    preditSignal=[]
    for i in range(len(preditRSSI)):
        preditSignal.append(signal(preditRSSI[i],preditSNR[i]))

    reelSignal=[]
    for i in range(len(reelRSSI)):
        reelSignal.append(signal(reelRSSI[i],reelSNR[i]))

    res = Calcul.sort(reelSignal, preditSignal)  # Reel est trié, prédit aussi de sorte à etre aligné avec reel
    reel = res[0]
    predit = res[1]
    DiffMoy = difMoy(reel, predit)
    DiffAbs = difAbs(reel, predit)
    DiffMin= difMin(reel, predit)
    DiffMax= difMax(reel, predit)
    # averagePREDIT=moving_average(predit, 30) : Courbe qui lisse les données
    # averageREEL=moving_average(reel,30)
    plt.plot(reel)
    plt.plot(predit)
    plt.xlabel('N°donnée')
    plt.ylabel('Signal')
    plt.title('Signal reel et prédit')
    legend = plt.legend(['Signal réel', 'Signal prédit'], title="Legend")
    legend.set_title("Legend", prop={'size': 15})
    # plt.plot(averagePREDIT)
    # plt.plot(averageREEL)
    plt.show()
    print("Ecart type :",DiffMoy,"Ecart des moyennes :" ,DiffAbs, "Différence minimum/Maximum= ", DiffMin,DiffMax )


def showSignalPredAll(SNRorRSSIorSIGNAL):
    tabGateway=["7276ff002e0507da","trungnam"]
    #tabGateway=["7276ff002e0507da","trungnam","7276ff002e06029f","rfthings-rak7240-79ed","danangdrt"]
    preditSignal = []
    reelSignal = []
    for id in (tabGateway):
        data = ManageData.getDataBYGATEWAYID(SNRorRSSIorSIGNAL,id)  # [[X_train,Y_train],[Y_train,Y_test]] #On ne s'interesse qu'à UNE gateway. Y_train a ici RSSI et SNR
        dataRSSI = copy(data)
        dataSNR = copy(data)
        for i in range(len(data[0][1])):
            dataRSSI[0][1][i] = data[0][1][i][1]  # On recréer un tab RSSI classique
            dataSNR[0][1][i] = data[0][1][i][0]
        for i in range(len(data[1][1])):
            dataRSSI[1][1][i] = data[1][1][i][1]  # On recréer un tab RSSI classique
            dataSNR[1][1][i] = data[1][1][i][0]

        n_tab_train_RSSI = Learn_n_RSSIModule.Learn_n_RSSI.learn_n("RSSI",
                                                                   dataRSSI)  # [n *len(X_train)]) #Apprend n_tab grâce pour Y_train
        # n_tab_test= #On Prédit les n en fonction des n les plus proches.
        dataPredRSSI = dataRSSI[1][0]  # Y_Test
        preditRSSI = RSSI_Model_n.RSSItabcalcExp(dataRSSI, n_tab_train_RSSI,
                                                 "RSSI")  # Puissance du signal prédite (doit être de la taille Y_train)
        reelRSSI = (dataRSSI[1][1])  # Puissance du signal réel Y_train

        n_tab_train_SNR = Learn_n_RSSIModule.Learn_n_RSSI.learn_n("SNR",
                                                                  dataSNR)  # [n *len(X_train)]) #Apprend n_tab grâce pour Y_train
        # n_tab_test= #On Prédit les n en fonction des n les plus proches.
        dataPredSNR = dataSNR[1][0]  # Y_Test
        preditSNR = RSSI_Model_n.RSSItabcalcExp(dataSNR, n_tab_train_SNR,
                                                "SNR")  # Puissance du signal prédite (doit être de la taille Y_train)
        reelSNR = (dataSNR[1][1])  # Puissance du signal réel Y_train

        for i in range(len(preditRSSI)):
            preditSignal.append(signal(preditRSSI[i], preditSNR[i]))

        for i in range(len(reelRSSI)):
            reelSignal.append(signal(reelRSSI[i], reelSNR[i]))

    res = Calcul.sort(reelSignal, preditSignal)  # Reel est trié, prédit aussi de sorte à etre aligné avec reel
    reel = res[0]
    predit = res[1]
    DiffMoy = difMoy(reel, predit)
    DiffAbs = difAbs(reel, predit)
    DiffMin = difMin(reel, predit)
    DiffMax = difMax(reel, predit)
    # averagePREDIT=moving_average(predit, 30) : Courbe qui lisse les données
    # averageREEL=moving_average(reel,30)
    plt.plot(reel)
    plt.plot(predit)
    plt.xlabel('N°donnée')
    plt.ylabel('Signal')
    plt.title('Signal reel et prédit')
    legend = plt.legend(['Signal réel', 'Signal prédit'], title="Legend")
    legend.set_title("Legend", prop={'size': 15})
    # plt.plot(averagePREDIT)
    # plt.plot(averageREEL)
    plt.show()
    print("Ecart type :", DiffMoy, "Ecart des moyennes :", DiffAbs, "Différence minimum/Maximum= ", DiffMin, DiffMax)