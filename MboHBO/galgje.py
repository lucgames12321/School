# Importeer de o zo mooie random module
import random
import os

woordenlijst = ["kaas", "friet", "bier", "pizza", "sambal"]
woordkeuze = random.choice(woordenlijst)
pogingen = 5
geraden = False
geraden_letters = []

# Vraag aan de speler of hij alleen of met iemand anders wil spelen
print ("met hoeveel mensen wil je spelen? (Kies uit: 1, 2 of s voor stop)")



keuze = input()
# Bij 1 speler het te raden woord getoond als underscores. bijvoorbeeld: ‘_ _ _ _ _ _’ voor een 6 letter woord
if keuze == "1":
    print(woordkeuze)  
    print("Raad het woord.")
    print("Je hebt 5 pogingen.")

    # Als het woord niet geraden is en de pogingen niet voorbij zijn doe dan:
    while pogingen > 0 and geraden == False:
        geraden_woord = ""

        # Als de letter in het woord zit dan wordt de letter getoond ALS het geraden is anders een underscore
        for letter in woordkeuze:
            if letter in geraden_letters:
                geraden_woord = geraden_woord + letter
            else:
                geraden_woord = geraden_woord + "_"
        
        # Als het geraden woord gelijk is aan de woordkeuze dan is het woord geraden JIPPIEE
        if geraden_woord == woordkeuze:
            geraden = True
            print("Je hebt het woord van de dag geraden! Gefeliciteerd!")

        # Zo niet dan gaan we het woord proberen te raden
        else:
            print(geraden_woord) #geraden woord in _ als het niet geraden is
            gokken = input("Typ een letter of het hele woord: ") #input van de speler
            os.system('cls') #clear de console

            if len(gokken) == 1: #als de lengte van de input 1 is dan is het één letter
                geraden_letters.append(gokken) #voeg de letter toe aan de lijst van geraden letters, Apped voegt letters toe aan een lijst. 
                
                if gokken not in woordkeuze: #Als de letter niet in het woord zit dan heb je één poging minder
                    pogingen = pogingen - 1
                    print("Loser! je hebt nog", pogingen, "pogingen over.")
            else:
                if gokken == woordkeuze:
                    geraden = True
                    print("Hoppa, je hebt het woord juist geraden.")
                else: 
                    pogingen = pogingen - 1
                    print("Loser! je hebt nog", pogingen, "pogingen over.")

  
    






# Bij 2 spelers wordt de vraag gesteld: “Geef een door de andere speler te raden woord op
elif keuze == "2":
    woordkeuze = input("Geef een door de andere speler te raden woord op: ")
    os.system('cls') #clear de console

    print("Het woord is ingevoerd.")
    print("Raad het woord.")
    print("Je hebt 5 pogingen.")

    # Als het woord niet geraden is en de pogingen niet voorbij zijn doe dan:
    while pogingen > 0 and geraden == False:
        geraden_woord = ""

        # Als de letter in het woord zit dan wordt de letter getoond ALS het geraden is anders een underscore
        for letter in woordkeuze:
            if letter in geraden_letters:
                geraden_woord = geraden_woord + letter
            else:
                geraden_woord = geraden_woord + "_"
        
        # Als het geraden woord gelijk is aan de woordkeuze dan is het woord geraden JIPPIEE
        if geraden_woord == woordkeuze:
            geraden = True
            print("Je hebt het woord van de dag geraden! Gefeliciteerd!")

        # Zo niet dan gaan we het woord proberen te raden
        else:
            print(geraden_woord) #geraden woord in _ als het niet geraden is
            gokken = input("Typ een letter of het hele woord: ") #input van de speler
            os.system('cls') #clear de console

            if len(gokken) == 1: #als de lengte van de input 1 is dan is het één letter
                geraden_letters.append(gokken) #voeg de letter toe aan de lijst van geraden letters, Apped voegt letters toe aan een lijst. 
                
                if gokken not in woordkeuze: #Als de letter niet in het woord zit dan heb je één poging minder
                    pogingen = pogingen - 1
                    print("Loser! je hebt nog", pogingen, "pogingen over.")
            else:
                if gokken == woordkeuze:
                    geraden = True
                    print("Hoppa, je hebt het woord juist geraden.")
                else: 
                    pogingen = pogingen - 1
                    print("Loser! je hebt nog", pogingen, "pogingen over.")


# Stopt het programma
elif keuze == "s":
    os.system('cls') #clear de console
    print("Progamma gestopt.")

# Als er een fout is opgetreden
else: 
    print("Er is een fout opgestreden..")
