names = ['Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz', 'Edward', 'Piotr',
         'Jan', 'Denis', 'Amir', 'Igor', 'Borys', 'Robert', 'Ariel', 'Kuba',
         'Rafał', 'Mateusz', 'Emanuel', 'Alfred', 'Artur', 'Jakub', 'Ludwik',
         'Bolesław', 'Remigiusz', 'Martin', 'Dobromił', 'Mariusz', 'Amadeusz',
         'Łukasz', 'Bolesław', 'Amir', 'Artur', 'Albert', 'Olgierd', 'Alek',
         'Kordian', 'Julian', 'Anastazy', 'Emanuel', 'Józef']
name_dict ={}
for name in sorted(names):
    first_letter = name[0]
    if first_letter not in name_dict.keys():
        name_dict[first_letter] = []
    name_dict[first_letter].append(name)
print(name_dict)