import urllib.request
from string import ascii_lowercase
from pprint import pprint

def main():

    infile = urllib.request.urlopen('http://www.example.com/')
    my_str = infile.read().decode()
    letter = {}

    for l in my_str.lower():
        if l in ascii_lowercase:
            if l  in letter:
                letter[l] += 1
            else:
                letter[l] = 1
    print(letter)
    pprint(letter)

main()