def find_min_max(numbers):
    if not numbers:
        return None, None

    min_value = numbers[0]
    max_value = numbers[0]

    for num in numbers:
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num

    return min_value, max_value

if __name__ == "__main__":
    try:
        user_input = input("Enter a list of numbers separated by spaces: ")
        number_list = [float(num) for num in user_input.split()]
        min_value, max_value = find_min_max(number_list)
        if min_value is not None and max_value is not None:
            print(f"The minimum value is: {min_value}")
            print(f"The maximum value is: {max_value}")
        else:
            print("The list is empty.")
    except ValueError:
        print("Please enter a valid list of numbers.")
