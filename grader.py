"""Assignment grader."""

from copy import copy
import sys

from solution import Solution  # pylint: disable=E0401


def read_test_case():
    """Read test case from STDIN and return parsed list."""
    return [int(x) for x in input().split(',')]


if __name__ == '__main__':
    test_case, want = read_test_case(), read_test_case()
    sol = Solution()
    n = len(test_case)
    original_input = copy(test_case)
    sol.duplicate_zeros(test_case)
    if test_case != want:
        print("\t❌ Test case failed:")
        print("\t\tInput:", original_input)
        print("\t\tGot:", test_case)
        print("\t\tWant:", want)
        sys.exit(1)
    print("\t✅ Test case accepted")
