div_by_5 = [number for number in range(0,101) if number % 5 == 0]
div_by_5_pow_3 = map(lambda x: x**3, div_by_5)
#lub           = [number**3 for number in div_by_5]
print(div_by_5)
print(list(div_by_5_pow_3))

