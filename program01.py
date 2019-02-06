'''
Sono stati appena corretti i compiti di N studenti ed in una lista sono riportati
i voti ottenuti dai vari studenti.
Sia C il voto massimo assegnato (questo significa che i voti sono interi da 0 a C compresi).
Bisona stabilire una soglia tra 0 e C a partire dalla quale gli studenti verranno ammessi all'orale.
(ovvero vengono ammessi tutti quelli con voti maggiori o uguali alla soglia)

Non volendo essere ne' troppo severo ne' troppo generoso nella valutazione, il docente, prima di scegliere la soglia,
decide di generare per ognuna delle possibili C+1 soglie (da 0 a C compreso)
il numero di studenti che verrebbero ammessi all'orale per quella soglia.

Definire una funzione es1(voti) che, data lista non vuota 'voti' con i voti degli studenti,
restituisce la lista di C+1 interi dove in posizione i si trova  il numero di studenti ammessi
all'orale nel caso la soglia venga fissata al valore i.
ATTENZIONE: la lista ls dei voti al termine della funzione NON DEVE risultare modificata.
Ad esempio per voti=[7,5,8,3,7,2,9] la funzione es2 restituisce la lista
[7, 7, 7, 6, 5, 5, 4, 4, 2, 1]

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
'''


def es1(voti):
    voti_numericals = voti.copy()
    for i, votes in enumerate(voti_numericals):
        if votes == 'a':
            voti_numericals[i] = 10
        elif votes == 'b':
            voti_numericals[i] = 11
        elif votes == 'c':
            voti_numericals[i] = 12
    sorted(voti_numericals)

    ammissions = list(range(max(voti_numericals) + 1))
    for i in range(max(voti_numericals) + 1):
        counter = 0
        for j in voti_numericals:
            if i <= j:
                counter += 1
        ammissions[i] = counter
        
    return ammissions

random_votes = [7, 5, 8, 3, 7, 2, 9]

ammissions = es1(random_votes)
print(ammissions)
print(random_votes)
