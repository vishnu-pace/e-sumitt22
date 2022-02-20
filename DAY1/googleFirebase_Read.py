from firebase import firebase

firebase_addr = 'https://iot-f41ad-default-rtdb.firebaseio.com/'
fire_base = firebase.FirebaseApplication( firebase_addr, None ) # Test mode

recv_data = fire_base.get( '/table1/sense', '' )

records = [ record for record in recv_data ]
#print(records)

print( recv_data[records[-1]]['Temp'] )