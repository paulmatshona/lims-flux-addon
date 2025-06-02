from flask import Flask, render_template, request, redirect, url_for
from model.ml import data as ml_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        # Handle form submission
        data = request.form['data']
        data = int(data) if data.isdigit() else data
        if type(data) == int:
            data+=10
        else:
            data = "Insert a number"
       
        # Process the data as needed
        #Machine learning operations here
        return render_template('data.html', data=data)
    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)
# This code sets up a simple Flask application with two routes: the index route and the data route.