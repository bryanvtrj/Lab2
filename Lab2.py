def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input("Input: ")
    input_list = user_input.split(",")
    float_list = [float(number.strip()) for number in input_list]
    return float_list

def calc_average_temperature(temperature_list):
    total = sum(temperature_list)
    average = total / len(temperature_list)
    return average

def calc_min_max_temperature(temperature_list):
    min_temp = min(temperature_list)
    max_temp = max(temperature_list)
    return [min_temp, max_temp]

# Define the main function
def main():
    # Call display_main_menu and get input
    display_main_menu()
    numbers = get_user_input()

    # Calculate average, min, and max temperatures
    average = calc_average_temperature(numbers)
    min_max = calc_min_max_temperature(numbers)

    # Display the results
    print("Average temperature:", average)
    print("Minimum and Maximum temperatures:", min_max)

# Entry point of the program
if __name__ == "__main__":
    main()
