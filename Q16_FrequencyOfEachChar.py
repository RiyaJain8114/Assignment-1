from collections import Counter
user_input = input("Enter a string: ")
frequency = Counter(user_input)
print("Character frequencies:", dict(frequency))
