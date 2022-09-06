# Smallest (excluding whitespace)
for i in range(1, 101):
    print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i)

# Without using the modulo operator
v = 810092048
for i in range(1,101):
    j = v & 3
    v = v >> 2 | j << 28
    w = i, "Fizz", "Buzz", "FizzBuzz"
    print(w[j])
