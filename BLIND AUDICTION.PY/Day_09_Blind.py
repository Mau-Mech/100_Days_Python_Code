from art import logo
print (logo)

# Step 1: Show in the screen: Whats your name, save in a dictionary (as key)
# Step 2 ; Show in the screen: Whats your bid, and save in the same dictionary (as value)

higher_value = {}

next_person = "yes"

while next_person == "yes":

    name = str(input("What's your name?: "))
    price = int(input("What's your bid?: $"))
    higher_value[name] = price
    next_person = str(input("Are there any other biders? Type 'yes' or 'no' please. ")).lower()


val = list(higher_value.values())
v1 = 0
for conta in val:
    if v1 <= conta:
        v1 = conta

for key,value in higher_value.items():
    if value == v1:
        print(f"The highest bidder its: {key}--{value}")
        break