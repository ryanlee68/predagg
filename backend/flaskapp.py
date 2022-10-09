from webbrowser import get
from flask import Flask, request
from parser import uniprotid
from getdf import get_df

app = Flask(__name__)

@app.route("/api/response", methods=['POST'])
def get_reponse():
    if request.method == 'POST':
        response = request.json
        df = get_df(uniprotid(response), response['sequences'])
        # print(df)
        # return response
        return {'success': True}, 200