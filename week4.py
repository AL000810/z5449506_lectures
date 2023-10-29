
def qan_tic():
        tic = "EST.AX"
        print(tic)
        return tic

tic = "WES.AX"
print(tic)
qan_tic()

def f(num):
    e_num = []
    i = 0
    while i < len(num):
#   for n in num:
        if num[i] % 2 == 0:
            e_num.append(num[i])
        i += 1  # Increment i to avoid an infinite loop
    return e_num

test = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]
result = f(test)
print(result)


# Create a list with all even integers from 0 to 1 million
evens = []
for x in range(1_000_000 +1):
    if x % 2 == 0:
        evens.append(x)
print(evens[:10])

evens = [x for x in range(1_000_000+1) if x % 2 == 0]
print(evens)

# Using a for loop to create a dictionary to list
dic = {'a': 1, 'b': 2, 'c': 3}
pairs = [(key, value) for key, value in dic.items()]
print(pairs)

#Dic to set
dic = {'a': 1, 'b': 2, 'c': 3}
keys = {key for key in dic}
print(f'The type of {keys} is {type(keys)}')

# List to Dic
# Sample list of items
my_list = [("a", 1), ("b", 2), ("c", 3)]

# Create a dictionary from the list using a comprehension
my_dict = {key: value for key, value in my_list}

print(my_dict)

# ex2
lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]

sq_lst = [x**2 for x in lst if x**2 > 150]
print(sq_lst)

# ex 3
numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
new_lst = set(numbers)
lst_1 = [x for x in new_lst if x%2 == 0]
lst_1.sort()
print(lst_1)


