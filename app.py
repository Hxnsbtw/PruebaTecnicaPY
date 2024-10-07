from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Ruta de la página principal
@app.route('/')
def index():
    url = 'https://api.coinlore.net/api/tickers/'
    response = requests.get(url)
    data = response.json()
    
    # Se extraen los datos
    coins = [
        {
            'id': coin['id'],
            'symbol': coin['symbol'],
            'name': coin['name'],
            'price_usd': coin['price_usd'],
            'percent_change_24h': coin['percent_change_24h']
        } for coin in data['data']
    ]
    
    return render_template('index.html', coins=coins)

# Ruta para detalles de una moneda específica
@app.route('/coin/<coin_id>')
def coin_detail(coin_id):
    url = f'https://api.coinlore.net/api/ticker/?id={coin_id}'
    response = requests.get(url)
    data = response.json()

    coin = data[0] 
    return render_template('detail.html', coin=coin)

if __name__ == '__main__':
    app.run(debug=True)
