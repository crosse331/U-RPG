import random
import time

def quest_logic():
    win_chance = 50
    if random.randint(0, 100) < win_chance:
        print("Ты выполнил квест и получил новое оружие!")
        print("Наносимый урон значительно увеличился!")
    else:
        print("Ты ещё слаб для таких сложных задач. Возвращайся, когда станешь сильнее.")
