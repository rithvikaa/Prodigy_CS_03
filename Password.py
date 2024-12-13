def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    number_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password)

    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    feedback = ""

    if strength_score == 5:
        feedback += "Strength: Very Strong ✅"
    elif strength_score == 4:
        feedback += "Strength: Strong ✅"
    elif strength_score == 3:
        feedback += "Strength: Moderate ⚠️"
    elif strength_score == 2:
        feedback += "Strength: Weak ❌"
    else:
        feedback += "Strength: Very Weak ❌❌"

    if not length_criteria:
        feedback += "\n- Password should be at least 8 characters long."
    if not uppercase_criteria:
        feedback += "\n- Include at least one uppercase letter."
    if not lowercase_criteria:
        feedback += "\n- Include at least one lowercase letter."
    if not number_criteria:
        feedback += "\n- Include at least one number."
    if not special_char_criteria:
        feedback += "\n- Include at least one special character."

    return feedback

password = input("Enter a password to check its strength: ")
print("\nPassword Feedback:")
print(check_password_strength(password))
