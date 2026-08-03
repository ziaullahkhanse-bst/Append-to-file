
try:
    a=int(input("Enter your age: "))
    if a<18 and a>0:
        print(f"Your are less than 18 and your age is {a}")

    elif a>=18:
        print(f"Your are an adult and your age is {a}")
except:
        print("Please enter a valid number.")