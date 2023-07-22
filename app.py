from flask import Flask, jsonify
import requests
import threading
import time

app = Flask(__name__)
apiUrl = 'https://api.tzevaadom.co.il/alerts-history/'
jsonData = None

def updateData():
    global jsonData
    while True:
        try:
            response = requests.get(apiUrl)
            jsonData = response.status_code
            if (response.status_code == 200):
                jsonData = response.json()
        except Exception as e:
            jsonData = e
            print(f'Error: {e}')
        time.sleep(10)

@app.route('/')
def home():
    return jsonify(jsonData)

if __name__ == '__main__':
    updateThread = threading.Thread(target=updateData)
    updateThread.start()
    app.run(port=3000)
