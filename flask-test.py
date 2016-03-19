import Adafruit_BBIO.GPIO as GPIO

import time


GPIO.setup("P8_11", GPIO.OUT)


from flask import Flask
from flask import render_template

from flask import request

from jinja2 import Environment, PackageLoader


app =Flask(__name__)

 
env = Environment(loader=PackageLoader('flask-test', 'templates'))

global status

status = "none"

@app.route("/", methods = ['GET', 'POST'])
def main():
	global status

	if request.method == 'GET':

		template = env.get_template('click.html')

		return template.render(val = "nothing")

	else:

		if request.form['led7'] == 'on':

			GPIO.output("P8_11", GPIO.HIGH)

			status = "on"

		elif request.form['led7'] == 'off':

			GPIO.output("P8_11", GPIO.LOW)

			status = "off"

		template = env.get_template('click.html')

		return template.render(val = status)
		time.sleep(5)
 

app.debug = True
if __name__ == "__main__":

	app.run(host="0.0.0.0",port=5000)
