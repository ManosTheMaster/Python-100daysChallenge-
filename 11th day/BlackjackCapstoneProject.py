#Randomness
import random

computer_firstCard = random.randint(1,10)
computer_secondCard = random.randint(1,10)

computer_cardList = [computer_firstCard, computer_secondCard]
computer_sumOfCards = computer_secondCard + computer_firstCard

players_firstCard = random.randint(1,10)
players_answer = input(f"You have a {players_firstCard}, do you want another? ('y' or 'n')")
if players_answer == "y":
    playerWantsExtraCard = True
else:
    playerWantsExtraCard = False
    
players_sumOfCards = players_firstCard

while playerWantsExtraCard and players_sumOfCards < 21:
    players_sumOfCards =+ random.randint(1,10)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

