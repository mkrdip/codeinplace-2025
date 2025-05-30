def main():
    # Create a list called `fruit_list` that contains the following fruits: 
    # 'apple', 'banana', 'orange', 'grape', 'pineapple'.
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # print(type(fruit_list))
    
    # Print the length of the list.
    print(len(fruit_list))

    # Add 'mango' at the end of the list. 
    fruit_list.append("mango")

    # Print the updated list.
    print(fruit_list)

    fruit_list.pop(3)

    # Print the updated list.
    print(fruit_list)

    ## Print all items in a list
    # for i in fruit_list:
    #     print(i)

    # Skipping indexs that are odd
    # for i in range(0, len(fruit_list)-1, 2):
    #     print(fruit_list[i])

if __name__ == "__main__":
    main()
  
