from collections import defaultdict
# Count Occurances of letters in string, replace with new string of letter followed by number
string_example = "aabbbcccccf"


def string_parser(string):
    lexicon = defaultdict(int)
    output = ""
    for letter in string:
        lexicon[letter] += 1

    for k, v in lexicon.items():
        output += k + str(v)

    print(output)


string_parser(string_example)


int_array = [5, 4, 3, 2, 1]


def reverse_array(int_array):
    reversed_array = []
    while(True):
        if len(int_array) > 0:
            num = int_array.pop(-1)
            reversed_array.append(num)
            continue
        break

    print(reversed_array)


reverse_array(int_array)


def count_bits(number):
    bits = 0
    while number >> bits:
        bits += 1
    print(bits)


# count_bits(100)


def reverse_string(normal_string):
    return normal_string[::-1]


def simple_input():
    x = input("Please enter in age")
    print(x)


# simple_input()


"""You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above."""


def licenseKeyFormatting(S: str, K: int) -> str:
    no_dash_string = list(S.replace("-", ""))
    string_length = len(no_dash_string)
    new_string = []
    while True:
        import pdb
        pdb.set_trace()
        for i in range(0, K):
            if not no_dash_string:
                break
            new_string.append(no_dash_string.pop())
            if (i-1) == K:
                new_string.append()
    output =  "".join(new_string[::-1])
    print(output.upper())
licenseKeyFormatting("5F3Z-2e-9-w", 4)
