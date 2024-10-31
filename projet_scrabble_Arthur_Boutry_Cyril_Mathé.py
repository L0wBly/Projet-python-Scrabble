import random
"""
Cyril Mathé
Arthur Boutry
"""
easy = ["soleil","wifi", "page","livre","lune","plage"]
medium = ["toran","kayak","bizarre","insolite","subtil"]
hard = ["parapluie","television","labyrinthe","innovant","nostalgie"]

def choose_words(n):
  words_choosen_easy = random.sample(easy, n)
  words_choosen_medium = random.sample(medium, n)
  words_choosen_hard = random.sample(hard, n)
  return words_choosen_easy,words_choosen_medium,words_choosen_hard

def regroup_words(m1,m2,m3):
  rm1 = "".join(m1)
  rm2 = "".join(m2)
  rm3 = "".join(m3)
  return rm1,rm2,rm3

def shuffle_words(shuffle_rm1,shuffle_rm2,shuffle_rm3):
  l_rm1 = random.sample(shuffle_rm1,len(shuffle_rm1))
  l_rm2 = random.sample(shuffle_rm2,len(shuffle_rm2))
  l_rm3 = random.sample(shuffle_rm3,len(shuffle_rm3))
  return l_rm1,l_rm2,l_rm3

def supp_double1(shuffled_words):
  nw_rm1 = ""
  for caractere in shuffled_words:
    if caractere not in nw_rm1:
        nw_rm1 = nw_rm1 + caractere
  return nw_rm1

def jouer():
  wordsEasy,wordsMedium,wordsHard = choose_words(3)
  # Appel regroupe_words avec le résultat de choose_wors
  regrouped_easy, regrouped_medium, regrouped_hard = regroup_words(wordsEasy,wordsMedium,wordsHard)
  # Appel shuffle_words avec le résultat de regroupe_words
  shuffled_easy, shuffled_medium, shuffled_hard = shuffle_words(regrouped_easy, regrouped_medium, regrouped_hard)
  # Appel supp_double avec le résultat de shuffle_words
  shuffle_words_easy,shuffle_words_medium,shuffle_words_hard = supp_double1(shuffled_easy),supp_double1(shuffled_medium),supp_double1(shuffled_hard)
  print("Bienvenu dans le jeu du scrabble !")
  i = 0
  p = 0
  j = len(wordsEasy) + len (wordsMedium) + len(wordsHard)
  print("Manche 1")

  while i < 3:
    print("Liste de lettres disponible :",shuffle_words_easy)
    print("Entrer un mot !")
    mot = input()
    if mot == "quit":
      print("Manche suivante")
      break
    elif mot not in wordsEasy:
      print("Faux")
    elif mot in wordsEasy:
      wordsEasy.remove(mot)
      print("Bon")
      p = p + 1
      print(p,"/",j)
      i += 1

  i = 0
  print("Manche 2")
  while i < 3:
    print("Liste de lettres disponible :",shuffle_words_medium)
    print("Entrer un mot !")
    mot = input()
    if mot == "quit":
      print("Manche suivante")
      break
    elif mot not in wordsMedium:
      print("Faux")
    elif mot in wordsMedium:
      wordsMedium.remove(mot)
      print("Bon")
      p = p + 1
      print(p,"/",j)
      i += 1
  i = 0
  print("Manche 3")
  while i < 3:
    print("Liste de lettres disponible :",shuffle_words_hard)
    print("Entrer un mot !")
    mot = input()
    if mot == "quit":
      print("Résultat")
      break
    elif mot not in wordsHard:
      print("Faux")
    elif mot in wordsHard:
      wordsHard.remove(mot)
      print("Bon")
      p = p + 1
      print(p,"/",j)
      i += 1
  print("Bien joué tu as",p,"point sur",j)
jouer()