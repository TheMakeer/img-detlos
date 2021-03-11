from flask import Flask
from flask import request
from multiprocessing import Value
import numpy as np
import cv2
import os

app = Flask(__name__)

app.secret_key = 'sdfhj43uop23opjuhjg234jghds8'
app.jinja_env.globals.update(zip=zip)

counter = Value('i', 0)

def save_img(img):
	with counter.get_lock():
		counter.value += 1
		count = counter.value
	img_dir = "esp32_imgs"
	if not os.path.isdir(img_dir):
		os.mkdir(img_dir)
	cv2.imwrite(os.path.join(img_dir,"img_"+str(count)+".jpg"), img)
	print("Image Saved", end="\n")

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
	return "ESP32-CAM Flask Server", 200

@app.route('/upload', methods=['POST','GET'])
def upload():
	received = request
	img = None
	if received.files:
		print('incoming file')
		print('--------------')
		print('--------------')
		print(str(received.files))
		print('--------------') 
		print('--------------')		
		print(received.files['imageFile'])
		['imageFile']

		# convert string of image data to uint8
		file  = received.files['imageFile']
		['imageFile']
		nparr = np.fromstring(file.read(), np.uint8)
		# decode image
		img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
		print(str(img))
		""" save_img(img) """
		return "[SUCCESS] Image Received", 201
	else:
		return "[FAILED] Image Not Received", 204

if __name__ == "__main__":
  app.run()