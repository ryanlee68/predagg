import requests
from pprint import pprint
import numpy as np

uniprotid = ['P04637']
predictors = {
    
}

residuemax = []
for unid in uniprotid:
    URL = f"https://mobidb.org/api/download?acc={uniprotid}&format=json"
    response = requests.get(URL)
    jsonresponse = response.json()
    residuemax.append(ist(np.arange(1,jsonresponse['length']+1)))


# pprint(jsonresponse)
pprint(jsonresponse['prediction-disorder-iupl'])
pprint(jsonresponse['length'])
# print(list(np.arange(1,jsonresponse['length']+1)))
headers = {'Protein Name': uniprotid, 'Residue Number': residuemax, 'Sum': []}
# open("instagram.ico", "wb").write(response.content)