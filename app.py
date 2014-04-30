from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/authorise')
def authorise():
	return render_template('authorise.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8006, debug=True)    