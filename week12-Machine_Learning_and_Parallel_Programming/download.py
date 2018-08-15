import json
import os
from pathlib import Path
from urllib.request import urlopen, Request
from time import time

def get_links(client_id):
   headers = {'Authorization': 'Client-ID {}'.format(client_id)}
   all_ims = []
   for page in ["1", "2", "3", "4", "5", "6"]:
       req = Request('https://api.imgur.com/3/gallery/hot/viral/month', headers=headers, method='GET')
       with urlopen(req) as resp:
           data = json.loads("\n".join([i.decode('utf-8') for i in resp.readlines()]))
       all_ims = all_ims+[i['link'] for i in data['data']]
   return all_ims


def download_link(directory, link):
   download_path = directory / os.path.basename(link)
   with urlopen(link) as image, download_path.open('wb') as f:
       for line in image.readlines():
            f.write(line)

        
def setup_download_dir():
   download_dir = Path('images')
   if not download_dir.exists():
       download_dir.mkdir()
   return download_dir
   

