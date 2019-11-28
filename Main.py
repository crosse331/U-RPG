import random
import quest
import battle
import time

#Universal RPG

text = [
    "Ты двигаешься дальше, но ничего не происходит...",
    "Ты огляделся, ничего не увидел, и пошёл дальше...",
    "..."]

print("Начинается игра!")
isGameEnded = False
while (not isGameEnded):
    time.sleep(1)
    battle_chance = 10
    quest_chance = 5
    if random.randint(0, 100) < battle_chance:
        print("На тебя напал страшный АйМонстр.")
        print("Начинается битва!")
        battle.battle_logic()
        continue
    elif random.randint(0, 100) < quest_chance:
        print("Ты обнаружил какое-то строение.")
        quest_input = input("Обследуешь его? (y|n)")
        if quest_input == "y" or quest_input == "Y":
            quest.quest_logic()
        elif quest_input == "q" or quest_input == "Q":
            isGameEnded = True

        continue
    else:
        print(text[random.randint(0, 2)])
        continue

print("Game Over!")
