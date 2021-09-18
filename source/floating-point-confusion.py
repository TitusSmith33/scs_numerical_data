def floating_point_confusion() -> None:
    """Demonstrate the properties of floating point numbers."""
    # initialize the number to 0.0
    number = 0.0
    for _ in range(10):
        number = number + 0.1
    # check to see if the number is equal to 1.0
    # the number is equal to 1.0, which is expected
    if number == 1.0:
        print(f"The value of {number} is equal to 1!")
    # the number is not equal to 1.0, even though that is expected
    else:
        print(f"The value of {number} is not equal to 1!")
    # perform a multiplication that is also expected to be 1.0
    multiply_number = 10.0 * 0.1
    # determine if the first computation gives the results of the second one
    if number == multiply_number:
        print(f"The value of {number} is equal to {multiply_number}!")
    # the results are again not the same
    else:
        print(f"The value of {number} is not equal to {multiply_number}!")


print("Illustrating some strange properties of floating-point numbers!")
floating_point_confusion()
