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
        
    elif num1 == num2 or num1 == num3:
        duplication = 2
        
    else:
        duplication = 0
        
    print(f"duplication:{duplication}")
    
    ########################################
    # Do not delete the return statement
    ########################################
        
    return duplication


if __name__ == '__main__':
    main()
