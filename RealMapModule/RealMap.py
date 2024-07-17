import folium
from folium.plugins import HeatMap

import CalculModule.Calcul
import ManageDataModule.ManageData
import RealMapModule.RealMapUtile
import GatewaysModule

def showHeatMapGateway(SNRorRSSIorSIGNAL,GateWay):
    dataPred=RealMapModule.RealMapUtile.DataPredToLatLongValue(SNRorRSSIorSIGNAL,GateWay) #Lat, Long, Value
    dataReel=RealMapModule.RealMapUtile.DataReelToLatLongValue(SNRorRSSIorSIGNAL,GateWay) #
    showHeatMap(dataReel,dataPred,GateWay)

def showAllMaxData(SNRorRSSIorSIGNAL):
    Data= RealMapModule.RealMapUtile.getMaxPredAllData(SNRorRSSIorSIGNAL)
    DataPred=Data[1]
    DataReel=RealMapModule.RealMapUtile.DataReelToLatLongValue(SNRorRSSIorSIGNAL,"all") #toutes les gateways
    showHeatMap(DataReel,DataPred)

def showHeatMap(DataReel, DataPred,GateWay="all"):
    import pandas as pd
    import plotly.graph_objects as go
    LatReel = []
    LongReel = []
    RSSIreel = [] #Appelé RSSI, cela peut aussi ête le SNR ou le SIGNAL
    for i in range(len(DataReel)):
        LatReel.append(DataReel[i][0])
        LongReel.append(DataReel[i][1])
        RSSIreel.append(DataReel[i][2])
    lat = []
    lon = []
    RSSI = []
    for i in range(len(DataPred)):
        lat.append(DataPred[i][0])
        lon.append(DataPred[i][1])
        RSSI.append(DataPred[i][2])
    RSSI=RealMapModule.RealMapUtile.scaleData(RSSI)
    geo_stat_list_final = pd.DataFrame({'Lat': lat, 'Long': lon, 'Signal': RSSI})
    geo_stat_list_final['weight'] = geo_stat_list_final['Signal']
    fig = go.Figure(go.Densitymapbox(lat=geo_stat_list_final.Lat,
                                     lon=geo_stat_list_final.Long,
                                     z=geo_stat_list_final.weight,
                                     radius=33,
                                     colorscale=[[0.0, 'blue', ], [0.5, 'lime'], [0.7, 'yellow'], [0.9, 'orange'],
                                                 [1.0, 'red']],  # custome colorscale
                                     zmin=0.0,
                                     zmax=1.0,
                                     opacity=0.7
                                     ))
    GateWayCo=GatewaysModule.Gateways.getGateWayCoord(GateWay)
    Lat=[GateWayCo[0]]
    Long=[GateWayCo[1]]
    if GateWay=="all":
        GateWaysCo=RealMapModule.RealMapUtile.getGateWaysCoord()
        Lat=GateWaysCo[0]
        Long=GateWaysCo[1]
    fig.add_trace(go.Scattermapbox(
        mode="markers",
        lat=Lat,
        lon=Long,
        hovertext="oui",
        marker={'color': "blue",
                "size": 30},
    ))
    """
    Blue = []
    LatBlue = []
    LongBlue = []
    LightBlue = []
    LatLightBlue = []
    LongLightBlue = []
    Green = []
    LatGreen = []
    LongGreen = []
    Yellow = []
    LatYellow = []
    LongYellow = []
    Orange = []
    LatOrange = []
    LongOrange = []
    Red = []
    LatRed = []
    LongRed = []
    for i in range(len(RSSIreel)):
        rssi = RSSIreel[i]
        lat = LatReel[i]
        long = LongReel[i]
        if rssi > 120:
            Blue.append(rssi)
            LatBlue.append(lat)
            LongBlue.append(long)
        elif 115 < rssi < 120:
            LightBlue.append(rssi)
            LatLightBlue.append(lat)
            LongLightBlue.append(long)
        elif 110 < rssi < 115:
            Green.append(rssi)
            LatGreen.append(lat)
            LongGreen.append(long)
        elif 105 < rssi < 110:
            Yellow.append(rssi)
            LatYellow.append(lat)
            LongYellow.append(long)
        elif 100 < rssi < 105:
            Orange.append(rssi)
            LatOrange.append(lat)
            LongOrange.append(long)
        else:
            Red.append(rssi)
            LatRed.append(lat)
            LongRed.append(long)
    fig.add_trace(go.Scattermapbox(
        mode="markers",
        lat=LatRed,
        lon=LongRed,
        hovertext="Signal<100",
        marker={'color': "red",
                "size": 10},
    ))
    fig.add_trace(go.Scattermapbox(
        mode="markers",
        lat=LatOrange,
        lon=LongOrange,
        hovertext="100<Signal<105",
        marker={'color': "orange",
                "size": 10},
    ))
    fig.add_trace(go.Scattermapbox(
        mode="markers",
        lat=LatYellow,
        lon=LongYellow,
        hovertext="105<Signal<110",
        marker={'color': "yellow",
                "size": 10},
    ))
    fig.add_trace(go.Scattermapbox(
        mode="markers",
        lat=LatGreen,
        lon=LongGreen,
        hovertext="110<Signal<115",
        marker={'color': "green",
                "size": 10},
    ))
    fig.add_trace(go.Scattermapbox(
        mode="markers",
        lat=LatBlue,
        lon=LongBlue,
        hovertext="115<Signal<120",
        marker={'color': "blue",
                "size": 10},
    ))
    fig.add_trace(go.Scattermapbox(
        mode="markers",
        lat=LatLightBlue,
        lon=LongLightBlue,
        hovertext="Signal>120",
        marker={'color': "purple",
                "size": 10},
    ))
    """
    fig.update_layout(mapbox_style="carto-positron",
                      mapbox_center_lon=108.130018,
                      mapbox_center_lat=16.10912,
                      mapbox_zoom=11.8)


    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.show()


def RSSItoColor(RSSItab,fig,go,LatReel,LongReel):
    Blue=[]
    LatBlue=[]
    LongBlue=[]
    LightBlue=[]
    LatLightBlue=[]
    LongLightBlue=[]
    Green=[]
    LatGreen=[]
    LongGreen=[]
    Yellow=[]
    LatYellow=[]
    LongYellow=[]
    Orange=[]
    LatOrange=[]
    LongOrange=[]
    Red=[]
    LatRed=[]
    LongRed=[]
    for i in range(len(RSSItab)):
        rssi=RSSItab[i]
        lat=LatReel[i]
        long=LongReel[i]
        if rssi>120:
            Blue.append(rssi)
            LatBlue.append(lat)
            LongBlue.append(long)
        elif 115<rssi<120:
            LightBlue.append(rssi)
            LatLightBlue.append(lat)
            LongLightBlue.append(long)
        elif 110<rssi<115:
            Green.append(rssi)
            LatGreen.append(lat)
            LongGreen.append(long)
        elif 105<rssi<110:
            Yellow.append(rssi)
            LatYellow.append(lat)
            LongYellow.append(long)
        elif 100<rssi<105:
            Orange.append(rssi)
            LatOrange.append(lat)
            LongOrange.append(long)
        else:
            Red.append(rssi)
            LatRed.append(lat)
            LongRed.append(long)
    fig.add_trace(go.Scattermapbox(
        mode="markers",
        lat=LatRed,
        lon=LongRed,
        hovertext="oui",
        marker={'color': "red",
                "size": 10},
    ))
    fig.add_trace(go.Scattermapbox(
        mode="markers",
        lat=LatOrange,
        lon=LongOrange,
        hovertext="oui",
        marker={'color': "orange",
                "size": 10},
    ))
    fig.add_trace(go.Scattermapbox(
        mode="markers",
        lat=LatYellow,
        lon=LongYellow,
        hovertext="oui",
        marker={'color': "yellow",
                "size": 10},
    ))
    fig.add_trace(go.Scattermapbox(
        mode="markers",
        lat=LatGreen,
        lon=LongGreen,
        hovertext="oui",
        marker={'color': "yellow",
                "size": 10},
    ))
    fig.add_trace(go.Scattermapbox(
        mode="markers",
        lat=Blue,
        lon=Blue,
        hovertext="oui",
        marker={'color': "blue",
                "size": 10},
    ))
    fig.add_trace(go.Scattermapbox(
        mode="markers",
        lat=LightBlue,
        lon=LightBlue,
        hovertext="oui",
        marker={'color': "blue",
                "size": 10},
    ))




