#Generators used to create iterators. Simple functions with return iterable set of items bit by bit in a specific way
#When an iteration over a set of item starts using the for statement. Generator is run. Once generator function hits "yield" statement
#Generate yields its execution back to the for loop, returning a new value from the set. Generator function can generate as many values need, yielding each one in its turn
#def fib(): example of the use using fibonacci sequence
    #a, b = 1, 1
    #while 1:
    #    yield a
    #    a, b = b, a + b