import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to Docker MMCOMS!"

@app.route('/howareyou')
def hello():
    return 'I am good, how about you? Vladi'

if __name__ == "__main__":
    app.run()
