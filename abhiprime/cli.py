"""Command-line interface for abhiprime."""

import argparse
import json
import sys
from typing import List

from .core import test_prime, prev_prime, next_prime, prime_factors, fib_prime
from .advanced import (
    prime_upto, range_prime, prime_count, nth_prime,
    twin_primes, cousin_primes, sexy_primes, prime_gaps,
    goldbach_partitions, mersenne_prime_test, segmented_sieve,
)


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="abhiprime - Powerful Prime Number Toolkit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  abhiprime test 17                    # Test if 17 is prime
  abhiprime upto 100                   # Primes up to 100
  abhiprime range 10 50                # Primes between 10 and 50
  abhiprime factors 60                 # Prime factorization of 60
  abhiprime count 1000                 # Count primes <= 1000
  abhiprime nth 100                    # 100th prime
  abhiprime twins 100                  # Twin primes up to 100
  abhiprime goldbach 100               # Goldbach partitions of 100
  abhiprime --format json upto 50      # Output as JSON
        """
    )

    parser.add_argument("command", choices=[
        "test", "prev", "next", "upto", "range", "factors",
        "count", "nth", "twins", "cousins", "sexy", "gaps",
        "goldbach", "mersenne", "fibprime"
    ], help="Command to execute")

    parser.add_argument("numbers", nargs="+", type=int, help="Input number(s)")
    parser.add_argument("--format", choices=["plain", "json"], default="plain",
                       help="Output format")
    parser.add_argument("--version", action="version", version="abhiprime 2.0.0")

    args = parser.parse_args()

    result = execute_command(args.command, args.numbers)

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(format_plain(result, args.command))


def execute_command(command: str, numbers: List[int]):
    """Execute the requested command."""
    if command == "test":
        n = numbers[0]
        return {"number": n, "is_prime": test_prime(n)}

    elif command == "prev":
        n = numbers[0]
        p = prev_prime(n)
        return {"number": n, "previous_prime": p}

    elif command == "next":
        n = numbers[0]
        return {"number": n, "next_prime": next_prime(n)}

    elif command == "upto":
        n = numbers[0]
        primes = prime_upto(n)
        return {"upper_bound": n, "count": len(primes), "primes": primes}

    elif command == "range":
        start, end = numbers[0], numbers[1]
        primes = range_prime(start, end)
        return {"range": [start, end], "count": len(primes), "primes": primes}

    elif command == "factors":
        n = numbers[0]
        factors = prime_factors(n)
        return {"number": n, "factors": factors, "unique_factors": list(dict.fromkeys(factors))}

    elif command == "count":
        n = numbers[0]
        return {"upper_bound": n, "prime_count": prime_count(n)}

    elif command == "nth":
        n = numbers[0]
        return {"index": n, "prime": nth_prime(n)}

    elif command == "twins":
        n = numbers[0]
        pairs = twin_primes(n)
        return {"upper_bound": n, "count": len(pairs), "pairs": pairs}

    elif command == "cousins":
        n = numbers[0]
        pairs = cousin_primes(n)
        return {"upper_bound": n, "count": len(pairs), "pairs": pairs}

    elif command == "sexy":
        n = numbers[0]
        pairs = sexy_primes(n)
        return {"upper_bound": n, "count": len(pairs), "pairs": pairs}

    elif command == "gaps":
        n = numbers[0]
        gaps = prime_gaps(n)
        return {"num_primes": n, "gaps": gaps}

    elif command == "goldbach":
        n = numbers[0]
        parts = goldbach_partitions(n)
        return {"number": n, "partitions": parts, "count": len(parts)}

    elif command == "mersenne":
        p = numbers[0]
        is_mersenne = mersenne_prime_test(p)
        mersenne_num = (1 << p) - 1
        return {"exponent": p, "mersenne_number": mersenne_num, "is_prime": is_mersenne}

    elif command == "fibprime":
        n = numbers[0]
        primes = fib_prime(n)
        return {"fib_limit": n, "prime_fibonacci": primes}

    return {}


def format_plain(result: dict, command: str) -> str:
    """Format result as plain text."""
    lines = []

    if command == "test":
        status = "is" if result["is_prime"] else "is not"
        lines.append(f"{result['number']} {status} prime")

    elif command == "prev":
        p = result["previous_prime"]
        lines.append(f"Previous prime before {result['number']}: {p if p else 'None'}")

    elif command == "next":
        lines.append(f"Next prime after {result['number']}: {result['next_prime']}")

    elif command in ("upto", "range"):
        lines.append(f"Found {result['count']} primes")
        lines.append(str(result['primes']))

    elif command == "factors":
        lines.append(f"Prime factors of {result['number']}: {result['factors']}")
        lines.append(f"Unique factors: {result['unique_factors']}")

    elif command == "count":
        lines.append(f"π({result['upper_bound']}) = {result['prime_count']}")

    elif command == "nth":
        lines.append(f"Prime #{result['index']} = {result['prime']}")

    elif command in ("twins", "cousins", "sexy"):
        lines.append(f"Found {result['count']} pairs")
        for p1, p2 in result['pairs']:
            lines.append(f"  ({p1}, {p2})")

    elif command == "gaps":
        for p1, p2, gap in result['gaps']:
            lines.append(f"  Gap {gap} between {p1} and {p2}")

    elif command == "goldbach":
        lines.append(f"Goldbach partitions of {result['number']}:")
        for p1, p2 in result['partitions']:
            lines.append(f"  {p1} + {p2} = {result['number']}")

    elif command == "mersenne":
        status = "is" if result["is_prime"] else "is not"
        lines.append(f"2^{result['exponent']} - 1 = {result['mersenne_number']} {status} prime")

    elif command == "fibprime":
        lines.append(f"Prime Fibonacci numbers: {result['prime_fibonacci']}")

    return "\n".join(lines)


if __name__ == "__main__":
    main()
