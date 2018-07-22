import requests, json
import Adafruit_DHT as dht
import time


while True:

        h,t = dht.read_retry(dht.DHT22, 4)
        print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t, h)

        url="http://210.125.84.68:48080/api/v1/event"

        payload = {"origin":1471806386919,"device":"thermostat","readings":[{"origin":1471806386919,"name":"temperature","value":t}, {"origin":1471806386919,"name":"humidity","value":h}]}

        headers={"Accept": "application/json", "Content-Type" : "application/json"}


        response = requests.post(url, data=json.dumps(payload), headers=headers)


        print(response.text)
        print(response.headers)

        time.sleep(10) ##delay time 100 seconds




##curl -X POST -H "Accept: application/json" -H "Content-Type: application/json" -d '{"name":"temperature","min":"-40","max":"140","type":"F","uomLabel":"degree cel","defaultValue":"0","formatting":"%s","labels":["temp","hvac"]}' http://210.125.84.68:48080/api/v1/valuedescriptor

##curl -X POST -H "Accept: application/json" -H "Content-Type: application/json" -d '{"name":"humidity","min":"0","max":"100","type":"F","uomLabel":"per","defaultValue":"0","formatting":"%s","labels":["humidity","hvac"]}' http://210.125.84.68:48080/api/v1/valuedescriptor

##curl -X POST -H "Accept: application/json" -H "Content-Type: application/json" -d '{"origin":1471806386919,"device":"thermostat","readings":[{"origin":1471806386919,"name":"temperature","value":"72"}, {"origin":1471806386919,"name":"humidity","value":"58"}]}' http://210.125.84.68:48080/api/v1/event