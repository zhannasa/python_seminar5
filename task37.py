# def reverse_numbers(numbers): 
#     if len(numbers) == 1:
#         return numbers
#     return numbers[-1] + reverse_numbers(numbers[:-1])

# n = int(input('Enter the number of elements: '))
# print(reverse_numbers(input('Enter the n elements: ')))
n = int(input('Enter the number of elements: '))
numbers = []
for _ in range(n):
    numbers.append(int(input()))
print(numbers)
for i in numbers[::-1]:
    print(i)




