from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS extension
import subprocess

app = Flask(__name__)
CORS(app)

def run_ipynb(notebook_path,input_data):
    try:
        subprocess.run(['python', notebook_path,input_data])
    except Exception as e:
        print(f"An error occurred: {str(e)}")

@app.route('/api/processFormData', methods=['POST'])
def process_form_data():
    data = request.get_json()
    input_data = data.get('inputField')
    notebook_path = '../../SARIMAX.py'
    run_ipynb(notebook_path,input_data)
    response_data = {"result": "Data processed successfully"}
    return jsonify(response_data)

@app.route('/api/getNews',methods=['GET'])
def get_news():
    try:
        subprocess.run(['python', "../../News.py"])
        return "Script executed successfully"
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
app.run(debug=True)