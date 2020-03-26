from string import ascii_lowercase
print(ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz

def main():
    my_file = input('enter file name: ')
    infile = open(my_file, 'r')
    my_str = infile.read()
    letter = {}

    for l in my_str.lower():
        if l in ascii_lowercase:
            if l  in letter:
                letter[l] += 1
            else:
                letter[l] = 1
    print(letter)

main()