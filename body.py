#!python3
###written by c4dburry

# BMI Rechner
# Formel
# BMI = Körpergewicht : (Körpergröße)²

##testing

#Eingaben
print("Bitte geben Sie ihr Gewicht ein: ")
bodyweight=float(input())
print("Bitte geben Sie ihre Körpergröße in cm an:")
bodysize=float(input())
bodysize=bodysize/100



#Berechnung
bmi = bodyweight / (bodysize**2 )
format_bmi = "{:.2f}".format(bmi)

print(format_bmi) 
