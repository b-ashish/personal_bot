from flask import Flask, render_template, request
import pandas as pd
import subprocess
import threading

app = Flask(__name__)

def rasa_server ():
    try:
        command = 'rasa run --cors "*" '
        result = subprocess.run(command, shell=True)

        if result.returncode==0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stdout.strip()}"
    except Exception as e:
        return f"Error: {e}"
def start_flask_app():
    app.run(host='0.0.0.0')

def action_server():
    command = 'rasa run actions'
    result = subprocess.run(command, shell=True)
    
@app.route("/",methods = ['get','POST'])
def home():
    return  render_template("index.html")

if __name__== "__main__":
    threading.Thread(target=action_server).start()
    threading.Thread(target=rasa_server).start()
    start_flask_app()