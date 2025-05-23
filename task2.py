from collections import deque


def find_polindrome(input_string):
    make_normal = "".join(input_string.split()).lower()  # use hint

    deque_char = deque(make_normal)

    while len(deque_char) > 1:
        if deque_char.popleft() != deque_char.pop():
            return False

    return True


# Test (use hint)
if __name__ == "__main__":

    test_strings = [
        "Привіт, світ!",
        "123321",
    ]

for test_string in test_strings:
    result = find_polindrome(test_string)
    print(f"'{test_string}' : {result}")