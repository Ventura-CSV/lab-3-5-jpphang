def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    """
    ########################################
    Code Your Program here
    ########################################
    """
    duplication = 0
    
    if num1 == num2 == num3:
        duplication = 3
        
    elif num1 == num2 and num1 != num3:
    elif num1 == num3 and num1 != num2:
    elif num2 == num1 and num2 != num3:
    elif num2 == num3 and num2 != num1:
        

    ########################################
    # Do not delete the return statement
    ########################################
        return duplication


if __name__ == '__main__':
    main()
