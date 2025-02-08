print("=================")
print("Menu of options")
print("=================\n")
print("Press 1 in order to convert the number to a word")
print("Press 2 in order to convert the word to a number\n")

selected_option= int(input("What do you want to do? "))

if selected_option == 1:
    print("\nConvert the number to a word \n")
    if selected_option == 1:
     num_to_convert = int(input("¿What number do you want to convert to a word? "))
    if num_to_convert == 1:
       print('The name is "One"')
    elif num_to_convert ==2:
     print('The name is "Two"')
    elif num_to_convert ==3:
      print('The name is "Three"')   
    elif num_to_convert ==4:
     print('The name is "Four"')
    elif num_to_convert ==5:
      print('The name is "Five"')    
    else:
      print("The value is not register, please try again")


elif selected_option == 2: 
    print("\nConvert the word to a number \n")
    if selected_option == 2:
     word_to_convert = str(input("¿What word do you want to convert to a number? "))
     word_to_convert = word_to_convert.lower() #This method will change the value at lowercase in order to avoid a possible bug
    if word_to_convert == "one":
       print('The number is "1"')
    elif word_to_convert == "two":
       print('The number is "2"')
    elif word_to_convert =="three":
       print('The number is "3"')   
    elif word_to_convert =="four":
       print('The number is "4"')
    elif word_to_convert =="five":
       print('The number is "5"')    
    else:
      print("The value is not register, please try again")


else: 
    print("\nThe option is not register, please try again")
 
print("End.")
    



