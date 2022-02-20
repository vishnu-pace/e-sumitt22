from firebase import firebase

firebase_addr = 'https://iot-f41ad-default-rtdb.firebaseio.com/'
fire_base = firebase.FirebaseApplication( firebase_addr, None ) # Test mode

#tempVal = tempRead()
tempVal = 26.5
humidVal = 7

data = {
    'Temp': tempVal,
    'Humid': humidVal
}


fire_base.post( '/table1/sense', data )
print('DONE')