string = "0123456789"
substring = ""

print(f"Pricipal chain: {string}")

substring = string[0]
print(f"\nSubchain with location [0] is {substring}")

substring = string[5]
print(f"\nSubchain with location [5] is {substring}")

substring = string[-4]
print(f"\nSubchain with location [-4] is {substring}")

substring = string[0:3]
print(f"\nSubchain with locations [0:3] is {substring}")

substring = string[:3]
print(f"\nSubchain with locations [:3] is {substring}")

substring = string[5:]
print(f"\nSubchain with locations [:5] is {substring}")

substring = string[-4:-1]
print(f"\nSubchain with locations [-4:-1] is {substring}")

substring = string[:]
print(f"\nSubchain with locations [:] is {substring}")

substring = string[1:6:2]
print(f"\nSubchain with locations and each space [1:6:2] is {substring}")

substring = string[::3]
print(f"\nSubchain with locations and each space [::3] is {substring}")