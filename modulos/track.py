import os, requests, json

os.system('clear')
os.system(' figlet geoiP ')
print("\n")
def geonovo():

  ip = input("\033[92mDigite Ip Alvo\033[0m : ")

  req = requests.post("https://ipinfo.io/",{"ip":f"{ip}"})

  resposta = req.json()

  data = []

  for x in resposta:

   data.append(f"{x} : {resposta[x]}")

  print("\n".join(data))

  print ("\n")
  os.system('exit')

geonovo()
