from webbrowser import get
from flask import Flask, request
from parser import identifier
from getdf import get_df

app = Flask(__name__)

@app.route("/api/response", methods=['POST'])
def get_reponse():
    if request.method == 'POST':
        response = request.json
        # print(response['uniprotid'])
        # print(response['sequence'])
        if response['uniprotid'] != "":
            print('there is a uniprotid')
            df = get_df(response['sequences'], uniprotid=response['uniprotid'])
            print(df)
        elif response['sequence'] != "":
            print('there is a sequence')
            print(response['sequence'])
            df = get_df(response['sequences'], sequence=response['sequence'])
            print(df)
        else:
            return {'success': False}, 500
        # df = get_df(response['sequences'], )
        # print(df)
        # return response
        # return {'success': True}, 200