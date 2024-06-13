def sum_of_numbers(numbers):
    return sum(numbers)

if __name__ == "__main__":
    try:
        user_input = input("Enter a list of numbers separated by spaces: ")
        number_list = [float(num) for num in user_input.split()]
        result = sum_of_numbers(number_list)
        print(f"The sum of the numbers is: {result}")
    except ValueError:
        print("Please enter a valid list of numbers.")

