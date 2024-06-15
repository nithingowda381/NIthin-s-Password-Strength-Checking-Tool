import re
def check_password_strength(password):  
    if len(password) < 8:
        return "Weak"  
    strength_criteria = [
        r"[A-Z]", 
        r"[a-z]",  
        r"[0-9]",  
        r"[@$!%*?&#]"  
    ]   
    matches = sum(bool(re.search(pattern, password)) for pattern in strength_criteria)  
    if matches == 4:
        return "Strong"
    elif matches >= 2:
        return "Okay"
    else:BBBBBBBBBBBBBBBBBBBBBV                                                          
        return "Weak"

def main():
    header = """
    ==========================================
    Nithin's Password Security Checking Tool
    ==========================================
    """
    print(header)
    
    while True:
        password = input("Enter a password to check its strength: ")
        
        strength = check_password_strength(password)
        print(f"The password '{password}' is {strength}.\n")
        
        if strength == "Strong":
            print("Password is strong enough. Exiting the tool.")
            break
        else:
            print("Please enter a stronger password.")

if __name__ == "__main__":
    main()
