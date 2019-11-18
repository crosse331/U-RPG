import random

#Universal RPG

def battle_logic():
    win_chance = 50
    if random.randint(0, 100) < win_chance:
        print("Ты победил!")
    else:
        print("Ты проиграл!")

print("Начинается игра!")
isGameEnded = False
while (not isGameEnded):
    battle_input = input("Начинается битва! Сражаться? (y|n)")
    if battle_input == "y" or battle_input == "Y":
        battle_logic()
    elif battle_input == "q" or battle_input=="Q":
        isGameEnded = True

print("Game Over!")
