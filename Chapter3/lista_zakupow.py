shopping = {
    'Piekarnia': ['Chleb', 'Pączek', 'Bułki'],
    'Warzywniak': ['Marchew', 'Seler', 'Rukola']
}
print('Lista zakupów')
for key in shopping:
    print(f'Idę do {key}, kupuję tu następujące rzeczy:{shopping[key]}')

#czy raczej tak ?:
#for key, value in shopping.items():
#   print(f'Idę do {key}, kupuję tu następujące rzeczy:{value}')

count = sum((map(lambda x: len(x), shopping.values())))
print(count)
