from urllib.request import Request, urlopen
import requests
ip = urlopen(Request("https://bit.ly/2PTxfFq")).read().decode().strip()
data = (f'IP: {ip}')
arch=open('MyIP.txt', 'a')
arch.write(data)

