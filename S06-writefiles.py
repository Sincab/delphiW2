from random import randint

def main():
    # Open file for writing data
    outfile = open("Numbers.csv", "w")
    for i in range(10):
        outfile.write(str(randint(0, 9)) + "_") #if coma in
    outfile.write(str(randint(0, 9)))
    outfile.close() # Close the file
    # Open file for reading data
    infile = open("Numbers.csv", "r")
    s = infile.read()
    numbers = [int(x) for x in s.split(",")]
    for number in numbers:
        print(number, end = " ")
    infile.close() # Close the file

main() # Call the main function

#SZAH7P
