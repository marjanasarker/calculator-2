"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
#result=power(float(num1), float (num2))

#try:
while True:
    
    user_input=input("Write your equation here:")
    print(user_input)
    tokens=user_input.split(" ")
    operator = tokens[0]
    
    #print(tokens)
    if "q" ==operator:
        print("You have exited")
        break 

    elif len(tokens)<2:
        print("Not enough inputs")
        break
    
    
    elif len(tokens)<3:
        num1=tokens[1]
        num2=0
    else:
        num1=tokens[1]
        num2=tokens[2]
        
        if operator=="+":
            result=add(float(num1), float (num2))
        elif operator=="-":
            result=subtract(float(num1), float (num2))
        elif operator=="pow":
            result=power(float(num1), float (num2))
        elif operator=="*":
            result=multiply(float(num1), float (num2))
    print (result)
#except ValueError:
