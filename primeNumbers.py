def primeNumbers(num):
    try:
        prime = []
        if num > 2:
            for i in range(2, num + 1):
                if num % i != 0:
                    prime.append(i)

        return prime

    except TypeError as e:
        raise TypeError("Handling run-time erroe %s") % e

