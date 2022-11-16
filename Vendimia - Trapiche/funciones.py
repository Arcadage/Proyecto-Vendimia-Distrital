import json
from openpyxl import Workbook

def aExcel(): 
    coso = leer_json()
    wb = Workbook()
    ws = wb.active
    ws.append(["Distrito","Nombre","Votos"])
    for i in coso.values():
        l = []
        l.append(i["Distrito"])
        l.append(i["Nombre"])
        l.append(i["Votos"])
        ws.append(l)
    wb.save("data.xlsx")

def escribir_json(leer):
 with open('candi.json','w') as r:
   json.dump(leer, r, indent = 4)

def leer_json():
  with open('candi.json','r') as r:
    leer = json.load(r)
  return leer
    
def SumarVotos(voto):
    candi = leer_json()    
    candi[voto]['Votos'] += 1
    OrdenarJson(candi)
    
def OrdenarJson(leer):
  dicAux = {}
  lista = []
  ids = []                            #Lista para identificar los ids que ya han sido agregados al JSON
  for i in leer.values():             #Lee los votos de cada candidata y los mete en una lista
    lista.append(i["Votos"])
  lista = sorted(lista, reverse=True) #Ordena la lista de mayor a menor
  
  for i in lista: 
    for j in leer.values():
      if j["ID"] in ids:
        continue
      if j["Votos"] == i:             #Compara en orden los elementos de la lista
        ids.append(j["ID"])           #Agrega el id de las candidatas a la lista de id en orden
        dicAux[j["ID"]] = j           #Agrega al diccionario auxiliar las candidatas en orden
        break
  escribir_json(dicAux)