def count_occurrences(elements, target):
    return elements.count(target)

if __name__ == "__main__":
    try:
        user_input = input("Enter a list of elements separated by spaces: ")
        elements = user_input.split()
        target = input("Enter the element to count: ")
        count = count_occurrences(elements, target)
        print(f"The element '{target}' occurs {count} times in the list.")
    except Exception as e:
        print(f"An error occurred: {e}")

