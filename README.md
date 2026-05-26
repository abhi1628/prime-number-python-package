# 🔢 abhiprime

[![PyPI version](https://badge.fury.io/py/abhiprime.svg)](https://pypi.org/project/abhiprime/)
[![Python versions](https://img.shields.io/pypi/pyversions/abhiprime.svg)](https://pypi.org/project/abhiprime/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/abhi1628/prime-number-python-package/actions/workflows/ci.yml/badge.svg)](https://github.com/abhi1628/prime-number-python-package/actions)
[![codecov](https://codecov.io/gh/abhi1628/prime-number-python-package/branch/main/graph/badge.svg)](https://codecov.io/gh/abhi1628/prime-number-python-package)

> A powerful, efficient, and comprehensive Python package for prime number operations.

## ✨ Features

- **🔍 Primality Testing**: Trial division + Miller-Rabin for all number sizes
- **⚡ High Performance**: Sieve of Eratosthenes (standard & segmented)
- **🎯 Advanced Algorithms**: Lucas-Lehmer, Baillie-PSW, prime counting
- **📊 Mathematical Functions**: Twin primes, Goldbach partitions, prime gaps
- **🚀 CLI Tool**: Command-line interface for quick operations
- **💾 Smart Caching**: LRU cache for repeated queries
- **📝 Type Hints**: Full type annotation support
- **🧪 Well Tested**: Comprehensive test suite with >95% coverage

## 📦 Installation

```bash
pip install abhiprime
```

Upgrade from v1:
```bash
pip install --upgrade abhiprime
```

## 🚀 Quick Start

### Basic Usage

```python
import abhiprime as ap

# Test primality
ap.test_prime(17)        # True
ap.test_prime(18)        # False

# Find nearby primes
ap.prev_prime(20)        # 19
ap.next_prime(20)        # 23

# Get primes in range
ap.prime_upto(50)        # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
ap.range_prime(10, 30)   # [11, 13, 17, 19, 23, 29]

# Prime factorization
ap.prime_factors(60)     # [2, 2, 3, 5]
```

### Advanced Features

```python
from abhiprime import (
    prime_count, nth_prime, twin_primes, 
    goldbach_partitions, segmented_sieve, PrimeCache
)

# Prime counting function π(n)
prime_count(100)         # 25
prime_count(1000)        # 168

# Find the nth prime
nth_prime(100)           # 541
nth_prime(10000)         # 104729

# Special prime pairs
twin_primes(50)          # [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)]
cousin_primes(50)        # [(3, 7), (7, 11), (13, 17), (19, 23), (37, 41), (43, 47)]
sexy_primes(50)          # [(5, 11), (7, 13), (11, 17), (13, 19), (17, 23), ...]

# Goldbach partitions
goldbach_partitions(100) # [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]

# Memory-efficient segmented sieve for large ranges
segmented_sieve(10**12, 10**12 + 1000)

# Caching for repeated operations
cache = PrimeCache(maxsize=10000)
cache.is_prime(104729)   # Cached result
cache.stats()            # {'prime_cache_size': 1, 'sieve_cache_size': 0}
```

### Large Number Support

```python
from abhiprime import miller_rabin, baillie_psw, lucas_lehmer

# Probabilistic test for large numbers (cryptography-grade)
miller_rabin(2**61 - 1, k=20)  # True (Mersenne prime)

# Baillie-PSW (no known counterexamples)
baillie_psw(3825123056546413051)

# Lucas-Lehmer for Mersenne primes
lucas_lehmer(127)  # True (2^127 - 1 is prime)
```

## 🖥️ Command Line Interface

```bash
# Test if a number is prime
abhiprime test 17
# Output: 17 is prime

# Get primes up to n
abhiprime upto 50
# Output: Found 15 primes
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Prime factorization
abhiprime factors 60
# Output: Prime factors of 60: [2, 2, 3, 5]

# Count primes
abhiprime count 1000
# Output: π(1000) = 168

# Find nth prime
abhiprime nth 100
# Output: Prime #100 = 541

# Twin primes
abhiprime twins 100
# Output: Found 8 pairs
#   (3, 5)
#   (5, 7)
#   ...

# Goldbach partitions
abhiprime goldbach 100
# Output: Goldbach partitions of 100:
#   3 + 97 = 100
#   11 + 89 = 100
#   ...

# JSON output
abhiprime --format json upto 20
# Output: {"upper_bound": 20, "count": 8, "primes": [2, 3, 5, 7, 11, 13, 17, 19]}
```

## 📊 Performance Comparison

| Operation | abhiprime v2 | abhiprime v1 | sympy |
|-----------|-------------|-------------|-------|
| `prime_upto(10^6)` | 0.05s | 2.3s | 0.08s |
| `prime_upto(10^8)` | 4.2s | N/A | 5.1s |
| `test_prime(10^18)` | 0.001s | 0.8s | 0.002s |
| `nth_prime(10^6)` | 0.3s | N/A | 0.4s |

*Benchmarks on Intel i7, Python 3.11*

## 🔧 API Reference

### Core Functions

| Function | Description | Time Complexity |
|----------|-------------|-----------------|
| `test_prime(n)` | Primality test | O(√n) small, O(k·log³n) large |
| `prev_prime(n)` | Largest prime < n | O(√n · gap) |
| `next_prime(n)` | Smallest prime > n | O(√n · gap) |
| `prime_upto(n)` | All primes ≤ n | O(n log log n) |
| `range_prime(a, b)` | Primes in [a, b] | O(n log log n) |
| `prime_factors(n)` | Prime factorization | O(√n) |

### Advanced Functions

| Function | Description |
|----------|-------------|
| `miller_rabin(n, k=10)` | Probabilistic primality test |
| `lucas_lehmer(p)` | Mersenne prime test |
| `baillie_psw(n)` | Deterministic probable prime test |
| `prime_count(n)` | Count primes ≤ n |
| `nth_prime(n)` | Find the nth prime |
| `twin_primes(n)` | Find twin prime pairs |
| `goldbach_partitions(n)` | Even number as sum of two primes |
| `segmented_sieve(low, high)` | Memory-efficient large range sieve |
| `prime_generator()` | Infinite prime generator |

## 🧪 Running Tests

```bash
# Clone the repository
git clone https://github.com/abhi1628/prime-number-python-package.git
cd prime-number-python-package

# Install dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/ -v --cov=abhiprime

# Run benchmarks
python benchmarks/benchmark.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Sieve of Eratosthenes implementation optimized with `bytearray`
- Miller-Rabin implementation based on deterministic variants
- Inspired by `sympy.ntheory` and `primesieve`

---

**⭐ Star this repo if you find it useful!**
