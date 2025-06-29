#练习1
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(1, 101) if is_prime(n)]
print("1到100之间的素数：", primes)

#练习2
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence[:n]

print("斐波那契数列的前20项：", fibonacci(20))

#练习3
total = 0
number = 1
while number <= 10000:
    if (number % 3 == 0 or number % 5 == 0) and number % 15 != 0:
        total += number
    number += 1

print("1-10000之间符合条件的数的和为：", total)