#BMI Calculatior for training
#Real life needed code I guess

#1. Huvisagch buyu Variables uusgeh
name = (input("tanii ner: "))
weight_kg = float(input("jin (kg):"))
height_cm = float(input("Undur(cm):"))

#2. Expression - BMI Caclaulation
height_m = height_cm / 100
bmi = weight_kg / (height_m**2)

#3. Comparusib operatirs ашиглах
is_normal = bmi >= 18.5 and bmi <25
is_underweight = bmi < 18.5

#4 Statement - print хийх
print(f"Sain uu, {name}!")
print(f"Tanii BMI: {bmi:.2f}")
print(f"Heviin jintei yu ?{is_normal}")
print(f"Turanhai yu ? {is_underweight}")