#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request

#Importing files that I used for this project 
from text import *

#Setting up Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/lincoln')
def lincon_speech():
    return render_template('lincoln.html', title='Gettysburg Address')

@app.route('/king')
def king_speech():
  return render_template('king.html', title='I Have a Dream')

@app.route('/military')
def ike_speech():
  return render_template('military.html', title='Ike Speech')

@app.route('/data')
def data_page():
  #USE NVD3
  return render_template('data.html', title='Data Page')



#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)