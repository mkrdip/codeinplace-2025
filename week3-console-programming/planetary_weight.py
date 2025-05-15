"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

"""
1 A) Define all constants
1) Take an input from the user as earthling weight in a variable
2) We know inputs are considered string, so we have to convert float number
3) A) Calculate: Multiply with 0.378 and store in a variable
3) B) Use variables to store values
4) Print weight on Mars
"""

# When it's all CAPS and outside any function, these variables can be called as constants
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378 
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14


def main():
    earthling_weight = input("Enter a weight on Earth: ")
    earthling_weight_float = float(earthling_weight)
    # print(type(earthling_weight)) # string variable type
    # print(type(earthling_weight_float)) # float variable type

    planet_name = input("Enter a planet: ")

    ## check the name of the planet and use it's constant
    ## for comparison use == operator
    if planet_name == "Mercury":
        planet_gravity = MERCURY_GRAVITY
    elif planet_name == "Venus":
        planet_gravity = VENUS_GRAVITY
    elif planet_name == "Mars":
        planet_gravity = MARS_GRAVITY
    elif planet_name == "Jupiter":
        planet_gravity = JUPITER_GRAVITY
    elif planet_name == "Saturn":
        planet_gravity = SATURN_GRAVITY
    elif planet_name == "Uranus":
        planet_gravity = URANUS_GRAVITY
    elif planet_name == "Neptune":
        planet_gravity = NEPTUNE_GRAVITY
    else:
        planet_gravity = 1
        # print("You have to enter a planet name!")
        
    planet_weight = earthling_weight_float * planet_gravity

    planet_weight_rounded = round(planet_weight, 2)

    print("The equivalent weight on ", planet_name, ": ", planet_weight_rounded)

if __name__ == "__main__":
    main()
