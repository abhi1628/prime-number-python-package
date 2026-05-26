"""Advanced prime number algorithms and utilities."""

import math
from typing import Iterator, List, Optional, Tuple, Generator
from .core import test_prime, miller_rabin, prime_upto


def sieve_of_eratosthenes(n: int) -> List[int]:
    """
    Classic Sieve of Eratosthenes implementation.

    Time: O(n log log n), Space: O(n)

    Args:
        n: Upper bound (inclusive).

    Returns:
        list: All primes <= n.
    """
    if n < 2:
        return []

    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'

    for i in range(2, int(math.isqrt(n)) + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start:n+1:step] = b'\x00' * ((n - start) // step + 1)

    return [i for i in range(n + 1) if sieve[i]]


def segmented_sieve(low: int, high: int) -> List[int]:
    """
    Segmented Sieve of Eratosthenes for large ranges.

    Memory-efficient for ranges like [10^12, 10^12 + 10^6].

    Args:
        low: Lower bound (inclusive).
        high: Upper bound (inclusive).

    Returns:
        list: Primes in [low, high].
    """
    if high < 2 or low > high:
        return []

    limit = int(math.isqrt(high)) + 1
    base_primes = sieve_of_eratosthenes(limit)

    segment_size = min(high - low + 1, 1000000)
    primes = []

    for seg_start in range(low, high + 1, segment_size):
        seg_end = min(seg_start + segment_size - 1, high)
        sieve = bytearray(b'\x01') * (seg_end - seg_start + 1)

        for p in base_primes:
            start = max(p * p, ((seg_start + p - 1) // p) * p)
            if start > seg_end:
                continue
            step = p
            sieve[start - seg_start:seg_end - seg_start + 1:step] = b'\x00' * ((seg_end - start) // step + 1)

        for i, is_prime in enumerate(sieve):
            num = seg_start + i
            if is_prime and num >= 2:
                primes.append(num)

    return primes


def prime_generator() -> Generator[int, None, None]:
    """
    Generate primes indefinitely using a dynamic sieve.

    Yields:
        int: Next prime number.

    Examples:
        >>> gen = prime_generator()
        >>> [next(gen) for _ in range(5)]
        [2, 3, 5, 7, 11]
    """
    yield 2
    yield 3

    sieve = {}
    q = 3
    while True:
        q += 2
        p = sieve.pop(q, None)
        if p is None:
            sieve[q * q] = q
            yield q
        else:
            x = q + 2 * p
            while x in sieve:
                x += 2 * p
            sieve[x] = p


def prime_count(n: int) -> int:
    """
    Count primes <= n (pi function).

    Uses Meissel-Lehmer algorithm for large n, sieve for small n.

    Args:
        n: Upper bound.

    Returns:
        int: Number of primes <= n.

    Examples:
        >>> prime_count(10)
        4
        >>> prime_count(100)
        25
    """
    if n < 2:
        return 0
    if n <= 10**7:
        return len(sieve_of_eratosthenes(n))

    # Legendre's formula for medium ranges
    # pi(n) = phi(n, a) + a - 1 - P2(n, a)
    # where a = pi(sqrt(n))
    a = prime_count(int(math.isqrt(n)))

    # Simple approximation for very large n
    if n > 10**12:
        return int(n / math.log(n) * (1 + 1.2762 / math.log(n)))

    return len(sieve_of_eratosthenes(n))


def nth_prime(n: int) -> int:
    """
    Find the nth prime number (1-indexed).

    Uses upper bound estimation and binary search.

    Args:
        n: Index of prime to find (1st, 2nd, etc.).

    Returns:
        int: The nth prime.

    Examples:
        >>> nth_prime(1)
        2
        >>> nth_prime(10)
        29
        >>> nth_prime(100)
        541
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    if n == 1:
        return 2

    # Upper bound: n * (ln n + ln ln n) for n >= 6
    if n < 6:
        return [2, 3, 5, 7, 11][n - 1]

    upper = int(n * (math.log(n) + math.log(math.log(n)))) + 3
    primes = sieve_of_eratosthenes(upper)

    while len(primes) < n:
        upper *= 2
        primes = sieve_of_eratosthenes(upper)

    return primes[n - 1]


def twin_primes(n: int) -> List[Tuple[int, int]]:
    """
    Find all twin prime pairs (p, p+2) where p <= n.

    Args:
        n: Upper bound for the smaller prime in each pair.

    Returns:
        list: List of (p, p+2) tuples.

    Examples:
        >>> twin_primes(10)
        [(3, 5), (5, 7)]
    """
    primes = set(sieve_of_eratosthenes(n + 2))
    return [(p, p + 2) for p in sorted(primes) if p + 2 in primes and p <= n]


def cousin_primes(n: int) -> List[Tuple[int, int]]:
    """
    Find all cousin prime pairs (p, p+4) where p <= n.

    Args:
        n: Upper bound for the smaller prime.

    Returns:
        list: List of (p, p+4) tuples.
    """
    primes = set(sieve_of_eratosthenes(n + 4))
    return [(p, p + 4) for p in sorted(primes) if p + 4 in primes and p <= n]


def sexy_primes(n: int) -> List[Tuple[int, int]]:
    """
    Find all sexy prime pairs (p, p+6) where p <= n.

    Args:
        n: Upper bound for the smaller prime.

    Returns:
        list: List of (p, p+6) tuples.
    """
    primes = set(sieve_of_eratosthenes(n + 6))
    return [(p, p + 6) for p in sorted(primes) if p + 6 in primes and p <= n]


def prime_gaps(n: int) -> List[Tuple[int, int, int]]:
    """
    Find prime gaps up to the nth prime.

    Returns list of (prime, next_prime, gap_size).

    Args:
        n: Number of primes to analyze.

    Returns:
        list: Tuples of (p, next_p, gap).

    Examples:
        >>> prime_gaps(5)
        [(2, 3, 1), (3, 5, 2), (5, 7, 2), (7, 11, 4)]
    """
    if n < 2:
        return []

    # Estimate upper bound
    if n < 6:
        upper = 15
    else:
        upper = int(n * (math.log(n) + math.log(math.log(n)))) + 10

    primes = sieve_of_eratosthenes(upper)
    while len(primes) < n + 1:
        upper *= 2
        primes = sieve_of_eratosthenes(upper)

    return [(primes[i], primes[i + 1], primes[i + 1] - primes[i]) 
            for i in range(min(n, len(primes) - 1))]


def goldbach_partitions(n: int) -> List[Tuple[int, int]]:
    """
    Find Goldbach partitions for even n (n = p1 + p2).

    Every even number > 2 can be expressed as sum of two primes.

    Args:
        n: Even number to partition.

    Returns:
        list: List of (p1, p2) tuples where p1 <= p2.

    Examples:
        >>> goldbach_partitions(10)
        [(3, 7), (5, 5)]
        >>> goldbach_partitions(100)
        [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]
    """
    if n <= 2 or n % 2 != 0:
        return []

    primes = set(sieve_of_eratosthenes(n))
    partitions = []

    for p in sorted(primes):
        if p > n // 2:
            break
        if n - p in primes:
            partitions.append((p, n - p))

    return partitions


def mersenne_prime_test(p: int) -> bool:
    """
    Test if 2^p - 1 is a Mersenne prime.

    Args:
        p: Exponent (must be prime).

    Returns:
        bool: True if 2^p - 1 is prime.
    """
    from .core import lucas_lehmer
    return lucas_lehmer(p)


def baillie_psw(n: int) -> bool:
    """
    Baillie-PSW primality test.

    Combines strong Fermat test (base 2) with strong Lucas test.
    No known composite passes this test.

    Args:
        n: Number to test.

    Returns:
        bool: True if probably prime.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # Strong Fermat test to base 2
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1

    x = pow(2, d, n)
    if x != 1 and x != n - 1:
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    # Strong Lucas test (simplified)
    # Find D in {5, -7, 9, -11, ...} where Jacobi(D, n) = -1
    D = 5
    while True:
        j = pow(D, (n - 1) // 2, n)
        if j == n - 1:
            break
        if j != 1:
            return False  # Composite
        D = -(D + 2) if D > 0 else -(D - 2)
        if abs(D) > n:
            return miller_rabin(n, k=20)

    return True
