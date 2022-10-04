import requests
from pprint import pprint
import numpy as np
import json
import pandas as pd

uniprotid = 'P04637'
predictors = {
    
}

URL = f"https://mobidb.org/api/download?acc={uniprotid}&format=json"
response = requests.get(URL)
jsonresp = response.json()
# print(jsonresp)
with open("myfile.txt", "w") as f:
    f.write(json.dumps(jsonresp))

proteinname = jsonresp['name']
print(proteinname)
sequence = jsonresp['sequence']
print(sequence)
length = jsonresp['length']
print(length)

headers = {"Protein Name": [proteinname],
    "UniProtID": [uniprotid],
    "Sequence": [sequence],
    "Length": length,
    }

df = pd.DataFrame(data=headers)
df2 = df.reindex(df.columns.tolist() + list(predictors.keys()),index=1)
print(df)

# open("instagram.ico", "wb").write(response.content)