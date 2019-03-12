from collections import defaultdict
# Count Occurances of letters in string, replace with new string of letter followed by number
string_example = "aabbbcccccf"


def string_parser(string):
    lexicon = defaultdict(int)
    output = ""
    for letter in string:
        lexicon[letter] += 1
    
    for k,v in lexicon.items():
        output += k + str(v)
    
    print(output)

string_parser(string_example)


int_array = [5,4,3,2,1]

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
    while number >> bits: bits += 1
    print(bits)

count_bits(100)
