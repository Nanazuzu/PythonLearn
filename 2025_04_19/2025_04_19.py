def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if all([any(temp.isupper() for temp in password), any(temp.islower() for temp in password), any(temp.isdigit() for temp in password), any(sym in password for sym in '!@#$%^&*()-_+=')]):
        return True
    else:
        return False
    
print(is_strong_password("Passw0rd!"))
print(is_strong_password("password"))
print(is_strong_password("Pa$13"))