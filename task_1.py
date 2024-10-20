numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_index = numbers.index(None)

total_sum = sum(numbers[:missing_index] + numbers[missing_index+1:])

count = len(numbers)

average = total_sum / count

numbers[missing_index] = average

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:",numbers)

