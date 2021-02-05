'''
Write a program that takes two arrays representing integers, and retums an integer representing their product. For example, since 193707721.x -761838257287 = -147573952589676412927, if
the inputs are (1,9,3,7,0,7,7,2, 1) and <-7,6,L,8,3,8,2,5,7,2,8,7>, your function should refum
(-1, 4,7, 5,7,3, 9, 5, 2, 5,8,9, 6,7, 6, 4, 1., 2,9,2,7>.


we can use the grade-school algorithm for multiplication which consists of multiplying
the first number by each digit of the second, and then adding all the resulting terms.
From a space perspective, it is better to incrementally add the terms rather than compute all of
them individually and then add them up. The number of digits required for the product is at most
n + m for n and m digit operands, so we use an array of size n + m for lhe result.
For example, when multiplying 123 with 987,wewould forn T x123 = 861, then we would form
8x123 x10=9840,whichwewouldaddto861toget10701. Thenwewouldform9xl23xl00=
7L0700, which we would add to 10701 to get the final result 727407

'''

def multiply(num1, num2):
    
    if ((num1[0] < 0) ^ (num2[0] < 0)):
        sign = -1
    else:
        sign = 1

    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    result = [0] * (len(num1) + len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    #Remove the leading zeros
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]
    

num1 = [1,9,3,7,0,7,7,2, 1]
num2 = [-7,6,1,8,3,8,2,5,7,2,8,7]
print(num1, num2)
print(multiply(num1, num2))


            
'''
There are m paftral products, each with at most n + 1 digits. We perform O(1) operations on each
digit in each partial product, so the time complexity is O(nm).

'''
