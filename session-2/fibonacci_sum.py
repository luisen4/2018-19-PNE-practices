import fibonacci

n = int(input("Please enter the number of terms you want to sum up: "))


sum = 0
while n > 0:
    add = fibonacci.fibonacci(n)
    sum += add
    n += -1

print("The result is: ", sum)