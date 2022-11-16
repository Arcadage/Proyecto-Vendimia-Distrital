import json
#Crea o reinicia el JSON
votos = {"1":{
            "ID":"1",
            "Dpto":"Godoy Cruz",
            "Votos":0,
            "Nombre":"Geraldina Otubello",
            "Distrito":"Trapiche",
            "Edad":27,
            "Estudios":"Docente de nivel primario",
            "Imagen":"imagenes/GeraldinaOtubello.jpg",
            "Imagen2":'imagenes/Geraldina.jpg'
        },
        "2":{
            "ID":"2",
            "Dpto":"Godoy Cruz",
            "Votos":0,
            "Nombre":"Catalina Puiggerver",
            "Distrito":"Trapiche",
            "Edad":18,
            "Estudios":"Estudiante de Abogacía",
            "Imagen":"imagenes/CatalinaPuiggerver.jpg",
            "Imagen2":'imagenes/Catalina.jpg'
        },
        "3":{
            "ID":"3",
            "Dpto":"Godoy Cruz",
            "Votos":0,
            "Nombre":"Katherina Zavaleta",
            "Distrito":"Trapiche",
            "Edad":20,
            "Estudios":"Estudiante de Licenciatura en Ciencia Política y Administración Pública",
            "Imagen":"imagenes/KatherinaZavaleta.jpg",
            "Imagen2":'imagenes/Katherina.jpg'
        }
    }

with open("candi.json","w") as f:
    json.dump(votos, f, indent=4)

