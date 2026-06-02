from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Сәлеметсіз бе! Бұл менің Flask сайтым 🚀'

if __name__ == '__main__':
    app.run(debug=True)