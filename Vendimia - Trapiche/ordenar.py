import operator
import json

leer = {}

def leer_json():
  global leer
  with open('vote.json','r') as r:
    leer = json.load(r)

leer_json()

lista = sorted(leer.items(), key=operator.itemgetter(1))

#glolista = []

lst = list(map(list,lista))

print(lst)

