# Task 1: Start

print("How many servings is the original recipie?")
try:
    original_amount = int(input())
except ValueError:
    print("Please only enter a number!")
    exit()

print("How many servings do you wish to make?")
try:
    new_amount = int(input())
except ValueError:
    print("Please only enter a number!")
    exit()


# Task 2: Quantity Calculation

def calculate_new_servings(original_amount, new_amount):
    try:
        if new_amount != original_amount:
            return new_amount/original_amount
        else:
            return original_amount
    except:
        print("Math as we know it is not capable of calculating your intended values")



# Task 3: Serving Success
        
    finally:
        print("Thank you for using the recipie size calculator, enjoy your meal!")

print("Multiply your measurments by this: " + str(calculate_new_servings(original_amount, new_amount)))