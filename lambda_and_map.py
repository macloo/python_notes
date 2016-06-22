# start with insanely simple function that takes 2 args and returns sum
def add_nums(n1, n2):
    result = n1 + n2
    return result

print add_nums(3, 6)

# lambda
# Small anonymous functions can be created with the lambda keyword.
# They are syntactically restricted to a single expression.
# stuff below does same as stuff above

quickie_result = lambda n1, n2:n1 + n2
print quickie_result(6, 9)

# map()
# There are three built-in functions that are very useful when used with lists:
# filter(), map(), and reduce().
# map(function, sequence) calls function(item) for each of the sequence's items
# and returns a list of the return values.
# here we will see how map works with lambda

mappy_result = map( lambda x:x * 2, [1, 1, 2, 3, 5, 8] )
print mappy_result

# more map()
# now here's the same map with a separate function instead of lambda and
# with a separate list too

def times_two(x):
    result = x * 2
    return result

my_list = [13, 21, 34, 55]

print map(times_two, my_list)

# so that might be a more normal occurence of map() but the previous example
# combining lambda and map could come in handy
# note how with map() the function name is not followed by parens

# map() can also be used with a range

print map(times_two, range(1, 6))
