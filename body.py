#!python3
###written by c4dburry



#Eingaben
#Körpergewicht
from time import sleep


print("Bitte geben Sie ihr Gewicht ein: ")
bodyweight=float(input())
#Körpergröße + Umrechnung von cm in m
print("Bitte geben Sie ihre Körpergröße in cm an:")
bodysize=float(input())
bodysize=bodysize/100
#Alter
print("Bitte geben Sie ihr Alter an:")
age=int(input())
#geschlecht
print("Bitte wählen Sie ihr Geschlecht aus: \n 1: männlich 2: weiblich 3:divers")
gender=int(input())
if gender == 1:
    gendertwo=1
elif gender > 1:
    gendertwo=2
else:
    gendertwo=3
print(gendertwo)
 
#Bewegungslevel
print("Bitte wählen Sie ihr Tätigkeitslevel aus:\n Level 1: liegend, keine Bewegung \n Level 2: wenig bewegung \n Level 3: vorwiegend sitzend \n Level 4: sitzend und stehend \n Level 5: körperlichg anstrengende Arbeit")
pal = int(input())
if pal == 1:
    pal = 0.95
elif pal == 2:
    pal = 1.2
elif pal == 3:
    pal = 1.6
elif pal == 4:
    pal = 1.8
else:
    pal = 2.0

    
#Berechnung läuft
print("Ihre Eingaben waren erfolgreich - Berechnung beginnt")
print("berechne Daten....")
sleep(5)
print("benutze deo....")
sleep(3)
print("lege Gewichte zurück....")
sleep(4)
print("flexing muscles---")

#Berechnung BMI
#BMI = Körpergewicht : (Körpergröße)²
print("BMI Daten")
bmi = bodyweight / (bodysize**2 )
format_bmi = "{:.2f}".format(bmi)
print(format_bmi) 

#Berechnung BMR
#BMR Formel für Männer
#BMR (kcal/24 h) = (10 x Körpergewicht) + (6,25 x Körpergöße in cm) - (5,0 x Alter) + 5
#BMR Formel für Frauen
#BMR (kcal/24 h) = (10 x Körpergewicht) + (6,25 x Körpergöße in cm) - (5,0 x Alter) - 161

print("BMR - Basic Metabolic Rate")
if gender == 2:
    bmr = (10 * bodyweight) + (6.25*bodysize*100) - (5*age) - (161)
else:
    bmr = (10 * bodyweight) + (6.25*bodysize*100) - (5*age) + (5)
format_bmr = "{:.2f}".format(bmr)
print(format_bmr)

#kcal bedarf berechnen
# Formel: kcal= BMR X PAL (physical activity Level)
kcal = bmr * pal 
print("Der Tagesbedarf an kcal ist:"+str(kcal))