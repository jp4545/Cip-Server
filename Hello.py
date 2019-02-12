from flask import Flask
from flask import request
import base64
from base64 import decodestring
from PIL import Image


app = Flask(__name__)

@app.route('/hello',methods=['GET', 'POST'])
def hello_world():
    data = request.data
    print(data)
    image_64_decode = base64.decodestring(data) 
    image_result = open('test.jpg', 'wb')
    image_result.write(image_64_decode)
    print("Image was written")
    return data

if __name__ == '__main__':
   app.run(debug = True,
   			host = "192.168.43.175",
   			port = "5000")