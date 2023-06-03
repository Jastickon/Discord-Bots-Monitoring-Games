import requests
ip = "es.gta5grand.com:22005"

def getPlayers(ip:str) -> tuple:
    """

    :param ip: "es.gta5grand.com:22005" or "8.8.8.8:8080"
    :return: (cur_player | max | peak)
    """
    s = requests.get("https://cdn.rage.mp/master")
    data = s.content
    conData = eval(data)
    for i in conData:
        if i == ip:
            data =conData[i]
            return data['players'],data['maxplayers'],data['peak']
getPlayers(ip)