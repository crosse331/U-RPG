import random
import time

def battle_logic():
    win_chance = 50
    if random.randint(0, 100) < win_chance:
        print("Ты победил!")
    else:
        print("Ты проиграл!")