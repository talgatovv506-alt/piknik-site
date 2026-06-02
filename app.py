from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rakmet')
def rakmet():
    return render_template('rakmet.html')

if __name__ == '__main__':
    app.run(debug=True)