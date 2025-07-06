import re

def load_common_passwords(filename="weak_passwords.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return set(line.strip().lower() for line in f if line.strip())
    except FileNotFoundError:
        print("[!] common_passwords.txt file not found.")
        return set()

def check_password_strength(password: str, weak_passwords: set) -> dict:
    score = 0
    suggestions = []

    if password.lower() in weak_passwords:
        return {
            "status": "Very Weak",
            "score": 0,
            "suggestions": ["This password leaked!. Create a unique, strong password."]
        }

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z).")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Include at least one digit (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character (!@#$ etc.).")

    if score == 5:
        status = "Strong"
    elif score >= 3:
        status = "Medium"
    else:
        status = "Weak"

    return {
        "status": status,
        "score": score,
        "suggestions": suggestions
    }

if __name__ == "__main__":
    weak_passwords = load_common_passwords()

    print("Password Strength Checker")
    print("Type `quit` or `exit` to stop.\n")

    while True:
        user_password = input("Enter password: ")

        if user_password.lower() in ["quit", "exit"]:
            print("Exiting... Goodbye!")
            break

        if not user_password:
            print("[!] No password entered!\n")
            continue

        result = check_password_strength(user_password, weak_passwords)

        print(f"\n[✔] Password Status: {result['status']}")
        print(f"[✔] Score: {result['score']}/5")

        if result["suggestions"]:
            print("\n[!] Suggestions:")
            for suggestion in result["suggestions"]:
                print(f"  - {suggestion}")
        print("\n" + "-"*40 + "\n")
