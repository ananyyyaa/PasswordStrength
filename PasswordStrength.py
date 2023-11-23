def check_password_strength(password):
   
    length_req = 10
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()_+{}[]|\\;:'\",.<>?`~"

    if len(password) < length_req:
        return "WEAK : Password is too short minimum 10 characters"

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if has_uppercase and has_lowercase and has_digit and has_special:
        return "STRONG"
    else:
        return "WEAK : Password should include uppercase, lowercase, digit, and special character"


password_input = input("Enter your password: ")
strength = check_password_strength(password_input)
print("Password strength:", strength)
