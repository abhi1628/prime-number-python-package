"""Core prime number algorithms with type hints and optimizations."""

import math
import random
from functools import lru_cache
from typing import List, Optional, Tuple


def test_prime(n: int) -> bool:
    """
    Efficiently test if a number is prime.

    Uses trial division for small numbers (< 10^12) and 
    Miller-Rabin for larger numbers.

    Args:
        n: Integer to test for primality.

    Returns:
        bool: True if n is prime, False otherwise.

    Examples:
        >>> test_prime(17)
        True
        >>> test_prime(18)
        False
        >>> test_prime(1)
        False
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # For large numbers, use Miller-Rabin
    if n > 10**12:
        return miller_rabin(n)

    # Trial division with 6k ± 1 optimization
    limit = int(math.isqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def is_prime_optimized(n: int) -> bool:
    """Alias for test_prime with full optimizations."""
    return test_prime(n)


@lru_cache(maxsize=10000)
def _cached_test_prime(n: int) -> bool:
    """Cached version for repeated queries."""
    return test_prime(n)


def miller_rabin(n: int, k: int = 10) -> bool:
    """
    Miller-Rabin primality test (probabilistic).

    Error probability < 4^(-k). For k=10, error < 0.0001%.

    Args:
        n: Number to test.
        k: Number of witness rounds (default 10).

    Returns:
        bool: True if probably prime, False if definitely composite.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def is_probable_prime(n: int) -> bool:
    """Alias for miller_rabin with k=10."""
    return miller_rabin(n, k=10)


def lucas_lehmer(p: int) -> bool:
    """
    Lucas-Lehmer test for Mersenne primes.

    Tests if 2^p - 1 is prime (requires p to be prime).

    Args:
        p: Exponent (must be prime).

    Returns:
        bool: True if 2^p - 1 is prime.

    Examples:
        >>> lucas_lehmer(3)  # 2^3 - 1 = 7 is prime
        True
        >>> lucas_lehmer(11)  # 2^11 - 1 = 2047 = 23 * 89
        False
    """
    if not test_prime(p):
        return False
    if p == 2:
        return True

    mersenne = (1 << p) - 1  # 2^p - 1
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % mersenne
    return s == 0


def prev_prime(n: int) -> Optional[int]:
    if n <= 2:
        return None
    if n == 3:
        return 2
    candidate = n - 1 if n % 2 == 0 else n - 2
    while candidate >= 2:
        if test_prime(candidate):
            return candidate
        candidate -= 2
    return None


def next_prime(n: int) -> int:
    """
    Find the smallest prime strictly greater than n.

    Args:
        n: Lower bound (exclusive).

    Returns:
        int: Next prime number.

    Examples:
        >>> next_prime(20)
        23
        >>> next_prime(17)
        19
    """
    if n < 2:
        return 2
    candidate = n + 1 if n % 2 == 0 else n + 2
    while True:
        if test_prime(candidate):
            return candidate
        candidate += 2


def prime_upto(n: int) -> List[int]:
    """
    Get all prime numbers up to and including n.

    Uses Sieve of Eratosthenes for efficiency.

    Args:
        n: Upper bound (inclusive).

    Returns:
        list: All primes <= n.

    Examples:
        >>> prime_upto(10)
        [2, 3, 5, 7]
        >>> prime_upto(1)
        []
    """
    if n < 2:
        return []

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.isqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return [i for i, is_p in enumerate(sieve) if is_p]


def range_prime(start: int, end: int) -> List[int]:
    """
    Get all primes in the range [start, end].

    Args:
        start: Lower bound (inclusive).
        end: Upper bound (inclusive).

    Returns:
        list: Primes in the specified range.

    Examples:
        >>> range_prime(10, 30)
        [11, 13, 17, 19, 23, 29]
    """
    if start > end or end < 2:
        return []

    # For small ranges relative to end, use segmented sieve
    if end > 10**6 and (end - start) < end // 10:
        from .advanced import segmented_sieve
        return segmented_sieve(start, end)

    # Otherwise use standard sieve
    primes = prime_upto(end)
    idx = 0
    while idx < len(primes) and primes[idx] < start:
        idx += 1
    return primes[idx:]


def prime_factors(n: int) -> List[int]:
    """
    Get all prime factors of n with multiplicity.

    Args:
        n: Number to factorize.

    Returns:
        list: Prime factors in ascending order.

    Examples:
        >>> prime_factors(60)
        [2, 2, 3, 5]
        >>> prime_factors(17)
        [17]
        >>> prime_factors(1)
        []
    """
    if n < 2:
        return []

    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1 if d == 2 else 2  # Skip even numbers after 2

    if n > 1:
        factors.append(n)
    return factors


def _is_perfect_square(n: int) -> bool:
    """Check if n is a perfect square."""
    root = int(math.isqrt(n))
    return root * root == n


def fib_prime(n: int) -> List[int]:
    """
    Get Fibonacci numbers that are also prime, up to the nth Fibonacci number.

    Note: Only F(4)=3, F(5)=5, F(7)=13, F(11)=89, F(13)=233, F(17)=1597,
    F(19)=4181, F(23)=28657, F(29)=514229 are known prime Fibonacci numbers.

    Args:
        n: Index limit for Fibonacci sequence.

    Returns:
        list: Prime Fibonacci numbers.

    Examples:
        >>> fib_prime(10)
        [2, 3, 5, 13]
    """
    if n < 1:
        return []

    fibs = [0, 1]
    for _ in range(2, n + 1):
        fibs.append(fibs[-1] + fibs[-2])

    return [f for f in fibs[2:] if test_prime(f)]
