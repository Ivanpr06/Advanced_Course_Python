import os

## txt file

# r = leer
# w = escribir
# w+ = leer y escribir

txt = open("file.txt", "w+")
txt.write("Mi nombre es Paco\nTengo 55 anyos\nSoy Espanyol\nMe gusta el Furgol")

def read():
  print(txt.read())
  print(txt.read(10))

def readline():
  print(txt.readline())
  print(txt.readline())
  print(txt.readline(4))
  for line in txt.readlines():
   print(line)


def write():
  txt.write("\nMe gusta come")
  print(txt.readline())

  txt.close()
  #os.remove("file.txt")

## Json file
def json():
    import json

    json_file = open("file.json", "w+")

    json_log = {
     "nombre": "Paco",
     "apellido": "Fernandez",
     "edad": 55,
     "me gusta": "el Furgol",
    }

    json.dump(json_log, json_file, indent=0)

    json_file.close()

    with open("file.json") as json_file:
        for line in json_file:
            print(line)

    json_dict2 = json.load(open("file.json"))
    print(json_dict2)
    print(type(json_dict2))


