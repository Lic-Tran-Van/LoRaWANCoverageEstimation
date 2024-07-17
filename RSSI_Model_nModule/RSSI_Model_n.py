# Calcule la puissance du signal théorique en fonction de la distance entre la gateway et le point de mesure.
#Dépend aussi de la variable d'environnement n
import PredPosModule.PredPos
from ApproximationModule import Approximation
from CalculModule import Calcul
from CalculModule.Calcul import tableDist
import RSSI_Model_nModule
#Calcul le tableau contenant toutes les valeurs du RSSI
#tab=#tab= [[X_train,Y_train],[X_test,Y_test]
#Renvoie un tableau contenant len(Y_train) RSSI
#Train est un boolen qui vaut True si on veut calc train et false si

def RSSItabcalc(RSSIorSNR,tab,n_tab,Train):
    RSSI_tab = []
    n_calc = Approximation.predictNTab_CloseTo(tab, n_tab)
    tabDist = tableDist(tab, Train)
    for i in range(len(tabDist) - 1):
        dist = tabDist[i]
        RSSI=RSSIcalc(RSSIorSNR,dist,n_calc[i],tab)
        RSSI_tab.append(RSSI)
    return RSSI_tab  # Retourne le tableau avec toutes les prédictions du signal SSI (len(Y_train))

#de même mais on utilise une heat map, donc tous les points avec un exp
def RSSItabcalcExp(tab,n_tab,RSSIorSNR):
    RSSI_tab = []
    X_Test=tab[1][0]
    # retourne une liste : [[X_train,Y_train],[X_test,Y_test]]
    # Avec X_train=[[longitude,latitude,Altitude,Gateway_Long,Gateway_Lat,Gateway_Alt] * nombres de données*8/10]
    tabDist = tableDist(tab, False)
    for i in range(len(X_Test)):
        lat=(float(X_Test[i][1]))
        long=(float(X_Test[i][0]))
        n = PredPosModule.PredPos.predictN_Exp(tab, n_tab, [lat,long])
        dist = tabDist[i]
        RSSI=RSSIcalc(RSSIorSNR,dist,n,tab)
        #if (RSSI_Model_nModule.RSSI_Model_nUtile.estTropLoin(i, tab)):
        #    faitqqchose
        RSSI_tab.append(RSSI)
    return RSSI_tab  # Retourne le tableau avec toutes les prédictions du signal SSI (len(Y_train))

def reference(RSSIorSNR,tab):
    data=tab[1][0] #Y_train :RSSI
    #Distance=260 #Point choisi arbitrairement (proche et signal puissant)
    Gateway2Lat = 16.1089199
    Gateway2Long = 108.1275935
    lat=16.109162
    long=108.130013
    #distance= Calcul.distance([long, lat], [Gateway2Long, Gateway2Lat]) #Calcul distance rescale
    distance=0.0000001
    lat_tab= Calcul.mini_maxi_lat(data) #min,max
    latMin=lat_tab[0]
    latMax=lat_tab[1]
    #longMin=lat_tab[0]  On scale avec les mêmes valeurs, pour pouvoir inverser la fonction scale
    #longMax=lat_tab[1]
    #lat= Calcul.scale(lat, latMin, latMax) #On scale long et lat NE PAS SUPPRIMER : version qui marche
    lat=Calcul.noScale(lat)
    #long= Calcul.scale(lat, latMin, latMax)  #NE PAS SUPPRIMER
    long=Calcul.noScale(long)
    if RSSIorSNR=="RSSI":
        RSSI=-80
    else :
        RSSI=0 #ici RSSI vaut SNR
    return [distance,RSSI]


#Calcul le RSSI en fonction de la distance, de la variable d'environnement n_tab propre au point et à RSSIref
#Retourne un tableau d'RSSI
import math

from CalculModule import Calcul
from RSSI_Model_nModule import RSSI_Model_n


def RSSIcalc(RSSIorSNR,distance,n,tab, donneXY="ok"):
    ref=RSSI_Model_n.reference(RSSIorSNR,tab)
    distanceref=ref[0]
    RSSIref=(ref[1]) #ref=[Distance,RSSI]
    Val=RSSIref -10*float(n)*(math.log(distance/distanceref))
    if RSSIorSNR=="RSSI":
        if Val<-120:
            return -120
        if Val>-70:
            return -70
        else:
            return Val
    else:
        if Val>12:
            return 12
        if Val<-12:
            return -12
        return Val
