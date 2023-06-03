import requests

#[1.1]","gamemode":"roleplay","url":"https://blrevived.de","lang":"ge","players":1,"peak":1,"maxplayers":300},"es.gta5grand.com:22005":{"name":"рџ›‘[ES][voice] [roleplay] Grand RolePlay | discord.gg/gta5grandcom

ip = "es.gta5grand.com:22005"

def getPlayers(ip):
    s = requests.get("https://cdn.rage.mp/master")
    data = master.loads(s.content)
    for i in data:
        if i["ip"] == ip:
            print(i)
            return i["players"],i["maxplayers"]