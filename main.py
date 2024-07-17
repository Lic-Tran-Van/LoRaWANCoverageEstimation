import SignalPred
import VerifDataModule.VerifData
from RealMapModule import RealMap
import RealMapModule
from VerifPrediction import verifiePredExp

RSSIorSNR="RSSI"
#print(verifiePredExp("trungnam",RSSIorSNR))

print(SignalPred.showSignalPred("Signal","trungnam"))


RealMap.showHeatMapGateway('signal',"danangdrt")
RealMap.showHeatMapGateway('signal',"trungnam")
RealMap.showHeatMapGateway('signal',"7276ff002e06029f")
RealMap.showHeatMapGateway('signal',"7276ff002e0507da")
RealMapModule.RealMap.showAllMaxData('signal')

RealMap.showHeatMapGateway('signal',"7276ff002e06029f")
RealMap.showHeatMapGateway('signal',"rfthings-rak7240-79ed")



#RealMapModule.RealMap.showAllMaxData('RSSI')
#RealMapModule.RealMap.showAllMaxData('SNR')
#RealMapModule.RealMap.showAllMaxData('signal')

#print(VerifDataModule.VerifData.distanceRSSI())
#VerifDataModule.VerifData.matriceCorr()

#print(SignalPred.showSignalPredAll("Signal"))
#print(VerifDataModule.VerifData.seeDoublon("trungnam"))
#print(VerifDataModule.VerifData.showdataDensity("RSSI"))
#print(VerifDataModule.VerifData.showdataDensity("Singal"))

#RealMapModule.RealMap.test()

