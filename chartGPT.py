#Variabili e Tipi di dati
"""
in python variabili e' come un contenitore che poui memerizare dei dati che ti seriverano piu avanti
"""

#esampio 
tensione = 230 #tensione di un circuito
nome_cliente = 'Mario Rossi' # nome di cliente
temperatura_cavo = 35.14 # temperatura di un cavo eletrico in grande calsius

#tipi di dati base
 # *interi 230
 # *virgola mobili 35.14 (float)
 # * stringhi 'mario rossi'

 #Stampare l'output: per visualizzare un variabili poui usare la funzione print()

print('tensione:', tensione)
print('nome_cliete: ', nome_cliente)
print('temperatura_cavo: ', temperatura_cavo)

#Esercizio
# 1.Prova a definire una variabile chiamata tipo_cavo con il tipo di cavo che usi di solito e stampala a schermo.
tipo_cavo = '2,5 neuatro'
cavo_fase = 'fase'
cavo_tera = 'terra'
print(tipo_cavo, cavo_fase, cavo_tera)

#Definisci una variabile per la tensione massima di un impianto e stampala. 
tensione_massima = 400
print('tensione massima: ', tensione_massima)

#Operazioni matematiche
"""
come eletricista potresti dover fare calcoli su resistenza, potenza o curente. in python, poui usare le operazioni matematiche di base
"""

#esampio: 
#Somma, sottrazioni, multiplicazione, divisione, esponete

resistenza = 10 # in ohm
corrente = 2  # in ampere

#calcoliamo la tensione usando la formula v = r * i
tensione = resistenza * corrente
print('tensione: ', tensione)  # Questo stamperà: 20

# Condizioni if statements
# le condizioni ci permettono a controllare i valori e di esegiuire operazioni a secondo dei resultati

tensione = 220

if tensione > 230:
    print('Attenzione, la tensione è tropo alta. ')
elif tensione < 210:
    print('la tensione è tropo basa.')
else:
    print('la tensione é sicura.')
    
# if controlla la prima condizione se la  tensioni > 230
# elif controlla un'altra condizioni se la prima è falsa tensioni  < 210
#else invece viene esegiuta se tutti le condizione precedente sono false

#Definisci due variabili, potenza e corrente. Calcola la resistenza 
potenza = 210
corrente = 10
resistenza = potenza / (corrente ** 2)
print('resistenza: ', resistenza)

# Scrivi una condizione per controllare se la resistenza è superiore a 100 ohm. Se è superiore, stampa un messaggio di avviso; altrimenti, stampa che la resistenza è entro i limiti.

if resistenza > 100:
    print('la resistenza è superiore.')
elif resistenza < 10:
    print('la resistenza è tropo basa')
else:
    print('la resistenza è entro i limiti.')


#Cicli loops 
# in python ci sono due tipi pricipale di cicli 
#FOR e WHILE LOOP

"""
#Ciclo for: il ciclo for è utile quando sai quante volte devi repetere un'operazione.
ad esampio se voui controllare una lista di tenzioni di diversi impiati poui usare ciclo for
"""
lista_tensioni = [220, 230, 240,250]
for tensione in lista_tensioni:
    print(f'Tensioni {tensione}v: Attenzione è tropo alta.')
else:
    print(f'Tensione {tensione}v: sicura')

"""
La variabile tensione prende il valore di ogni elemento nella lista tensioni e verifica se è sicura.
f"Testo {variabile}" è un modo per creare una stringa che inserisce il valore di una variabile nel testo.
"""

#Ciclo while 
"""
il ciclo while repete un blocco di codice finche una condizioni remana vera.
"""
#esampio 
corrente = 5 #corrente iniziale
while corrente < 10:
  print(f'Corrente {corrente}A: aumenta corrente')
  corrente += 1  # Incrementa la corrente di 1 per simulare un aument. corrente = corrente + 1
"""
il ciclo continua finché corrente è minore di 10.
corrente += 1 è un’operazione che aumenta il valore di corrente di 1 a ogni ciclo.
"""

#Esercizio
#Crea una lista chiamata resistenze con alcuni valori (ad esempio: [5, 50, 150, 300]).
lista_resistenze = [5,50,150,300]

#Usa un ciclo for per controllare ogni valore di resistenza. Se è maggiore di 100, stampa un messaggio di avviso; altrimenti, stampa che la resistenza è entro i limiti.
for resistenza in lista_resistenze:
   if resistenza > 100:
      print(f'Resistenza {resistenza} ohm: resistenza è tropo alta')
   else:
    print(f'Resistenza {resistenza} ohm: resistenza è entro i limiti.')
#Usa un ciclo while per aumentare una variabile temperatura da 20 fino a 30. Stampa la temperatura a ogni passo.
temperatura = 20 # valori iniziale
while temperatura <= 30:
    print(f"Temperatura {temperatura}° Celsius.")
    temperatura += 1 #Incrementa la temperatura di 1 per simulare un aument

#Funzioni: in python funzioni è un blocco di codice che puo seguire una operazione specifica e puo essere re utilizato facilmente.
def calcola_resistenza(potenza, corrente):
    # Calcola la resistenza usando la formula R = P / I^2
    resistenza = potenza / (corrente ** 2)
    return resistenza
print('resistenza: ', resistenza)

"""
 def indica che stiamo definendo una funzione.
calcola_resistenza è il nome della funzione, seguito da due parametri (potenza e corrente) tra parentesi.
return restituisce il risultato, in modo che possiamo usare il valore della resistenza calcolata al di fuori della funzione
"""
# Usare una Funzione
# Una volta definita, puoi richiamare la funzione usando il suo nome e passando i parametri necessari.
risultato = calcola_resistenza(210, 10)
print(f"Resistenza calcolata: {risultato} ohm")

#Esercizio

#Definisci una funzione chiamata verifica_tensione che prende un parametro tensione e:
#Stampa "Attenzione! Tensione troppo alta." se la tensione è superiore a 230.
#Stampa "Tensione sicura." altrimenti.

def verifica_tensione(tensione):
    if tensione > 230:
        print(f'Attenzioni {tensione}V troppo alta.')
    else:
        print(f'{tensione}V Tensione sicura.')

#Chiama la funzione verifica_tensione con diversi valori di tensione (ad esempio, 220, 240, 230) per verificare che funzioni correttamente.
verifica_tensione(220)
verifica_tensione(240)
verifica_tensione(230)

#Esercizio
#Crea una lista di almeno 5 valori di tensione con valori sia sopra che sotto i 230V.
lista_tensioni2 = [220, 240, 230, 250, 400]
#Passa la lista alla funzione verifica_tensioni e controlla i risultati.
def verifica_tensione(lista_tensioni):
    for tensione in lista_tensioni:
        if tensione > 230:
            print(f'Attenzione {tensione}V troppo alta.')
        else:
            print(f'Tensioni {tensione}V è normale.')
verifica_tensione(lista_tensioni2)

# Dizionari: un dictionario in python è una racounta di elementi ciascuno è composta da una chiave e un valori.

#esempio: 
circuiti = {
    "linea_1_circuiti_1": 210,
    "linea_2_circuiti_2": 220,
    "linea_3_circuiti_3": 230,
    "linea_4_circuiti_4": 240,
    "linea_5_circuiti_5": 250
}

#linea1_circuiti_1 è la chiave e 210 sono i valori associati

# Accedere ai Valori
#Puoi accedere al valore di una chiave specifica usando la sintassi dizionario[chiave].
tension_cercuiti = circuiti["linea_1_circuiti_1"]
print(f'Tensione del cercuito linea 1: ', tension_cercuiti)

#Ciclo su un Dizionario
