def main():#defining a square function for testing
    x = int(input("What's x?"))
    print("x square is",square(x))
# Doc note: Keeping logic in a separate module (Test.py) lets Unit Test.py import just the function and test it in isolation — this is the standard pattern for unit testing.
def square(n):
    return n*n
# Doc note: `__name__ == "__main__"` guard ensures `main()` only runs when this file is executed directly, not when imported by Unit Test.py.
if __name__ == "__main__":
    main()