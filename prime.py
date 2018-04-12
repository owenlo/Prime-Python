"""Prime number generator."""

import math


def gen_prime(start, end):
    """Generate and return a list of prime numbers based on a specified range.

    Keyword arguments:
    start -- the starting range (inclusive)
    end --- the ending range (exclusive)
    """
    if start <= 0 or end <= 0:
        raise Exception("Start and end values must be greater than zero.")

    if start >= end:
        raise Exception("The start value cannot be greater than or equal to the end value")

    prime_list = []

    for prime in range(start, end):
        if is_prime(prime):
            prime_list.append(prime)
    return prime_list


def is_prime(number):
    """Returns true if number is prime else returns false."""
    if number == 0 or number == 1:
        return False

    isprime = True
    for test in range(2, int(math.sqrt(number) + 1)):  # +1 since we have to test up to the square root value
        if number % test == 0:
            isprime = False
            break
    return isprime


def main():
    """Example usage. Generates prime numbers in the specified range."""
    prime = gen_prime(1, 100000)
    print(prime)


if __name__ == "__main__":
    main()
