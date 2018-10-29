import conf
from boltiot import Bolt
import json, time

mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)

response = mybolt.analogRead('A0') 
data = json.loads(response)
print ("Current light intensity is: %s" % data['value']) 
sensor_value = int(data['value']) 


while True: 
    response = mybolt.analogRead('A0') 
    data = json.loads(response) 
    # print (data['value'])
    try: 
        sensor_value = int(data['value']) 
        print ('current light intensity: '+str(sensor_value))
        if sensor_value < 100:
            response = mybolt.digitalWrite('3','LOW')
        else:
        	response = mybolt.digitalWrite('3','HIGH')
    except Exception as e: 
        print ("Error",e)
    time.sleep(10)
