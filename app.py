from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session

from database import *
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY']="string"

ON_COMPUTER = True

FULL_PATH = "/Users/omardahleh/Desktop/y2l-individual-project"
UPLOAD_FOLDER = "/static/saved_images"


@app.route('/', methods=['GET'])
def home():
	return render_template('home.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
	if request.method== 'GET':
		return render_template('upload.html')
	else:
		name=request.form['name']
		op=request.form['op']

		print(request.files)

		image_file=request.files['file']

		image_name = image_file.filename

		description=request.form['description']
		location=request.form['location']
		timeuploaded=datetime.utcnow()

		add_content(name,op,image_name,description,location, timeuploaded)

		img_id = get_content_id(timeuploaded)

		actual_filename = UPLOAD_FOLDER + "/image_" + str(img_id) + "." + image_name.split(".")[-1]

		if ON_COMPUTER:
			unique_filename = FULL_PATH + actual_filename
		else:
			unique_filename = actual_filename

		touch(unique_filename)
		image_file.save(unique_filename)

		change_content_image(img_id, img_url=actual_filename)


		return redirect(url_for('home'))

@app.route('/portfolio', methods=['GET'])
def portfolio():
	photos=query_by_photos()
	photos.reverse()
	if len(photos) > 9:
		photos = photos[0:8]
	return render_template('portfolio.html', photos=photos)


if __name__ == '__main__':
	app.run(debug=True)

