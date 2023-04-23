dice ={}
for y in range(1, 7):
   for z in range(1, 7):
       if (y + z) < 12:
            if (y + z) not in dice.keys():
                dice[y + z] = []
            dice[y + z].append((y, z))
print(dice)


dice ={}
for x in range(2, 13):
    dice[x] = list(map(lambda y: (y, x - y), filter(lambda y: 1 <= x - y <= 6, range(1, 7))))
print(dice)
