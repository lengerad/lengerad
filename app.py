from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/analog')
def analog():
    return render_template('analog.html')

@app.route('/analog/tokyo')
def analog_tokyo():
    return render_template('tokyo.html')

@app.route('/analog/osaka')
def analog_osaka():
    return render_template('osaka.html')

@app.errorhandler(404) 
def not_found(e): 
    return render_template("not_found.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
