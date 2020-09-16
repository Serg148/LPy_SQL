from flask import Flask
from utils import creating_request,exec_query


app = Flask(__name__)

@app.route('/')
def hello_world():
    return'Hello, World!'

@app.route('/names/')
def unique_names():
    query = 'SELECT count(distinct(FirstName)) FROM customers;'
    return str(exec_query(query)[0][0])

@app.route('/tracks/')
def tracks():
    query = 'SELECT count(Trackid) FROM tracks;'
    return str(exec_query(query)[0][0])

@app.route('/tracks-sec/')
def tracks_sec():
    query ='SELECT Name, Milliseconds/1000 FROM tracks;'
    return str(exec_query(query))


@app.route('/customers/')
def sorting_data():
    query = creating_request()
    return str(exec_query(query))

if __name__ == "__main__":
    app.run()
