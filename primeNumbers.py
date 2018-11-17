def primeNumbers(num):
    if type(num) == int and num > 1:
        for i in range(2, num):
            if num % i == 0:
                return ("%d is not a prime number") % (num)
            else:
                return ("%d is a prime number") % (num)
    else:
        return "Unexpected Input"
