for i in range(1,101):
    s = ""
    if not i%3:
        s += 'Fizz'
    if not i%5:
        s += 'Buzz'
    print(s or i)
