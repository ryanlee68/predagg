from flask import Flask

app = Flask(__name__)

@app.route("/api/response", methods=['POST'])
def get_repsonse():
    if request.method == 'POST':
        response = request.json
        print(response)
        return response