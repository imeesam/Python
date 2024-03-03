weight = float(input("Enter your weight in kg"))
height = float(input("Enter your height in meter"))
BMI = weight/(height)**2
if BMI < 18.5 :
    print("You are UnderWeight")
elif BMI >= 18.5 or BMI <= 24.9 :
    print("You are NormalWeight")
elif BMI >= 25 or BMI <= 29.9 :
    print("You are OverWeight")
else :
    print("You are Obese")
