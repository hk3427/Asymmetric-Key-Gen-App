from flask import Flask
from flask_restful import Resource, Api
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import json

app = Flask(__name__)
api = Api(app)

class keygen(Resource):
    def get(self):
        private_key = RSA.generate(2048) #2048 bit key
        public_key = private_key.publickey()
        private_decoded = private_key.export_key().decode()
        public_decoded = public_key.export_key().decode()
        rsa_dict = {'public_key': public_decoded, 'private_key': private_decoded}
        rsa_output = json.dumps(rsa_dict)
        return rsa_output

api.add_resource(keygen, '/key')

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)