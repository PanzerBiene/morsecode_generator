def read_letters(file_name):
    f = open(file_name)
    contents = f.read()
    i = 0
    output = []
    while i < len(contents):
        letter = contents[i]
        print(letter)
        output.append(morsecode(letter))
        i += 1
    return output

def morsecode(char):
    morse = ["*-", "-***", "-*-*", "-**", "*", "**-*", "--*", "****", "**", "*---", "-*-", "*-**", "--", "-*", "---", "*--*", "--*-", "*-*", "***", "-", "**-", "***-", "*--", "-**-", "-*--", "--**"]
    morse_numbers = ["-----", "*----", "**---", "***--", "****-", "*****", "-****", "--***", "---**", "----*", "-----"]
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    i = 0
    if char.isdigit():
        while i < len(numbers):
            if char == numbers[i]:
                return morse_numbers[i]
            i+=1
    else:
        while i < len(letters):
            if char == letters[i]:
                return morse[i]
            i+=1


print(read_letters("file.txt"))
