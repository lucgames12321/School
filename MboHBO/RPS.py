import random

gewonnen = 0
verloren = 0
gelijkgespeeld = 0
doorspelen = True
opties = ["steen", "papier", "schaar"]

while doorspelen == True:
 g_keuze = input("Type steen/papier/schaar of Q om te stoppen: ")

 if g_keuze.lower() == "q":
    doorspelen = False
 else:
    random_nummer = random.randint(0, 2)
    c_keuze = opties[random_nummer]
    print("de computer kiest", c_keuze)

 if g_keuze == "steen" and c_keuze == "schaar":
    print("Je hebt gewonnen!")
    gewonnen += 1

 elif g_keuze == "papier" and c_keuze == "steen":
    print("Je hebt gewonnen!")
    gewonnen += 1

 elif g_keuze == "schaar" and c_keuze == "papier":
    print("Je hebt gewonnen!")
    gewonnen += 1

 elif c_keuze == g_keuze:
    print("gelijkspel!")
    gelijkgespeeld += 1
    
 else:
    print("je hebt verloren!")
    verloren += 1
    print("Je hebt", gewonnen, "keer gewonnen!")
    print("Je hebt", verloren, "keer verloren!")
    print("Je hebt", gelijkgespeeld, "keer gelijk gespeeld!")
print("Het spel is gestopt, vaarwel!")