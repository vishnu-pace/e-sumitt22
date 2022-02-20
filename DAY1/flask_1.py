from flask import Flask, render_template
webApp = Flask( __name__ )

@webApp.route('/')
def homePage():
    return 'WELCOME HOME'

@webApp.route('/main')
def mainPage():
    return render_template( 'home.html' )

@webApp.route( '/main/<pinNum>/<status>' )
def readNumber( pinNum, status ):
    if int(status) == 1:
        #GPIO.output( pinNum, 1 )
        return str(pinNum) + ' is ON'
    elif int(status) == 0:
        #GPIO.output( pinNum, 0 )
        return str(pinNum) + ' is OFF'


if __name__ == '__main__':
    webApp.run( host= '0.0.0.0', port=80, debug=True )
