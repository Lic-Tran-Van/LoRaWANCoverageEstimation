import CalculModule.Calcul
import ManageDataModule.ManageData
import RSSI_Model_nModule
from ApproximationModule.Approximation import predictN_Exp
from RSSI_Model_nModule import RSSI_Model_n
import GatewaysModule
from GatewaysModule import Gateways


#Predit le signal d'un point à l'aide de sa position

def predict_Exp(Long, Lat, data,n_tab,GateWay,RSSIorSNR):
    donneXY=[Lat,Long]
    nPredit=predictN_Exp(data, n_tab, donneXY)
    Pos=GatewaysModule.Gateways.getGateWayCoord(GateWay)
    dist=CalculModule.Calcul.distance(donneXY,Pos)
    RSSI=RSSI_Model_nModule.RSSI_Model_n.RSSIcalc(RSSIorSNR,dist,nPredit,data, donneXY)
    return RSSI
