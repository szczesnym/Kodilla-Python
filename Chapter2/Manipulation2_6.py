#Task 1
cube_list = [number ** 3 for number in range(1, 10)]
print(list(number ** 3 for number in range(1, 10) if number ** 3 % 2 != 0))

#Lub klasycznie
#for cube in cube_list:
#    if not cube % 2 == 0:
#        print(cube)

#Task 2
input_list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
print(list(number for number in input_list if number == 0))
print(list(number for number in input_list if number != 0))
