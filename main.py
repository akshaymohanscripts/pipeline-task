from app import app
from flask import Flask, send_file, render_template
import requests
import pandas as pd
import os

	
@app.route('/')
def upload_form():
	return render_template('download.html')

@app.route('/download')
def download_file():
    
    url = "https://reqres.in/api/users"
    response = requests.request("GET", url).json()
    
    df = pd.DataFrame(response['data'])
    df= df.to_csv('response_python.csv') 
    return send_file('response_python.csv', as_attachment=True)

if __name__ == "__main__":
    app.run()