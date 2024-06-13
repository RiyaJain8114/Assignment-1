def calculate_age(current_year, birth_year):
    return current_year - birth_year

def main():
    try:
        current_year = int(input("Enter the current year: "))
        birth_year = int(input("Enter your birth year: "))
        age = calculate_age(current_year, birth_year)
        print(f"You are {age} years old.")
    except ValueError:
        print("Please enter a valid year.")

if __name__ == "__main__":
    main()
