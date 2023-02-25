from PIL import Image
import requests
import json
import io
import os
import pandas as pd
from tqdm import tqdm
from token_ import RSL_TOKEN

data = pd.read_csv('_ (1).csv', delimiter=';')
ids = data['Идентификатор']
names = data['Заглавие']

base_url = 'http://10.2.0.172:8080'
count = 0

for idx, name in tqdm(zip(ids, names)):
    name = name[:50].replace('/', '')
    catalog = idx[:5].lower()
    code = idx[5:]
    req_url = base_url + f'/{catalog}/{code}/resources'
    resp = requests.get(req_url, headers={"Dlib-Client-Key":RSL_TOKEN})
    if b'txt' in resp.content:
        txt_url = base_url + f'/{catalog}/{code}/resources/txt'
        txt_resp = requests.get(txt_url, headers={"Dlib-Client-Key":RSL_TOKEN})
        with open(f'pdfs_txts/{idx}_{name}.txt', 'wb') as txt_out:
            txt_out.write(txt_resp.content)
