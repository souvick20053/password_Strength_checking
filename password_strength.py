import re
def password_strength_check(password):
    if len(password)<8:
        return "Weak ❌ (Too Short)"
    elif not re.search("[A-Z]",password):
        return "Weak ❌ (Add Uppercase)"
    elif not re.search("[a-z]",password):
        return "Weak ❌ (Add Lowercase)"
    elif not re.search("[0-9]",password):
        return "Weak ❌ (Add Number)"
    elif not re.search("[!@#$%^&*()]",password):
        return "Weak ❌ (Add Special character)"
    else:
        return "Strong Password ✅",password
    
password=input("Enter the Password=")
print(password_strength_check(password))
