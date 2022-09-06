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

# Without using the modulo or bitwise operators
fizz = 0,0,1
buzz = 0,0,0,0,1
for idx in range(100):
    fizz, buzz = fizz[1:] + fizz[:1], buzz[1:] + buzz[:1]
    print("Fizz" * fizz[-1] + "Buzz" * buzz[-1] or idx + 1)
