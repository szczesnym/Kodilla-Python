# Task 1
name_list = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
name_dictionary = {}

for name in name_list:
    name_dictionary[name] = len(name)
print(name_dictionary)

# Task 2
numbers = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
new_list = []

for number in numbers:
    prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            prime = False
    if prime:
        new_list.append(number)
print(new_list)


# Task 3
days = ['pon', 'śro', 'pią', 'sob']
days_dict = {'pon': 1, 'wto': 2, 'śro': 3, 'czw': 4, 'pią': 5, 'sob': 6, 'nie': 7}

for day_name, day_number in days_dict.items():
    if not day_name in days:
        days.insert(day_number - 1, day_name)
print(days)


# Task 4
alien_tea_make_steps = {'wyjmij kubek': 1, 'znajdź opakowanie herbaty': 0,
                        'włóż herbatę do kubka': 2, 'zalej herbatę': 5,
                        'włącz czajnik': 4, 'nalej wody do czajnika': 3}

for step_desc, _ in sorted(alien_tea_make_steps.items(), key=lambda x: x[1]):
    print(step_desc)
