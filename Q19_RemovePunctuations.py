def remove_punctuation(input_string):
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
    return ''.join(char for char in input_string if char not in punctuation)

def main():
    user_input = input("Enter a string: ")
    result = remove_punctuation(user_input)
    print("String without punctuation:", result)

if __name__ == "__main__":
    main()
