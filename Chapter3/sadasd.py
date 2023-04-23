dice_combinations = {}

# Używamy funkcji map() i wyrażenia lambda do wygenerowania kombinacji wyników dla każdej sumy oczek w dwóch rzutach
for i in range(2, 13):
    dice_combinations[i] = set(map(lambda x: (x, i-x), range(1, 7)))

print(dice_combinations)