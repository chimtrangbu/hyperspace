def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


v = int(input("Let's print the prime numbers up to? "))
for x in range(v + 1):
    if (isPrime(x)):
        print(x)
