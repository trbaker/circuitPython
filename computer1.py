import serial
import requests
import ast
import time

ser = serial.Serial('/dev/cu.usbmodem143201', 115200, timeout=None)
while True:
    data_raw = ser.readline()
    # next few lines just clean up the serial data
    tempf = str(data_raw)[:7]
    tempf = tempf.replace("F", "")
    tempf = tempf.replace("b'", "")
    tempf= float(tempf)
    # print to screen (for now)
    print(tempf)
    # send data to sample ArcGIS Online service
    url = 'https://services3.arcgis.com/GzteEaZqBuJ6GIYr/arcgis/rest/services/survey123_910b6ea1c50743269a5b171a91fe6cc7_fieldworker/FeatureServer/0/addFeatures'
    #template dictionary that we'll replace item in, before sending to AGO
    params={"f":"pjson","token":"","rollbackOnFailure":"false","features":'{ \
        "attributes" : { \
            "controller" : "ACPE microcontroller sensor 1", \
            "lat" : 45.23434, \
            "lon": -94.2342, \
            "temperature" : tempf, \
            "humidity" : 0}}'
            }
    params=str(params).replace("tempf", str(tempf))
    # converts the string to a python dictionary
    params=ast.literal_eval(params)
    requests.post(url, params)
    time.sleep(2)       # integer is seconds to pause
    print('  resetting....')
