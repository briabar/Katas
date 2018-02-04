def SumFunc(num):
    '''Take in integer i and return sum of all multiples of 3 and 5 below it'''
    answer = 0
    for i in range(0,num):
        if i % 3 == 0 or i % 5 == 0:
            answer += i
    return answer

print(SumFunc(1000))
