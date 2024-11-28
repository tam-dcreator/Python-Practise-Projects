import random

color_list = []
for _ in range(300):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)

    color = (r, g, b)
    color_list.append(color)
