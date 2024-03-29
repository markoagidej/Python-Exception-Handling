# Task 1: Start

temp = input("Enter the temperature in Fahrenheit: ")

try:
    f_temp = int(temp)
except:
    print("Please only input numerical values.")


# Task 2: Temperature Conversion

def convert_f_to_c(temp):
    try:
        new_temp = (temp - 32) * 5/9
    except OverflowError:
        print("That temperature is probably too big to exist")
    except:
        print("Not a valid temperature!")


# Task 3: User Experience
    else:
        print(new_temp)
    finally:
        print("Thank you for using the temperature converter!")
        
convert_f_to_c(f_temp)