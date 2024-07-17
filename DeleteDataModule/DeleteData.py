from ManageDataModule import ManageData
#Retourne un tableau avec : [[Coordonée], RSSI, Gateway_id]
from DeleteDataModule import DeleteDataUtile


def InternData():
    data= ManageData.get_list_data()
    Coordonnées=[]
    tab=[]
    Rtab=[]
    Gateway_tab=[]
    for i in range(len(data[2])):
        long=float(data[2][i])
        lat=float(data[3][i])
        RSSI=float(data[1][i])
        Gateway_id=data[8][i]
        Co=[long,lat]
        Coordonnées.append(Co)
        Rtab.append(RSSI)
        Gateway_tab.append(Gateway_id)
    tab.append(Coordonnées)
    tab.append(Rtab)
    tab.append(Gateway_tab)
    return tab

def getExtremeDataInd():
    tab=InternData()
    deleteTab=[]
    for i in range (len((tab[1]))): #Pour chaque donnée
        RSSImoy= DeleteDataUtile.moyRSSI(tab,i)
        DeleteAble=DeleteDataUtile.deletable(tab,i,RSSImoy)
        if (DeleteAble):
            deleteTab.append(i) #Ajoute l'indice i du point dans un tableau ou va être supprimé les données.
    return deleteTab

#Retourne la liste des données avec des éléments de supprimés
def deleteTab():
    data= ManageData.get_list_data()#[SNR,  RSSI,longitude,latitude,Altitude,Gateway_Lat,Gateway_Long,Gateway_Alt, Gateway_Id]
    deleteTabInd=getExtremeDataInd()
    data2=data
    for j in range(len(data[0])): #Pour chaque donnée
        if (DeleteDataUtile.isDeletable(deleteTabInd,j)):
            for i in range(len(data)): #On va supprimé pour chaque type de donnée
                data2[i][j].pop(j)
    return data2


