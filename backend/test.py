import requests
from pprint import pprint
import numpy as np
import json

uniprotid = ['P04637']
predictors = {
    
}

residuemax = []
jsonresponse = []
for unid in uniprotid:
    URL = f"https://mobidb.org/api/download?acc={unid}&format=json"
    response = requests.get(URL)
    jsonresp = response.json()
    jsonresponse.append(jsonresp)
    # pprint(response.json())
    # open("results.json", "wb").write(response.text())
    # pprint(str(jsonresp['length']) + "<--")
    residuemax.append(list(np.arange(1,jsonresp['length']+1)))



# pprint(jsonresponse)
# for i in range(len(uniprotid)):
    # pprint(jsonresponse[i]['prediction-disorder-iupl'])
# pprint(jsonresponse['prediction-disorder-iupl'])
# pprint(jsonresponse['length'])
# print(list(np.arange(1,jsonresponse['length']+1)))
# newlist = []
# for _ in jsonresponse[0]['prediction-disorder-iupl']['regions']:
#     for i in _:
#         newlist.append(i+1)
headers = {'Protein Name': uniprotid, 'Residue Number': residuemax, 'IUPred-Long': jsonresponse[0]['prediction-disorder-iupl']['regions'], 'Sum': []}
print(headers)
# open("instagram.ico", "wb").write(response.content)