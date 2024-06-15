
# Password Strength Checking Tool

## Overview
This Python script is designed to assess the strength of passwords based on specific criteria. It categorizes passwords into three levels: Weak, Okay, and Strong, providing feedback to users on the security of their chosen passwords.

## Features
- **Password Criteria**: Evaluates passwords based on length and the presence of uppercase letters, lowercase letters, digits, and special characters.
- **User Interaction**: Prompts users to input passwords and informs them of their strength level.
- **Looped Execution**: Allows continuous checking until a strong password is entered.
- **Exit Condition**: Terminates once a strong password is identified, ensuring efficiency in password selection.

## Criteria for Password Strength
- **Weak**: Passwords less than 8 characters long.
- **Okay**: Passwords that meet at least two of the following:
  - Contains at least one uppercase letter (A-Z)
  - Contains at least one lowercase letter (a-z)
  - Contains at least one digit (0-9)
  - Contains at least one special character from the set `@$!%*?&#`
- **Strong**: Passwords that meet all four criteria listed above.

## Usage
1. **Run the Script**: Execute the script in a Python environment.
2. **Input Password**: Enter a password when prompted.
3. **Assessment**: The tool will evaluate the password and provide feedback.
4. **Feedback**: If the password is deemed "Weak" or "Okay", users will be prompted to enter a stronger password. If the password is "Strong", the tool will exit.

## Example Output
```
==========================================
Nithin's Password Security Checking Tool
==========================================

Enter a password to check its strength: Password123@
The password 'Password123@' is Strong.

Password is strong enough. Exiting the tool.
```

## Dependencies
- Python 3.x
- `re` module (standard library)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Nithin Gowda M S

---

