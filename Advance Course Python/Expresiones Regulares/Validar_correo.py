import re

email = input("Email: ").strip()
#Muy simple
# if "@" in email and "." in email:
#     print("Email Valido")
# else:
#     print("Email Invalido")
# Simple
# username,domain = email.split("@")
#
# if username and domain.endswith(".com"):
#     print("Valido")
# else:
#     print("Invalido")

# Implementamos librería re

if re.search(r"^\w+@\w+\.(com|es)$",email,re.IGNORECASE):
    print("Valido")
else:
    print("Invalido")