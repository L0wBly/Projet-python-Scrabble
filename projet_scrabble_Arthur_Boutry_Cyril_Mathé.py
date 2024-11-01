import random
"""
Cyril Mathé
Arthur Boutry
"""
easy = ["soleil","wifi", "page","livre","lune","plage"]
medium = ["toran","kayak","bizarre","insolite","subtil"]
hard = ["parapluie","television","labyrinthe","innovant","nostalgie"]

def choose_words(words_choosen,n):
  return random.sample(words_choosen, n)

def regroup_words(mot):
  return "".join(mot)

def shuffle_words(shuffle):
  return random.sample(shuffle,len(shuffle))

def supp_double1(shuffled_words):
  nw_rm1 = ""
  for caractere in shuffled_words:
    if caractere not in nw_rm1:
        nw_rm1 = nw_rm1 + caractere
  return nw_rm1

def jeu(shuffle_word,liste_mot):
  i = 0
  while i < 3:
    print("Liste de lettres disponible :",shuffle_word)
    print("Entrer un mot !")
    mot = input()
    if mot == "quit":
      print("Manche suivante")
      break
    elif mot not in liste_mot:
      print("Faux")
    elif mot in liste_mot:
      liste_mot.remove(mot)
      print("Bon")
      i += 1

def jouer():
  wordsEasy,wordsMedium,wordsHard = choose_words(easy,3),choose_words(medium,3),choose_words(hard,3)
  # Appel regroupe_words avec le résultat de choose_wors
  regrouped_easy, regrouped_medium, regrouped_hard = regroup_words(wordsEasy),regroup_words(wordsMedium),regroup_words(wordsHard)
  # Appel shuffle_words avec le résultat de regroupe_words
  shuffled_easy, shuffled_medium, shuffled_hard = shuffle_words(regrouped_easy),shuffle_words(regrouped_medium),shuffle_words(regrouped_hard)
  # Appel supp_double avec le résultat de shuffle_words
  shuffle_words_easy,shuffle_words_medium,shuffle_words_hard = supp_double1(shuffled_easy),supp_double1(shuffled_medium),supp_double1(shuffled_hard)
  print("Bienvenu dans le jeu du scrabble !")
  p = 0
  j = len(wordsEasy) + len (wordsMedium) + len(wordsHard)
  print("Manche 1")
  jeu(shuffle_words_easy,wordsEasy)
  print("Manche 2")
  jeu(shuffle_words_medium,wordsMedium)
  print("Manche 3")
  jeu(shuffle_words_hard,wordsHard)
  p += 3-len(wordsEasy) + 3-len(wordsMedium) + 3-len(wordsHard)
  print(f"Bien joué tu {p} as point sur {j}")


jouer()