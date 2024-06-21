from flask import Flask, request, jsonify
from unifiapi import *
from keycloakapi import *

app = Flask(__name__)

UNIFI_API_ENDPOINT = 'https://gateway.local.duentetech.de:443'
UNIFI_API_USERNAME = 'XXX'
UNIFI_API_PASSWORD = 'XXX'
UNFIF_API_SITE = 'Gateway%20-%20Dream%20Machine%20Pro'



# Beispiel für einen GET-Endpunkt
@app.route('/api/wlansso', methods=['GET'])
def get_example():
    session = unifi_login(UNIFI_API_ENDPOINT, UNIFI_API_USERNAME, UNIFI_API_PASSWORD)
    if session:
        #Get User Device MAC Address
        #Redrirct to Keycloak
        if (authorize_user(session, UNIFI_API_ENDPOINT, UNFIF_API_SITE, 'xxx', 100)):
            data = {
                'message': 'User Login Successfull',
                'status': 'success'
            }
            return jsonify(data), 200
        else:
             data = {
                'message': 'User Login Failed',
                'status': 'error'
            }
             return jsonify(data), 200
    else:
        data = {
            'message': 'Could not connect to Unifi Controller',
            'status': 'error'
        }
        return jsonify(data), 401

# Beispiel für einen POST-Endpunkt
@app.route('/api/post', methods=['POST'])
def post_example():
    if request.is_json:
        req_data = request.get_json()
        response_data = {
            'message': 'This is a POST request',
            'received': req_data,
            'status': 'success'
        }
        return jsonify(response_data), 200
    else:
        return jsonify({'message': 'Request must be JSON', 'status': 'failure'}), 400

if __name__ == '__main__':
    app.run(debug=True)