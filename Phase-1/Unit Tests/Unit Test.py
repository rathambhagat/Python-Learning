# Doc note: `from module import name` imports only the specified name into this namespace (cleaner than `import module` when you only need one item).
from Test import square

def main():
    test_square()# testing the function 
# Doc note: Test functions named with a `test_` prefix are auto-discovered and run by pytest without needing to call them manually.
def test_square():
    # Doc note: `assert expr` evaluates the expression; raises AssertionError if False. Core building block of unit testing.
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
# Doc note: `__name__ == "__main__"` is True only when this script is run directly, not when imported. Prevents test setup from firing on import.
if __name__ == "__main__":
    main()
    