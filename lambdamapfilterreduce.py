def square_it(number):
    return number ** 2

# LAMBDA FUNCTIONS
first = lambda x: 2 * x
second = lambda x, y: x + y
third = lambda x,y: x if x > y else y

print(first(3))
print(second(3,2))
print(third(1,2))

# MAP -- APPLY SAME FUNCTION TO EACH ELEMENT OF A SEQUENCE
# RETURN MODIFIED LIST

numbers = [4,3,2,1]

def square_not_map(lst1):
    lst2 = []
    for num in lst1:
        lst2.append(num ** 2)
    return lst2

print(square_not_map(numbers))

# THIS IS EQUAL TO.....

print (list(map(lambda x: x**2, numbers)))

#DOESN'T NEED TO BE A LAMBDA FUNCTION
print (list(map(square_it, numbers)))


# FILTER FUNCTION
# FILTERS OUT ITEMS IN SEQUENCE
n = [4,3,2,1]
def over_two(lst1):
    lst2 = [x for x in lst1 if x > 2]
    return lst2

print(over_two(n))

#SAME AS...

print(list(filter(lambda x: x > 2, n)))

# REDUCE
# APPLIES SAME OPERATION TO ITEMS OF A SEQUENCE
# USES RESULT OF OPERATION AS FIRST PARAM OF NEXT OPERATION
# RETURNS AN ITEM, NOT A LIST

def mult(lst1):
    prod = lst1[0]
    for i in range(1,len(lst1)):
        prod *= lst1[i]
    return prod
print(mult(n))

# SAME AS...

print(reduce(lambda x,y: x*y, n))
