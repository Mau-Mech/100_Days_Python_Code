string = input("Type any phrase: ")
print(f"\n¿All the letters are minus?: {string.islower()}")
string = string.lower()
print(f"String in minus: {string}")

print(f"\n¿All the letters are in mayus?: {string.isupper()}")
print(f"String in mayus. {string.upper()}")
print(f"String original: {string}")