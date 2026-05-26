"""Comprehensive test suite for abhiprime."""

import pytest
import math
import abhiprime as ap


class TestBasicPrimality:
    """Tests for basic primality functions."""

    def test_small_primes(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for p in primes:
            assert ap.test_prime(p) is True

    def test_small_composites(self):
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
        for c in composites:
            assert ap.test_prime(c) is False

    def test_edge_cases(self):
        assert ap.test_prime(0) is False
        assert ap.test_prime(1) is False
        assert ap.test_prime(-5) is False

    def test_large_prime(self):
        assert ap.test_prime(104729) is True

    def test_large_composite(self):
        assert ap.test_prime(104729 * 104723) is False


class TestMillerRabin:
    """Tests for Miller-Rabin probabilistic test."""

    def test_known_primes(self):
        primes = [2, 3, 5, 7, 11, 101, 1009, 10007]
        for p in primes:
            assert ap.miller_rabin(p, k=5) is True

    def test_known_composites(self):
        composites = [4, 6, 8, 9, 15, 21, 25, 27, 121]
        for c in composites:
            assert ap.miller_rabin(c, k=5) is False

    def test_carmichael_numbers(self):
        carmichaels = [561, 1105, 1729, 2465, 2821]
        for c in carmichaels:
            assert ap.miller_rabin(c, k=10) is False


class TestLucasLehmer:
    """Tests for Mersenne prime testing."""

    def test_known_mersenne_primes(self):
        assert ap.lucas_lehmer(2) is True
        assert ap.lucas_lehmer(3) is True
        assert ap.lucas_lehmer(5) is True
        assert ap.lucas_lehmer(7) is True

    def test_known_non_mersenne(self):
        assert ap.lucas_lehmer(4) is False
        assert ap.lucas_lehmer(11) is False
        assert ap.lucas_lehmer(23) is False


class TestPrevNextPrime:
    """Tests for previous and next prime functions."""

    def test_prev_prime(self):
        assert ap.prev_prime(20) == 19
        assert ap.prev_prime(19) == 17
        assert ap.prev_prime(3) == 2
        assert ap.prev_prime(2) is None

    def test_next_prime(self):
        assert ap.next_prime(20) == 23
        assert ap.next_prime(23) == 29
        assert ap.next_prime(1) == 2
        assert ap.next_prime(2) == 3


class TestSieve:
    """Tests for sieve implementations."""

    def test_prime_upto(self):
        assert ap.prime_upto(10) == [2, 3, 5, 7]
        assert ap.prime_upto(1) == []
        assert ap.prime_upto(2) == [2]
        assert ap.prime_upto(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_range_prime(self):
        assert ap.range_prime(10, 30) == [11, 13, 17, 19, 23, 29]
        assert ap.range_prime(1, 5) == [2, 3, 5]
        assert ap.range_prime(20, 20) == []

    def test_segmented_sieve(self):
        assert ap.segmented_sieve(1, 100) == ap.sieve_of_eratosthenes(100)
        assert ap.segmented_sieve(1000, 1100) == ap.range_prime(1000, 1100)


class TestPrimeFactors:
    """Tests for prime factorization."""

    def test_basic_factorization(self):
        assert ap.prime_factors(60) == [2, 2, 3, 5]
        assert ap.prime_factors(17) == [17]
        assert ap.prime_factors(1) == []

    def test_product_check(self):
        import functools
        for n in [60, 100, 2310, 104729]:
            factors = ap.prime_factors(n)
            product = functools.reduce(lambda x, y: x * y, factors, 1)
            assert product == n


class TestAdvancedFunctions:
    """Tests for advanced prime functions."""

    def test_prime_count(self):
        assert ap.prime_count(10) == 4
        assert ap.prime_count(100) == 25
        assert ap.prime_count(1000) == 168

    def test_nth_prime(self):
        assert ap.nth_prime(1) == 2
        assert ap.nth_prime(10) == 29
        assert ap.nth_prime(25) == 97
        assert ap.nth_prime(100) == 541

    def test_twin_primes(self):
        twins = ap.twin_primes(20)
        assert (3, 5) in twins
        assert (5, 7) in twins
        assert (11, 13) in twins
        assert (17, 19) in twins

    def test_goldbach_partitions(self):
        parts = ap.goldbach_partitions(10)
        assert (3, 7) in parts
        assert (5, 5) in parts

    def test_mersenne_test(self):
        assert ap.mersenne_prime_test(3) is True
        assert ap.mersenne_prime_test(11) is False


class TestPrimeCache:
    """Tests for caching utilities."""

    def test_cache_basic(self):
        cache = ap.PrimeCache()
        assert cache.is_prime(17) is True
        assert cache.is_prime(18) is False
        assert cache.stats()["prime_cache_size"] == 2

    def test_cache_reuse(self):
        cache = ap.PrimeCache()
        cache.is_prime(17)
        cache.is_prime(17)
        assert cache.stats()["prime_cache_size"] == 1


class TestPerformance:
    """Basic performance sanity checks."""

    def test_large_range_performance(self):
        primes = ap.prime_upto(100000)
        assert len(primes) == 9592

    def test_segmented_sieve_large(self):
        primes = ap.segmented_sieve(10**6, 10**6 + 1000)
        assert len(primes) > 0
        for p in primes:
            assert ap.test_prime(p)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])