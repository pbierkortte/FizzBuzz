# Shortest (ignoring whitespace)
for i in range(100):
    print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i + 1)

# Without using the modulo operator
v = 810092048
for i in range(100):
    j = v & 3
    v = v >> 2 | j << 28
    w = (i + 1, "Fizz", "Buzz", "FizzBuzz")
    print(w[j])
