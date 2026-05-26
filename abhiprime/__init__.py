"""
abhiprime - A powerful Python package for prime number operations.

Features:
- Basic primality testing (trial division + Miller-Rabin)
- Sieve of Eratosthenes (standard + segmented)
- Prime generators (lazy evaluation)
- Prime counting, nth prime, twin primes
- Prime factorization
- Fibonacci primes
- Goldbach partitions
- Prime gaps analysis
- CLI interface
"""

__version__ = "7.0.0"
__author__ = "abhi1628"

from .core import (
    test_prime,
    prev_prime,
    next_prime,
    prime_upto,
    range_prime,
    prime_factors,
    fib_prime,
    is_probable_prime,
    miller_rabin,
    lucas_lehmer,
)
from .advanced import (
    prime_count,
    nth_prime,
    twin_primes,
    cousin_primes,
    sexy_primes,
    prime_gaps,
    goldbach_partitions,
    mersenne_prime_test,
    baillie_psw,
    prime_generator,
    segmented_sieve,
)
from .utils import (
    sieve_of_eratosthenes,
    is_prime_optimized,
    PrimeCache,
)

__all__ = [
    "test_prime",
    "prev_prime",
    "next_prime",
    "prime_upto",
    "range_prime",
    "prime_factors",
    "fib_prime",
    "is_probable_prime",
    "miller_rabin",
    "lucas_lehmer",
    "prime_count",
    "nth_prime",
    "twin_primes",
    "cousin_primes",
    "sexy_primes",
    "prime_gaps",
    "goldbach_partitions",
    "mersenne_prime_test",
    "baillie_psw",
    "prime_generator",
    "segmented_sieve",
    "sieve_of_eratosthenes",
    "is_prime_optimized",
    "PrimeCache",
]
