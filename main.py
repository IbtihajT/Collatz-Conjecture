# Create a Recursive function
def collatz_conjecture(number):

    # Base case for recurssion
    if number == 1:
        return 1

    # Odd Case
    if number % 2 != 0:
        return collatz_conjecture((3 * number) + 1)

    # Even Case
    else:
        return collatz_conjecture(number / 2)


if __name__ == '__main__':
    number = 2**997
    print(f"Number to execute the conjecture on: {number}\n")
    print(f"Output: {collatz_conjecture(number)}")
