# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# print max(numbers)
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
a = 0
large = numbers[a]
while a < len(numbers):
  if numbers[a] > large:
    large = numbers[a]
  a = a+1
print large
 