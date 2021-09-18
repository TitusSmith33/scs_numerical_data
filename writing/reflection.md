# Numerical Data

## Titus Smith

## Program Output

### What is the output from running the following commands?

Use a fenced code block to provide the output for this command.

- `python determine-even-odd.py`

```

Determining whether integer values are even or odd
The number of 0 is even!
The number of 10 is even!
The number of 11 is odd!
The number of -10 is even!
The number of -11 is odd!

```

Use a fenced code block to provide the output for this command.

- `python floating-point-confusion.py`

```

Illustrating some strange properties of floating-point numbers!
The value of 0.9999999999999999 is not equal to 1!
The value of 0.9999999999999999 is not equal to 1.0!

```

## Program Understanding

### What is the purpose of the `%` operator in a Python program?

Provide a one-paragraph response to this question.

The % operator in python is used to find the remainder of a value when two integers are divided by each other. If the two numbers that are being divided can be divided into each other equally then there will be no remainders, however if the two numbers cannot be divided into each other perfectly then that means there will be a remainder. This can be useful to us when we are looking for an even or odd number, because all even numbers can be divided by two without any extra, and there will be a remainder when an odd is divided by two. This operator helps us identify number properties, like even or odd, and use that information to shorten large data sets.

#### What are the inputs and outputs of the `determine_even_odd` function?

Provide a one-paragraph response to this question.

The input the determine_even_odd function is an integer. This integer is then run through the code and using the "%" operator, as described above, the function then determines whether or not that particular integer that was inputted was even or odd. As this is happening if the integer comes back as it being an even number then the program returns a string, or words, and for this case it returns the strong even. If the input isn't even then the program returns the string odd, because if a number isn't even then it is odd.

#### Does the computation `10.0 * 0.1` produce the value of `1.0`? Why?

Provide a one-paragraph response to this question.

No, the program outputs that it is not equal to one. The problem has to do with floats conversion to binary numbers. When the float 0.1 is converted to binary language, binary can't fully represent that value but it can represent a value very very close to it, and if you were to round it then you would get the correct answer, but we aren't doing that. Although the binary representation may be really really close to the desired value, it isn't exact. Therefor when you multiply a number that is really close but exactly the correct number, you can't expect to get the intended output.

#### Does the `for` loop on lines 4 and 5 of `floating-point-confusion` produce the value of `1.0`? Why?

Provide a one-paragraph response to this question.

No, similar to the reason multiplying does not work, when the conversion from decimal values into binary numbers happens, the numbers are altered. Even though the binary representation may be close enough to the decimal value. With this program we aren't rounding therefor we aren't looking for close enough, we need a precise conversion. When you add 0.1 to itself ten times, yes it ends up being one, but the binary conversion of .1 isn't exactly equal to 0.1, it is slightly off. So when you add a slightly off number ten times, you won't get the expected output without rounding.
