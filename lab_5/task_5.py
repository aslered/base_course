name = 'Yurii Solonovich Alexsandrovich'

upper_case_list = [ord(symbol) for symbol in name.upper()]
print(name.upper())
print(upper_case_list)

lower_case_list = [ord(symbol) for symbol in name.lower()]
print(name.lower())
print(lower_case_list)

sum_upper = sum(upper_case_list)
print(sum_upper)

sum_lower = sum(lower_case_list)
print(sum_lower)