def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    while True:
        try:
            user_input = input("Enter a temperature and its unit (e.g., 25 C or 77 F): ")
            temp_parts = user_input.split()

            if len(temp_parts)!= 2:
                raise ValueError
            
            temp = temp_parts[0]
            unit = temp_parts[1]

            temp = float(temp)

            

            if unit== "C" or unit== "c":
                result = celsius_to_fahrenheit(temp)
                print("Temperature in Fahrenheit:", result, "F")
                break
            elif unit == "F" or unit=="f":
                result = fahrenheit_to_celsius(temp)
                print("Temperature in Celsius:", result, "C")
                break
            else:
                raise TypeError

        except ValueError:
            print("enter a valid number for temperature.")
        except TypeError:
            print("invalid unit. use C for Celsius or F for Fahrenheit.")

main()