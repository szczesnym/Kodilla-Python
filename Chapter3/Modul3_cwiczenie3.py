def replace_all_in_list(text_list, dic_of_repls):
    new_text_list = []
    for text in text_list:
        for orig, repl in dic_of_repls.items():
            text = text.replace(orig, repl)
        new_text_list.append(int(text))
    return new_text_list

models = ['Volkswagen - Golf', 'Renault - Clio', 'Volkswagen - Polo',
          'Ford - Fiesta', 'Nissan - Qashqai', 'Peugeot - 208', 'VW - Tiguan',
          'Skoda - Octavia', 'Toyota - Yaris', 'Opel - Corsa',
          'Dacia - Sandero', 'Renault - Captur', 'Citroen - C3',
          'Peugeot - 3008', 'Ford - Focus', 'Fiat - 500', 'Dacia - Duster',
          'Peugeot - 2008', 'Skoda - Fabia', 'Fiat - Panda', 'Opel - Astra',
          'VW - Passat', 'Mercedes-Benz - A-Class', 'Peugeot - 308', 'Ford - Kuga']

sales2018 = ['445,754', '336,268', '299,920', '270,738', '233,026', '230,049',
             '224,788', '223,352', '217,642', '217,036', '216,306', '214,720',
             '210,082', '204,197', '196,583', '191,205', '182,100', '180,204',
             '172,511', '168,697', '160,275', '157,986', '156,020', '155,925',
             '154,125']

sales2017 = ['483,105', '327,395', '272,061', '254,539', '247,939', '244,615',
             '234,916', '230,116', '199,182', '232,738', '196,067', '212,768',
             '207,299', '166,784', '214,661', '189,928', 'NA', '180,868',
             '180,136', '187,322', '217,813', '184,123', 'NA', 'NA', 'NA']

sales2016 = ['492,952', '315,115', '308,561', '300,528', '234,340', '249,047',
             '180,198', '230,255', '193,969', '264,844', '170,300', '217,105',
             '134,560', 'NA', '214,435', '183,730', 'NA', 'NA', '177,301',
             '191,617', '253,483', '208,575', 'NA', '195,653', 'NA']

replacement = {'NA': '0', ',': ''}
repl_sales2016 = replace_all_in_list(sales2016, replacement)
repl_sales2017 = replace_all_in_list(sales2017, replacement)
repl_sales2018 = replace_all_in_list(sales2018, replacement)




cars = {}
for model in models:
    (vendor, name) = model.split(' - ')
    index = models.index(model)
    sales = {'2016': repl_sales2016[index], '2017': repl_sales2017[index], '2018': repl_sales2018[index]}
    if vendor not in cars.keys():
        cars[vendor] = {name: sales}
    cars[vendor][name] = sales
print(cars)

#Question 1
max_2017_index = repl_sales2017.index(max(repl_sales2017))
answer1 = models[max_2017_index].split(' - ')[1]
print('Anwser 1:' + str(answer1))

#question 2
sale_by_producer = {}
for vendor in cars.keys():
    for model in cars[vendor].keys():
        vendor_sale = sum(cars[vendor][model].values())
        if vendor in sale_by_producer.keys():
            sale_by_producer[vendor] += vendor_sale
        else:
            sale_by_producer[vendor] = vendor_sale
best_performer = sorted(sale_by_producer.items(), reverse=True)[0] #tylko na potrzeby print poniżej
answer2 = 'Producer with hihgest sales: ' + best_performer[0] + ' with sales: ' + str(best_performer[1])
print(answer2)

#question 3
new_sales_2017 = 0
for i in range(1, len(repl_sales2017)):
    if repl_sales2017[i] != 0 and repl_sales2016[i] == 0:
        new_sales_2017 += 1
answer3 = new_sales_2017
print("New sales in 2017: " + str(answer3))

#question 4
sale_by_model = {}
for vendor in cars.keys():
    for model in cars[vendor].keys():
        model_sales = sum(cars[vendor][model].values())
        sale_by_model[model] = model_sales
worst_performer = min(sale_by_model, key=sale_by_model.get) #tylko na potrzeby print poniżej
answer4 = 'Model with lowest sales: ' + worst_performer + ' with sales: ' + str(sale_by_model.get(worst_performer))
print(answer4)


#question 5
ford_model_sale = [cars[model] for model in cars if 'Ford' in model]
value_year_2018 = sum([sales['2018'] for sales in ford_model_sale[0].values()])
value_year_2017 = sum([sales['2017'] for sales in ford_model_sale[0].values()])
answer5 = (value_year_2018 - value_year_2017) * 100 // value_year_2018
print('Sales 2018 to 2017 increased by: ' + str(answer5) + '%')
