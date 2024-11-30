import random

n = 5  


arrays = []
for i in range(3):
    array = [random.randint(0, 100) for i in range(n)]
    arrays.append(array)

max_element = 0
total_sum = 0

for array in arrays:
    max_element = max(max_element, max(array))
    total_sum += sum(array)

print("Созданные массивы:", arrays)
print("Наибольший элемент:", max_element)
print("Сумма всех элементов:", total_sum)