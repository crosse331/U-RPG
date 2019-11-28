import random
import core.quest as quest
import core.battle as battle
import time


class MainGame:
    def __init__(self):
        self.text = [
            "Ты двигаешься дальше, но ничего не происходит...",
            "Ты огляделся, ничего не увидел, и пошёл дальше...",
            "..."]
        self.isGameEnded = False

    def logic(self):
        print("Начинается игра!")
        while not self.isGameEnded:
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
                    self.isGameEnded = True

                continue
            else:
                print(self.text[random.randint(0, 2)])
                continue

        print("Game Over!")



