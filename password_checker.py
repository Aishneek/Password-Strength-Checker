import re
import getpass
def check_password_strength(password):
    score = 0
    feedback = []
    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should contain at least 8 characters.")
    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")
    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")
    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")
    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")
    # Determine password strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MODERATE"
    else:
        strength = "STRONG"
    return strength, feedback, score
# Main program
print("=" * 40)
print("       PASSWORD STRENGTH CHECKER")
print("=" * 40)
password = getpass.getpass("Enter your password: ")
strength, feedback, score = check_password_strength(password)
print("\nPassword Strength:", strength)
print("Security Score:", score, "/ 5")
if feedback:
    print("\nSuggestions to improve your password:")
    for suggestion in feedback:
        print("-", suggestion)
else:
    print("\nExcellent! Your password meets all the basic requirements.")
print("\nThank you for using Password Strength Checker!")