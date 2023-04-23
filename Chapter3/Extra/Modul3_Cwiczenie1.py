numbers = [5, 32, 56, 2, 2, 16, 7, 10, 23, 100]
#mean_number = 0

# numbers = list(map(lambda x: (x // 10) * 10, numbers))
numbers = [round(number, -1) for number in numbers]
print('Rounded elemants: ' + str(numbers))
numbers = [not_extrem for not_extrem in sorted(numbers) if not_extrem != min(numbers) and not_extrem != max(numbers)]
print('No MIN and MAX: ' + str(numbers))
mean_number = sum(numbers) / len(numbers)
print('Mean of the list: ' + str(mean_number))
