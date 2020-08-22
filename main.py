import requests, json

BaseUrl = "https://api.fckveza.com/genprim?auth=uac4fdee83ecfb6f0317c97151df9446a:InVUu83UqxmTpuqJwWHS&apikey=68a5sdf67"
Apikey = "Chat me https://line.me/ti/p/~veza1007"

def genprim(authkey):
    params = {
      "apikey": Apikey, 
      "auth": authkey
    }
    data = requests.get(BaseUrl+"/genprim", params=params).json()
    return data
#example generate primery token
print(genprim("uac4fdee83ecfb6f0317c97151df9446a:InVUu83UqxmTpuqJwWHS"))

