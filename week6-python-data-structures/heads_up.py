import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    lines_list = []
    with open(FILE_NAME) as f:
        for line in f:
            # removes whitespace characters (\n) from the start and end of the line
            line = line.strip() 
            # if the line was only whitespace characters, skip it 
            if line != "":
                lines_list.append(line)
                
    return lines_list


def main():
    words = get_words_from_file()
    # print(words)
    while True:
        # Here boolean True means while the operations 
        # below are true this program continues
        input("Presss enter to continue")
        chosen_word = random.choice(words)
        print(chosen_word)
        
    

if __name__ == '__main__':
    main()
