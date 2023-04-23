models = ['Volkswagen - Golf', 'Renault - Clio', 'Volkswagen - Polo',
          'Ford - Fiesta', 'Nissan - Qashqai', 'Peugeot - 208', 'VW - Tiguan',
          'Skoda - Octavia', 'Toyota - Yaris', 'Opel - Corsa',
          'Dacia - Sandero', 'Renault - Captur', 'Citroen - C3',
          'Peugeot - 3008', 'Ford - Focus', 'Fiat - 500', 'Dacia - Duster',
          'Peugeot - 2008', 'Skoda - Fabia', 'Fiat - Panda', 'Opel - Astra',
          'VW - Passat', 'Mercedes-Benz - A-Class', 'Peugeot - 308', 'Ford - Kuga']

sales2018 = ['445,754', '336,268', '299,920', '270,738', '233,026', '230,049', '224,788', '223,352', '217,642', '217,036', '216,306', '214,720', '210,082', '204,197', '196,583', '191,205', '182,100', '180,204', '172,511', '168,697', '160,275', '157,986', '156,020', '155,925', '154,125']
sales2017 = ['483,105', '327,395', '272,061', '254,539', '247,939', '244,615', '234,916', '230,116', '199,182', '232,738', '196,067', '212,768', '207,299', '166,784', '214,661', '189,928', 'NA',      '180,868', '180,136', '187,322', '217,813', '184,123', 'NA',       'NA',      'NA']
sales2016 = ['492,952', '315,115', '308,561', '300,528', '234,340', '249,047', '180,198', '230,255', '193,969', '264,844', '170,300', '217,105', '134,560', 'NA',      '214,435', '183,730', 'NA',      'NA',      '177,301', '191,617', '253,483', '208,575', 'NA',       '195,653', 'NA']





sale_by_producer = {}
for model in models:
    (vendor, name) = model.split(' - ')
    vendor_sale = sum(map(lambda x: 0 if x == 'NA' else int(x.replace(',', '')), cars[vendor][name].values()))
    if vendor in sale_by_producer.keys():
        sale_by_producer[vendor] += vendor_sale
    else:
        sale_by_producer[vendor] = vendor_sale
best_performer = sorted(sale_by_producer.items(), reverse=True)[0] #tylko na potrzeby print poniżej
print('Producer with hihgest sales2: ' + best_performer[0] + ' with sales: ' + str(best_performer[1]))
anwser2 = best_performer[0]

sale_by_producer = {}
for vendor in cars.keys():
    for model in cars[vendor].keys():
        #print(cars[vendor][model].values())
    #(vendor, name) = model.split(' - ')
        vendor_sale = sum(map(lambda x: 0 if x == 'NA' else int(x.replace(',', '')), cars[vendor][model].values()))
        if vendor in sale_by_producer.keys():
            sale_by_producer[vendor] += vendor_sale
        else:
            sale_by_producer[vendor] = vendor_sale
best_performer = sorted(sale_by_producer.items(), reverse=True)[0] #tylko na potrzeby print poniżej
print('Producer with hihgest sales: ' + best_performer[0] + ' with sales: ' + str(best_performer[1]))
#anwser2 = best_performer[0]


sale_by_model = {}
tempList =[]
for car in cars.keys():
    #print(cars.get(car).values())
    for model in cars.get(car).keys():
        for x in cars.get(car).values():
            sale_by_model[model] = sum(map(lambda y: 0 if y == 'NA' else int(y.replace(',', '')), x.values()))
max_key = max(sale_by_model, key=sale_by_model.get)
print(max_key + ': value:' +str(sale_by_model.get(max_key)))


for vendor in cars.keys():
    for model in cars[vendor].keys():
        model_sale = sum(cars[vendor][model].values())
        p