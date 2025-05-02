"""
Have students write a Python program that takes in an input message from the user and 
repeats the message 10 times!
"""

def main():
    message = input("What's your section name: ") # variable, takes input text from the user
    pre_text = "Our section name is: " # this stays the same, treat it like a constant

    for i in range(10):
        print(pre_text, message) # example of string concatation


if __name__ == "__main__":
    main()
  
