try:
    celsius = int(input("Enter the temperature in Celsius: "))
    farenheit = celsius * 2 + 30
    print(f"It is {farenheit} degrees")
except:
    print("Error, please input a number")