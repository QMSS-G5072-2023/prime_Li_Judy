from prime_pl2889 import prime_pl2889

import pytest

@pytpyest.mark.parametrize("example, expected", [
        (0, False),
        (1, True),
        (-2, False),
        (3, True),
        (4, False),
        (7, True),
        (5, True),
        (9, False)
])
def test_is_prime_param(example, expected):
        result = is_prime(example)
        assert result == expected,f'For number {example}, expected prime={expected}'
