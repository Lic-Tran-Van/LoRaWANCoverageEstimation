from CalculModule import Calcul


#Calcul le RSSI moyen dans le cercle choisi
def moyRSSI(tab,i):
    A=1
    RSSImoy = 0
    for j in range(len(tab[1])):
        if (Calcul.distance(tab[0][i], tab[0][j]) < A and i != j):  # Si les points sont suffisemment proche alors :
            RSSImoy += tab[1][i]
    return RSSImoy

def deletable(tab, i, RSSImoy):
    MaxEcart=1
    if abs(tab[1][i])>abs(RSSImoy+MaxEcart):
        return True
    else :
        return False


def isDeletable(deleteTabInd,j):
    for k in range(len(deleteTabInd)):
        if (j == deleteTabInd[k]):
            return True