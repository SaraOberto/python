#1 Popola
import pprint
pp=pprint.PrettyPrinter(indent=4)
diz={"Giuseppe Gullo": [("Corsa campestre",(40,21,0), "Allievi"),("Corsa 100mt",(0,12,0), "Juniores mas"),("Corsa 200mt",(0,29,19), "Juniores mas")],
     "Antonia Barbera": [("Corsa campestre",(0,39,11), "Juniores fem"),("Corsa 100mt",(0,18,0), "Juniores fem"),("Corsa 200mt",(0,0,0), "Juniores fem")],
     "Nicola Esposito": [("Corsa campestre",(0,43,22), "Allievi"),("Corsa 100mt",(0,14,0),"Juniores mas"),("Corsa 200mt",(0,36,19), "Juniores mas")]}

#2 Aggiungi alla struttura il tuo nominativo con valori a scelta
diz["Sara Oberto"]=[("Corsa campestre",(0,32,7),"Allievi"),("Corsa 100mt",(0,32,7),"Juniores fem"),("Corsa 200mt",(0,14,7),"Juniores fem")]

#3 Aggiungi la 4° disciplina sportiva 'corsa ad ostacoli 400 mt' per ogni atleta
#9:26 Gornati
nDisciplina=diz["Giuseppe Gullo"]
nDisciplina.append(("Corsa ad ostacoli 400mt",(0,40,34),"Allievo"))
diz["Giuseppe Gullo"]=nDisciplina

nDisciplina=diz["Antonia Barbera"]
nDisciplina.append(("Corsa ad ostacoli 400mt",(0,39,10),"Allieva"))
diz["Antonia Barbera"]=nDisciplina

nDisciplina=diz["Nicola Esposito"]
nDisciplina.append(("Corsa ad ostacoli 400mt",(0,40,10),"Allievo"))
diz["Nicola Esposito"]=nDisciplina

nDisciplina=diz["Sara Oberto"]
nDisciplina.append(("Corsa ad ostacoli 400mt",(0,40,26),"Allieva"))
diz["Sara Oberto"]=nDisciplina

#4 Stampa la tupla con le informazioni sulla disciplina sportiva corsa campestre per l'atleta Giuseppe Gullo
#9:26 Gornati
print("Informazioni sulla tupla sulla disciplina sportiva corsa campestre di Giuseppe Gullo")
print(f"{diz['Giuseppe Gullo'][0][1]}")

#5 Stampa i singoli valori della tupla con le informazioni sulla disciplina corsa 200 mt. per Nicola Esposito
#9:26 Gornati
print("Informazioni sulla tupla sulla disciplina sportiva corsa 200 mt. per Nicola Esposito")
print(f"Minuti {diz['Nicola Esposito'][2][1][0]}")
print(f"Secondi {diz['Nicola Esposito'][2][1][1]}")
print(f"Millesimi {diz['Nicola Esposito'][2][1][2]}")

#6 Stampa il tempo di Antonia Barbera nella corsa 100 mt.
#9:47 Gornati
print("Tempo di Antonia Barbera nella corsa 100 mt.")
print(f"Minuti {diz['Antonia Barbera'][1][1][0]}")
print(f"Secondi {diz['Antonia Barbera'][1][1][1]}")
print(f"Millesimi {diz['Antonia Barbera'][1][1][2]}")

#7 Stampa il tempo minimo riportato nella corsa 100mt. della categoria Juniores mas.
#9:46 Gornati
print("Tempo minimo nella corsa 100mt nella categioria Juniores mas")
minimo=diz["Giuseppe Gullo"][1][1]
for chiave in diz.keys():
  if(diz[chiave][1][2]=="Juniores mas" and diz[chiave][1][1]<minimo):
    minimo=diz[chiave][1][1]
print(f"{minimo}")

#8 Stampa il tempo massimo riportato nella corsa 200mt della categoria Juniores mas
# 9:53 Gornati
print("Tempo massimo nella corsa 200mt nella categioria Juniores mas")
massimo=diz["Giuseppe Gullo"][2][1]
for chiave in diz.keys():
    if(diz[chiave][2][2]=="Juniores mas" and diz[chiave][2][1]>massimo):
        massimo=diz[chiave][2][1]
print(f"{massimo}")

#9 Stampa la media dei tempi nella corsa campestre della categoria allievi.
# 10:21 Gornati
sMinuti=0
sSecondi=0
sMillesimi=0
mMinuti=0
mSecondi=0
mMillesimi=0
cont=0
for chiave in diz.keys():
  if(diz[chiave][0][2]=="Allievi"):
    sMinuti+=diz[chiave][0][1][0]
    sSecondi+=diz[chiave][0][1][1]
    sMillesimi+=diz[chiave][0][1][2]
    cont+=1
if(sMinuti==0):
  mMinuti==0
elif(sSecondi==0):
  mSecondi==0
elif(sMillesimi==0):
  mMillesimi==0
else:
  mMinuti=sMinuti/cont
  mSecondi=sSecondi/cont
  mMillesimi=sMillesimi/cont
print(f"La media dei tempi nella corsa campestre della categoria allievi è: ")
print(f"Minuti: {mMinuti} ")
print(f"Secondi: {mSecondi}")
print(f"Millesimi: {mMillesimi}")

#10 Realizzare le opportune funzioni per aggiungere al dizionario i dati validi relativi alle 4 gare per un atleta.
def leggiNomeValido():
  nome=""
  while len(nome)==0:
    nome=input("Inserisci nome: ")
    if(len(nome)==0):
      print("Devi inserire il nome")
  return nome

def leggiCognomeValido():
  cognome=""
  while len(cognome)==0:
    cognome=input("Inserisci cognome: ")
    if(len(cognome)==0):
      print("Devi inserire il cognome")
  return cognome

def leggiChiave():
  nome=leggiNomeValido()
  cognome=leggiCognomeValido()
  return nome+cognome

def campestreValido():
  while len(campestre1)==0 or campestre1<0:
    campestre1=int(input("Inserisci minuti: "))
    if(len(campestre1)==0 or campestre1<0):
      print("Devi inserire minuti validi")
  while len(campestre2)==0 or campestre2<0:
    campestre2=int(input("Inserisci minuti: "))
    if(len(campestre2)==0 or campestre2<0):
      print("Devi inserire minuti validi")
  while len(campestre3)==0 or campestre3<0:
    campestre3=int(input("Inserisci minuti: "))
    if(len(campestre3)==0 or campestre3<0):
      print("Devi inserire minuti validi")
  campestre=(campestre1,campestre2,campestre3)
  return campestre

def centomtValido():
  while len(cento1)==0 or cento1<0:
    cento1=int(input("Inserisci minuti: "))
    if(len(cento1)==0 or cento1<0):
      print("Devi inserire minuti validi")
  while len(cento2)==0 or cento2<0:
    cento2=int(input("Inserisci minuti: "))
    if(len(cento2)==0 or cento2<0):
      print("Devi inserire minuti validi")
  while len(cento3)==0 or cento3<0:
    cento3=int(input("Inserisci minuti: "))
    if(len(cento3)==0 or cento3<0):
      print("Devi inserire minuti validi")
  cento=(cento1,cento2,cento3)
  return cento

def duecentomtValido():
  while len(dueCento1)==0 or dueCento1<0:
    dueCento1=int(input("Inserisci minuti: "))
    if(len(dueCento1)==0 or dueCento1<0):
      print("Devi inserire minuti validi")
  while len(dueCento2)==0 or dueCento2<0:
    dueCento2=int(input("Inserisci minuti: "))
    if(len(dueCento2)==0 or dueCento2<0):
      print("Devi inserire minuti validi")
  while len(dueCento3)==0 or dueCento3<0:
    dueCento3=int(input("Inserisci minuti: "))
    if(len(dueCento3)==0 or dueCento3<0):
      print("Devi inserire minuti validi")
  dueCento=(dueCento1,dueCento2,dueCento3)
  return dueCento

def ostacoliValido():
  while len(ostacoli1)==0 or ostacoli1<0:
    ostacoli1=int(input("Inserisci minuti: "))
    if(len(ostacoli1)==0 or ostacoli1<0):
      print("Devi inserire minuti validi")
  while len(ostacoli2)==0 or ostacoli2<0:
    ostacoli2=int(input("Inserisci minuti: "))
    if(len(ostacoli2)==0 or ostacoli2<0):
      print("Devi inserire minuti validi")
  while len(ostacoli3)==0 or ostacoli3<0:
    ostacoli3=int(input("Inserisci minuti: "))
    if(len(ostacoli3)==0 or ostacoli3<0):
      print("Devi inserire minuti validi")
  ostacoli=(ostacoli1,ostacoli2,ostacoli3)
  return ostacoli

def leggiDatiValidi():
  campestre=campestreValido()
  cento=centomtValido()
  duecento=duecentomtValido()
  ostacoli=ostacoliValido()
  return [("Corsa campestre",(campestre)),("Corsa 100mt",(cento)),("Corsa 200mt",(duecento)),("Ostacoli",(ostacoli))]

while True:
  chiave=leggiChiave()
  if chiave in diz:
    print("Persona già esistente")
  else:
    break
dati=leggiDatiValidi()  
diz[chiave]=dati
print(diz)
