def task_1():
    print ("Welcome to the Temperature Converter!")
    print ("This program converts between Celsius and Fahrenheit")
    continue_program = "yes"
    while continue_program == "yes":
        temperature = int(input ("Enter the temperature: "))
        conversion = input ("Convert to (C)elsius or (F)ahrenheit? ")
        if conversion == "C":
            result = (temperature - 32) * 5/9
            original_unit = "Fahrenheit"
            converted_unit = "Celsius"
            print("Converted ", temperature, "degrees", original_unit, " into", result, "degrees", converted_unit)
            continue_program = input("Do you want to continue?")
        elif conversion == "F":
            result = temperature * 9/5 + 32
            original_unit = "Celsius"
            converted_unit = "Fahrenheit"
            print("Converted ", temperature, "degrees", original_unit, " into", result, "degrees", converted_unit)
            continue_program = input("Do you want to continue?")
        else:
            print ("Invalid conversion choice! Please enter C or F.")       


def task_2():
    print ("Welcome to the Number Guessing Game!")
    print ("I'm thinking of a number between 1 and 100.")
    secret_number = 42
    max_attempts = 5
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        print ("Attempt " ,attempts, " of " ,max_attempts)
        guess = int(input ("Enter your guess: "))
        if guess == secret_number:
            print ("Congratulations! You guessed the number!")
            break
        elif guess < secret_number:
            print ("Too low! Try again.")
        else:
            print ("Too high! Try again.")


