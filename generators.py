# GENERATORS

def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1,2,3,4,5])

print(my_nums)


def square_numbers2(nums):
    for i in nums:
        yield (i*i)


my_nums = square_numbers2([1,2,3,4,5])

print(my_nums)
print("using next(my_nums)")
print(next(my_nums))

print(next(my_nums))

print(next(my_nums))

print(next(my_nums))

print(next(my_nums))

# THROWS A StopIteration EXCEPTION
# print(next(my_nums))

my_nums = square_numbers2([1,2,3,4,5])

for num in my_nums:
    print("generator object in for loop")
    print(num)

# THIS WILL INSTANTIATE A GENERATOR OBJECT USING LIST COMPREHENSION

my_nums = (x*x for x in [1,2,3,4,5]) # NOTICE IT USES PARANTHESIS RATHER THAN [] BRACKETS

for num in my_nums:
    print("list comprehension")
    print(num)
