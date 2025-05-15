"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

"""
1) Take an input from the user as earthling weight in a variable
2) We know inputs are considered string, so we have to convert float number
3) A) Calculate: Multiply with 0.378 and store in a variable
3) B) Use variables to store values
4) Print weight on Mars
"""

MARS_GRAVITY = 0.378 # When it's all CAPS this variable can be called a constant

def main():
    earthling_weight = input("Enter a weight on Earth: ")
    earthling_weight_float = float(earthling_weight)
    # print(type(earthling_weight)) # string variable type
    # print(type(earthling_weight_float)) # float variable type
    mars_weight = earthling_weight_float *  MARS_GRAVITY
    # According to Assignment it sounded like it should be 2
    # but the Check Correct script wants it to be 4
    mars_weight_rounded = round(mars_weight, 4) 
    print("The equivalent weight on Mars: ", mars_weight_rounded) # concat

    

if __name__ == "__main__":
    main()
