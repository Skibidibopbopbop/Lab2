def calculate_bmi(height, weight):     
    print("Height = " + str(height)) 
    print("Weight = " + str(weight)) 
    calculate_bmi = weight / (height*height)
    print("BMI = " +str(calculate_bmi))
    if calculate_bmi < 18.5:
        print("You are Under Weight!")
    elif 18.5 <= calculate_bmi <= 25.0:
        print("You are normal weight")
    else:
        print("You are FATTTTT!!!")


 
calculate_bmi(weight=57, height=1.73) 
