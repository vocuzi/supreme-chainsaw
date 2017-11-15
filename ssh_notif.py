import requests, sys, json
conn = sys.argv[1]
location = requests.get("https://tools.keycdn.com/geo.json?host="+str(conn)).text
location = json.loads(location)
name = sys.argv[2]
date = sys.argv[3]
payload = """
SSH LOGIN ALERT
src:%s,
host:%s,
date:%s,
isp:%s,
location:%s,
"""%(conn,name,date,location['data']['geo']['isp'],location['data']['geo']['city']+' '+location['data']['geo']['country_name'])
url="https://api.telegram.org/bot_pi_key_here/sendMessage?chat_id=chat_id_here&text="+payload
r = requests.get(url)
