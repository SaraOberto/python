#1 Popola
import pprint
pp=pprint.PrettyPrinter(indent=4)
diz={"AA123BB": [("Giugno",9,1293),("Luglio",7,3231),("Agosto",7,4020),("Settembre",6,3928)],
     "AB345CD": [("Giugno",8,1391),("Luglio",6,1234),("Agosto",9,4932),("Settembre",8,2872)],
     "CD456FF": [("Giugno",7,2872),("Luglio",6,3273),("Agosto",4,3211),("Settembre",8,2827)]}
     
#2 Aggiungi
diz["ZZ999OS"]=[("Giugno",10,16000),("Luglio",10,16000),("Agosto",10,16000),("Settembre",10,16000)]

#3 Stampa tupla con tutte le informazioni su Luglio per la targa AA123BB
print("Informazioni sulla tupla di Luglio per la targa AA123BB")
print(f"Noleggi: {diz['AA123BB'][1][1]}")
print(f"Km: {diz['AA123BB'][1][2]}")

#4 Stampa solo il numero di noleggi sul mese di Luglio per la targa AA123BB
print("Numero di noleggi sul mese di Luglio per la targa AA123BB")
print(f"Noleggi: {diz['AA123BB'][1][1]}")

#5 Stampa la somma di tutti i km in tutti i mesi per la targa AB345CD
km=0
for i in range (len(diz["AB345CD"])):
  km+=diz["AB345CD"][i][2]
print(f"I km totali della targa AB345CD sono {km}")

#6 Stampa la somma di tutti i km in tutti i mesi per tutte le macchine
km=0
for chiave in diz.keys():
  for j in range(len(diz[chiave])):
    km+=diz[chiave][j][2]
print(f"I km totali di tutte le macchine in tutti i mesi sono {km}")

#7 Stampa il mese in cui sono stati fatti più km per la macchina targata CD456FF
KmM=diz["CD456FF"][0][2]
i=1
mese=""
for i in range (len(diz["CD456FF"])):
  if(diz["CD456FF"][i][2]>KmM):
    KmM=diz["CD456FF"][i][2]
    mese=diz["CD456FF"][i][0]
print(f"Il mese in cui sono stati fatti più Km nella macchina targata CD456FF é {mese} con {KmM}Km")
