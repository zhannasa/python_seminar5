
# def prime_number(n):
#     count = 0
#     for i in range(2, n//2+1):
#         if n % i == 0:
#             count+=1
#     if count <= 0:
#         print('Yes') 
#     else:
#         print('No')
# n = int(input('Enter the number: '))
# print(prime_number(n))

def prime_number(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count+=1
    if count == 2:
        print('Yes') 
    else:
        print('No')
n = int(input('Enter the number: '))
print(prime_number(n))
