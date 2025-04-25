from flask import Flask, render_template, request
from serpapi import GoogleSearch
import time
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form['query']
        results = search_toolkit_links(query)
    return render_template('index.html', results=results)

import time

def search_toolkit_links(query):
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/91.0.4472.124 Safari/537.36'
        )
    }

    # Construir a URL para DuckDuckGo
    url = f"https://duckduckgo.com/html/?q={query}+components+UI+icons+libraries+site:github.com"
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao fazer requisição ao DuckDuckGo: {e}")
        return []

    # Depuração: Verificar a resposta do HTML
    print("🧪 HTML recebido:")
    print(response.text)  # Adicionando depuração aqui

    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for a in soup.find_all('a', class_='result__a'):  # Verificando se a classe é correta
        href = a.get('href')
        if href and 'github.com' in href:
            links.append(href)

    print(f"🔗 Links encontrados: {links}")

    time.sleep(1)  # Delay de 1 segundo entre as requisições para evitar bloqueios

    return links[:10]


@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = search_toolkit_links(query)
    return render_template('index.html', results=results)
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    app.run(debug=True)
