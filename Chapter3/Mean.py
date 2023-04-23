numbers = [5, 32, 56, 2, 2, 16, 7, 10, 23, 100]
#mean_number = 0

# numbers = list(map(lambda x: (x // 10) * 10, numbers))
numbers = [round(number, -1) for number in numbers]
print(numbers)
numbers = [not_extrem for not_extrem in sorted(numbers) if not_extrem != min(numbers) & not_extrem != max(numbers)]
print(numbers)
mean_number = sum(numbers) / len(numbers)
print(mean_number)
