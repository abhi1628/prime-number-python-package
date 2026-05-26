"""Performance benchmarks for abhiprime."""

import time
import sys
from typing import Callable, List, Tuple

from abhiprime import (
    test_prime, prime_upto, range_prime, prime_count,
    nth_prime, segmented_sieve, miller_rabin
)


def benchmark(func: Callable, *args, iterations: int = 1) -> Tuple[float, any]:
    """Benchmark a function call."""
    start = time.perf_counter()
    result = None
    for _ in range(iterations):
        result = func(*args)
    elapsed = time.perf_counter() - start
    return elapsed, result


def run_benchmarks():
    """Run all benchmarks and print results."""
    print("=" * 60)
    print("abhiprime v2.0.0 Performance Benchmarks")
    print("=" * 60)
    print(f"Python: {sys.version}")
    print()

    benchmarks = [
        ("prime_upto(10^4)", lambda: prime_upto(10000), 10),
        ("prime_upto(10^5)", lambda: prime_upto(100000), 5),
        ("prime_upto(10^6)", lambda: prime_upto(1000000), 3),
        ("test_prime(10^6+3)", lambda: test_prime(1000003), 1000),
        ("test_prime(10^12+39)", lambda: test_prime(10**12 + 39), 100),
        ("miller_rabin(10^18+3)", lambda: miller_rabin(10**18 + 3), 50),
        ("nth_prime(1000)", lambda: nth_prime(1000), 10),
        ("nth_prime(10000)", lambda: nth_prime(10000), 5),
        ("prime_count(10^6)", lambda: prime_count(1000000), 5),
        ("segmented_sieve(10^8, 10^8+1000)", lambda: segmented_sieve(10**8, 10**8 + 1000), 10),
    ]

    print(f"{'Benchmark':<45} {'Time (ms)':<12} {'Result':<20}")
    print("-" * 77)

    for name, func, iterations in benchmarks:
        try:
            elapsed, result = benchmark(func, iterations=iterations)
            avg_time = (elapsed / iterations) * 1000  # ms

            if isinstance(result, list):
                result_str = f"[{len(result)} items]"
            else:
                result_str = str(result)[:20]

            print(f"{name:<45} {avg_time:>10.3f} ms  {result_str:<20}")
        except Exception as e:
            print(f"{name:<45} {'ERROR':<12} {str(e)[:20]:<20}")

    print()
    print("=" * 60)


if __name__ == "__main__":
    run_benchmarks()
