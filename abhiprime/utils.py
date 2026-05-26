"""Utility classes and helper functions."""

import math
from typing import Dict, List, Optional, Set
from functools import lru_cache


class PrimeCache:
    """
    LRU cache for prime-related computations.

    Useful for repeated queries in the same session.

    Examples:
        >>> cache = PrimeCache()
        >>> cache.is_prime(17)
        True
        >>> cache.prime_upto(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
    """

    def __init__(self, maxsize: int = 10000):
        self._prime_cache: Dict[int, bool] = {}
        self._sieve_cache: Dict[int, List[int]] = {}
        self.maxsize = maxsize

    def is_prime(self, n: int) -> bool:
        """Cached primality test."""
        if n in self._prime_cache:
            return self._prime_cache[n]
        from .core import test_prime
        result = test_prime(n)
        self._prime_cache[n] = result
        self._cleanup()
        return result

    def prime_upto(self, n: int) -> List[int]:
        """Cached sieve results."""
        if n in self._sieve_cache:
            return self._sieve_cache[n]
        from .advanced import sieve_of_eratosthenes
        result = sieve_of_eratosthenes(n)
        self._sieve_cache[n] = result
        self._cleanup()
        return result

    def _cleanup(self):
        """Remove old entries if cache exceeds maxsize."""
        while len(self._prime_cache) > self.maxsize:
            self._prime_cache.pop(next(iter(self._prime_cache)))
        while len(self._sieve_cache) > self.maxsize // 10:
            self._sieve_cache.pop(next(iter(self._sieve_cache)))

    def clear(self):
        """Clear all caches."""
        self._prime_cache.clear()
        self._sieve_cache.clear()

    def stats(self) -> Dict[str, int]:
        """Return cache statistics."""
        return {
            "prime_cache_size": len(self._prime_cache),
            "sieve_cache_size": len(self._sieve_cache),
        }


def is_prime_optimized(n: int) -> bool:
    """Optimized primality test with early exits."""
    if n < 2:
        return False
    if n in (2, 3, 5):
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False

    # Check 6k ± 1 up to sqrt(n)
    limit = int(math.isqrt(n)) + 1
    i = 5
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sieve_of_eratosthenes(n: int) -> List[int]:
    """Memory-optimized sieve using bytearray."""
    if n < 2:
        return []

    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'

    for i in range(2, int(math.isqrt(n)) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = b'\x00' * ((n - i*i) // i + 1)

    return [i for i in range(n + 1) if sieve[i]]
