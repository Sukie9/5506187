def case_counter(text):
    uppercase_count = 0
    lowercase_count = 0

    for char in text:
        if char.isalpha():
            if char.isupper():
                uppercase_count += 1
            elif char.islower():
                lowercase_count += 1

    print("Uppercase letters:", uppercase_count)
    print("Lowercase letters:", lowercase_count)

# Example of using the function with user input
user_input = input("Enter a phrase: ")
case_counter(user_input)






