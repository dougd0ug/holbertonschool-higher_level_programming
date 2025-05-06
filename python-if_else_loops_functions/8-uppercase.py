#!/usr/bin/python3

def uppercase(str):
    for i in str:
        upper = ord(i)
        if 97 <= upper <= 123:
            upper -= 32

        print("{:c}" .format(upper), end="")

#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")