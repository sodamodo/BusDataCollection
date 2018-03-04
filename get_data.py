import xml.etree.ElementTree as ET
import requests
import json
import datetime as DT



#list of route numbers
routes = [1, 2, 5, 6, 7, 8, 9, 12, 14, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30]
test_data = [{u'DirectionLong': u'Inbound', u'Destination': u'To Multimodal TC', u'RunId': 1012, u'Latitude': 33.957489, u'OnBoard': None, u'Deviation': 0, u'Direction': u'I', u'BlockFareboxId': 101, u'TripId': 1829, u'Name': u'748', u'VehicleId': 748, u'Longitude': -83.352914, u'RouteId': 2, u'OpStatus': u'ONTIME', u'Heading': 334, u'LastStop': u'Cone Dr and Zebulon IB', u'Speed': 25, u'DisplayStatus': u'On Time', u'LastUpdated': u'/Date(1520119790000-0500)/', u'GPSStatus': 2, u'CommStatus': u'GOOD', u'DriverName': u'Smith'}]
test_data_string = """[{"VehicleId":741,"Name":"741","Latitude":33.960462,"Longitude":-83.378653,"RouteId":5,"TripId":1812,"RunId":5012,"Direction":"I","DirectionLong":"Inbound","Destination":"To Multimodal TC","Speed":25,"Heading":68,"Deviation":11,"OpStatus":"LATE","CommStatus":"GOOD","GPSStatus":2,"DriverName":"Alexander","LastStop":"Dougherty and Hull IB","OnBoard":null,"LastUpdated":"\/Date(1520120741000-0500)\/","DisplayStatus":"Late","BlockFareboxId":501}]"""


#creates API URL with route number. Returns link
#
def MakeUrlGetAllVehicles(route_number):
    return "https://bustracker.accgov.com/InfoPoint/rest/Vehicles/GetAllVehiclesForRoute?routeID={}".format(route_number)

def getData(URL):
    r = requests.get(URL)
    # datetime = DT.now()
    return r.content

# Parse out LastUpdated, Latitude, Longitude, Speed. Use getData result as parameter
def parseData(bus_data):
    # print bus_data
    lat = bus_data[0][0]["Latitude"]
    long = bus_data[0]["Longitude"]

    lat_long = (lat, long)
    # # last_update = bus_data[0]["LastUpdated"]
    # # print last_update
    # print lat
    # root = ET.fromstring(bus_data)
    # print root.tag

parseData(test_data)
# parseData(getData(MakeUrlGetAllVehicles(routes[2])))