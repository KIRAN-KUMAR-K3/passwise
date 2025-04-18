import math
import re

# Load common passwords
with open('common_passwords.txt') as f:
    common_passwords = set(p.strip() for p in f.readlines())

def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'\d', password): charset += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): charset += 32
    if charset == 0: return 0
    return round(len(password) * math.log2(charset), 2)

def check_strength(password):
    strength = "Very Weak"
    suggestions = []

    if password.lower() in common_passwords:
        suggestions.append("Avoid common passwords.")
        return strength, suggestions, 0

    length = len(password)
    entropy = calculate_entropy(password)

    # Criteria-based score
    score = 0
    if length >= 8: score += 1
    if re.search(r'[a-z]', password): score += 1
    if re.search(r'[A-Z]', password): score += 1
    if re.search(r'\d', password): score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): score += 1

    if score == 5: strength = "Very Strong"
    elif score >= 4: strength = "Strong"
    elif score == 3: strength = "Moderate"
    elif score == 2: strength = "Weak"

    if length < 8:
        suggestions.append("Use at least 8 characters.")
    if not re.search(r'[A-Z]', password):
        suggestions.append("Add uppercase letters.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        suggestions.append("Include special characters.")
    if not re.search(r'\d', password):
        suggestions.append("Include numbers.")

    return strength, suggestions, entropy
