def sieve_of_eratosthenes(n):
    """0부터 n까지의 소수를 모두 반환"""
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

if __name__ == "__main__":
    print(sieve_of_eratosthenes(50))
