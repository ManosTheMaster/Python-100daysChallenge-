from replit import clear
bitters = {}

name = input("What is your name?")
bit = input("Enter your bid?")
maxBit = bit
winner = name
answer = input("Are they any other bitters?")
while answer == "Yes":

    bitters[name] = bit
    for name in bitters:
        if bitters[name] > maxBit:
            maxBit = bit
            winner = name
    clear()
    name = input("What is your name? ")
    bit = input("Enter your bid? $")
    answer = input("Are they any other bitters? ")

print(f"The winner is {winner} with {bit}$ bit")

    


