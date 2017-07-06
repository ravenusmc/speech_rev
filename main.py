#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request

#Setting up Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Graph Page')



#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)