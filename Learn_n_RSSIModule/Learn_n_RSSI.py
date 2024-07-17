import math

#Calcul n la variable d'environnement d'une donnée afin de prédire la puissance du signal.
#ref=[Distance, RSSI] elle est calculée ou choisi et est la même pour toute les données
from RSSI_Model_nModule import RSSI_Model_n
import CalculModule

#Calculate the environmental variable for a training data (real data)
def CalcN(RSSI, distance, ref):
    distref=ref[0]
    RSSIref=ref[1]
    return (RSSIref-RSSI)/(math.log(distance/distref )*10)

#Calculate the environmental variable for the training dataset
def CalcNtab(RSSI_tab,distance_tab, ref ):
    n_tab=[]
    for i in range(len(RSSI_tab)-1):
        n_tab.append(CalcN(RSSI_tab[i],distance_tab[i],ref))
    return n_tab

#renvoie un tableau avec la liste des variables d'environnements n
#data=[[X_train,Y_train],[X_test,Y_test]]
def learn_n(RSSIorSNR, data):
    n_tab=[] #Tableau contenant les variables d'environnement
    X_Train=data[0][1]
    tab_dist= CalculModule.Calcul.tableDist(data, True)  #Table des distances entre la mesure et la gateway associée.
    ref= RSSI_Model_n.reference(RSSIorSNR,data) #Ref, contien [Distance, RSSI] de reference
    n_tab= CalcNtab(X_Train, tab_dist, ref) #Calcule et stock les valeurs de n
    return n_tab
