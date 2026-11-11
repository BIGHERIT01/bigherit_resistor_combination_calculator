
# RESISTOR COMBINATION CALCULATOR


# Function to collect resistor values
def get_resistors():
    resistors = []

    # Ask for the number of resistors
    number = int(input("How many resistors do you have? "))

    # Check that the number is greater than zero
    while number <= 0:
        print("Enter a number greater than zero.")
        number = int(input("How many resistors do you have? "))

    # Collect each resistor value
    for i in range(number):
        value = float(input(f"Enter resistor {i + 1} value (ohms): "))

        # Check that resistance is positive
        while value <= 0:
            print("Resistance must be greater than zero.")
            value = float(input(f"Enter resistor {i + 1} value (ohms): "))

        # Add resistor value to the list
        resistors.append(value)

    return resistors


# Function to calculate series resistance
def calculate_series(resistors):
    total = sum(resistors)
    return total


# Function to calculate parallel resistance
def calculate_parallel(resistors):
    total = 0

    # Add the reciprocal of each resistor
    for value in resistors:
        total += 1 / value

    return 1 / total


# Function to compare resistor values
def compare_resistors(resistors):

    # Find the highest, lowest and average values
    highest = max(resistors)
    lowest = min(resistors)
    average = sum(resistors) / len(resistors)

    # Display comparison results
    print("\n----- RESISTOR COMPARISON -----")
    print("Highest Resistance:", highest, "ohms")
    print("Lowest Resistance:", lowest, "ohms")
    print("Average Resistance:", round(average, 2), "ohms")
    

# MAIN PROGRAM MENU


while True:

    print("\n================================")
    print("   BIGHERIT RESISTANCE CALCULATOR")
    print("================================")
    print("1. Calculate resistance")
    print("2. Compare resistors")
    print("3. Exit")

    # Collect user's choice
    choice = int(input("Enter your choice: "))

    if choice == 1:

        values = get_resistors()

        series = calculate_series(values)
        parallel = calculate_parallel(values)

        print("\n----- CALCULATION RESULTS -----")
        print("Series Resistance:", round(series, 2), "ohms")
        print("Parallel Resistance:", round(parallel, 2), "ohms")

    elif choice == 2:

        values = get_resistors()
        compare_resistors(values)

    elif choice == 3:

        print("\nThank you for using BigHerit Resistance Calculator!")
        break

    else:
        print("Invalid choice. Try again.")
