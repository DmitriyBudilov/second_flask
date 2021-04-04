from flask import Flask, render_template, url_for, redirect
import random
from data import tours, departures

app = Flask(__name__)

@app.route('/')
def index():
    list_of_tours = [ {key: value} for key, value in tours.items() ]
    return render_template('index.html', list_of_tours=list_of_tours) 

@app.route('/departures/<departure>/')
def index_page(departure):
    return render_template('departure.html', tours=tours, departure=departure)

@app.route('/tours/<id>/')
def tour(id):
    return render_template('tour.html', tours=tours[int(id)], departures=departures)

@app.errorhandler(404)
def http_404_handler(error):
    return "<h1>404 страница не найдена</h1>", 404

@app.errorhandler(500)
def http_500_handler(error):
    return "<h1>500 ведутся работы</h1>", 500

if __name__ == '__main__':
    app.run()