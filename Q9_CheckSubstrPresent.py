string = input("Enter the main string: ")
substring = input("Enter the substring: ")
if substring in string:
    print(f"'{substring}' is in the string")
else:
    print(f"'{substring}' is not in the string")
