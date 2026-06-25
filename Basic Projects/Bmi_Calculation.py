#global variables and imports


#getting inputs

def get_input():
    weight = float(input("Enter your weight(kg):"))
    height = float(input("Enter your height(meter):"))
    return weight, height


#calculate bmi

def calculate_bmi(weight,height):
    return weight / (height**2)



#get bmi result
def bmi_reult(bmi):
    if bmi < 18.5:
        print("Under Weight!")
    elif 18.5 <= bmi < 25:
        print("Normal!")
    elif 25 <= bmi < 30:
        print("Over Weight!")
    elif 30 <= bmi < 35:
        print("Obese!")
    else:
        print("Exteremly Obese!")




#running the task


def main():
    weight,height = get_input()
    bmi = calculate_bmi(weight, height)
    bmi_reult(bmi)


if __name__ == "__main__":
    main()




