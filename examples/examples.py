"""Examples of using abhiprime v2."""

import abhiprime as ap

# =============================================================================
# BASIC PRIMALITY TESTING
# =============================================================================

print("=== Basic Primality Testing ===")
print(f"Is 17 prime? {ap.test_prime(17)}")
print(f"Is 100 prime? {ap.test_prime(100)}")
print(f"Is 104729 (10000th prime) prime? {ap.test_prime(104729)}")
print()

# =============================================================================
# FINDING PRIMES
# =============================================================================

print("=== Finding Primes ===")
print(f"Previous prime before 100: {ap.prev_prime(100)}")
print(f"Next prime after 100: {ap.next_prime(100)}")
print(f"Primes up to 50: {ap.prime_upto(50)}")
print(f"Primes between 10 and 30: {ap.range_prime(10, 30)}")
print()

# =============================================================================
# PRIME FACTORIZATION
# =============================================================================

print("=== Prime Factorization ===")
n = 360
factors = ap.prime_factors(n)
print(f"Prime factors of {n}: {factors}")
print(f"Verification: {' × '.join(map(str, factors))} = {eval('*'.join(map(str, factors)))}")
print()

# =============================================================================
# ADVANCED: LARGE NUMBER TESTING
# =============================================================================

print("=== Large Number Testing ===")
large_prime = 10**12 + 39
print(f"Is {large_prime} prime? {ap.miller_rabin(large_prime)}")
print()

# =============================================================================
# ADVANCED: PRIME COUNTING
# =============================================================================

print("=== Prime Counting Function π(n) ===")
for n in [10, 100, 1000, 10000]:
    count = ap.prime_count(n)
    print(f"π({n}) = {count}")
print()

# =============================================================================
# ADVANCED: NTH PRIME
# =============================================================================

print("=== Nth Prime ===")
for n in [1, 10, 100, 1000]:
    p = ap.nth_prime(n)
    print(f"Prime #{n} = {p}")
print()

# =============================================================================
# ADVANCED: SPECIAL PRIME PAIRS
# =============================================================================

print("=== Special Prime Pairs ===")
print(f"Twin primes up to 50: {ap.twin_primes(50)}")
print(f"Cousin primes up to 50: {ap.cousin_primes(50)}")
print(f"Sexy primes up to 50: {ap.sexy_primes(50)}")
print()

# =============================================================================
# ADVANCED: GOLDBACH PARTITIONS
# =============================================================================

print("=== Goldbach Partitions ===")
n = 100
partitions = ap.goldbach_partitions(n)
print(f"Goldbach partitions of {n}:")
for p1, p2 in partitions:
    print(f"  {p1} + {p2} = {n}")
print()

# =============================================================================
# ADVANCED: MERSENNE PRIMES
# =============================================================================

print("=== Mersenne Primes ===")
for p in [2, 3, 5, 7, 13, 17, 19]:
    mersenne = 2**p - 1
    is_prime = ap.mersenne_prime_test(p)
    status = "✓ PRIME" if is_prime else "✗ Composite"
    print(f"2^{p} - 1 = {mersenne} → {status}")
print()

# =============================================================================
# ADVANCED: SEGMENTED SIEVE (Memory Efficient)
# =============================================================================

print("=== Segmented Sieve ===")
# Find primes in a huge range without loading all primes up to 10^12
primes = ap.segmented_sieve(10**12, 10**12 + 100)
print(f"Primes between 10^12 and 10^12+100: {primes}")
print()

# =============================================================================
# ADVANCED: CACHING
# =============================================================================

print("=== Caching ===")
cache = ap.PrimeCache(maxsize=1000)

# First call computes
result1 = cache.is_prime(104729)
print(f"First call: {result1}")

# Second call uses cache (instant)
result2 = cache.is_prime(104729)
print(f"Cached call: {result2}")

print(f"Cache stats: {cache.stats()}")
print()

# =============================================================================
# ADVANCED: GENERATOR (Memory Efficient)
# =============================================================================

print("=== Prime Generator ===")
gen = ap.prime_generator()
first_20 = [next(gen) for _ in range(20)]
print(f"First 20 primes: {first_20}")
print()

# =============================================================================
# FIBONACCI PRIMES
# =============================================================================

print("=== Fibonacci Primes ===")
fib_primes = ap.fib_prime(30)
print(f"Prime Fibonacci numbers up to F(30): {fib_primes}")
