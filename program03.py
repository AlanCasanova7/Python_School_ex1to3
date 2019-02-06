'''
Definire una funzione es3(lista, testo) che prende:
- una lista di parole (nessuna delle quali e' prefisso dell'altra)
- una stringa di testo. Il testo e' stato ottenuto concatenando alcune delle parole presenti nella lista 'lista'
  (una stessa parola puo' comparire piu' volte nella stringa di testo).
- restituisce una coppia (tupla) formata da:
        - la lista delle parole che, concatenate producono il testo
        - la parola che vi occorre piu' spesso
  (se questa parola non e' unica allora viene restituita quella che precede le altre lessicograficamente).
  Nella lista di output ogni parola appare una sola volta e le parole
  risultano ordinate in base alla loro prima apparizione nella concatenazione che produce il testo
  (i.e. quella che compare per prima al primo posto ecc.ecc.)
  Infine al termine della funzione la lista 'lista' deve risultare modificata come segue:
  in essa saranno state cancellate tutte le parole utilizzate in testo, e tornate come risultato.
  Ad esempio: se lista=['gatto','cane','topo']
  - con  testo='topogattotopotopogattogatto' la risposta e' la coppia (['topo','gatto'],'gatto')
    e lista diviene ['cane']
  se lista=['ala','cena','elica','nave','luce','lana','vela']
  - con testo='lucenavelanavelanaveelica' la risposta e' (['luce','nave','lana','vela','elica'],'nave')
  e ls diviene ['ala','cena']

NOTA: il timeout previsto per questo esercizio è di 5 secondi per ciascun test

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
'''


def es3BAD(lista, testo):
  testo_copy = testo

  most_seen_word = ''
  max_occurency = 0

  used_words = list(lista).copy()

  for word in lista[::-1]:
    occurency = 0
    while testo_copy.find(word) != -1:
      occurency += 1
      testo_copy = testo_copy.replace(word, '', 1)
    if occurency == 0:
      used_words.remove(word)
    elif occurency > 0:
      lista.remove(word)
    if occurency > max_occurency:
      max_occurency = occurency
      most_seen_word = word
    elif occurency == max_occurency and word < most_seen_word:
      most_seen_word = word

  sorted(used_words, reverse = False)

  to_return = (used_words, most_seen_word)
  return to_return


def es3(word_list, text):
  copy_text = text
  used_words = []
  most_used_word = ''
  highest_occurency = 0
  
  while len(copy_text) > 0:
    print(len(copy_text))
    max_range = 0
    while copy_text[0:max_range] not in word_list:
      max_range += 1
      if max_range > len(copy_text):
        return -1
    current_word = copy_text[0:max_range]
    word_list.remove(current_word)
    used_words.append(current_word)
    occurency = 0
    while copy_text.find(current_word) != -1:
      occurency += 1
      copy_text = copy_text.replace(current_word, '', 1)
    if occurency > highest_occurency:
      most_used_word = current_word
      highest_occurency = occurency
    elif occurency == highest_occurency and most_used_word > current_word:
      most_used_word = current_word

  to_return = (used_words, most_used_word)
  return to_return