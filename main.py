#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request

#Setting up Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/lincoln')
def lincon_speech():
    return render_template('lincoln.html', title='Gettysburg Address')



#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)