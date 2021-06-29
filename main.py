def read_letters(file_name):
    f = open(file_name)
    contents = f.read()
    i = 0
    output = []
    while i < len(contents):
        letter = contents[i]
        output.append()
        i += 1

def morsecode(letter):
    morse = ["*-", "-***", "-*-*", "-**", "*", "**-*", "--*", "****", "**", "*---", "-*-", "*-**", "--", "-*", "---", "*--*", "--*-", "*-*", "***", "-", "**-", "***-", "*--", "-**-", "-*--", "--**"]
    numbers = ["-----", "*----", "**---", "***--", "****-", "*****", "-****", "--***", "---**", "----*", "-----"]
    