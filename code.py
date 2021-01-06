MOD = 998244353

# sometimes
#   n <= 80000
#   m <= 100000
# while sometimes
#   n <= 3000
#   m <= 2^200

# def height(n,m):
#     sum = n + m 
#     total = print('The summation is: ' + str(sum))
#     return sum

def sum (n,m):
    sum = n + m
    total = print('The result is: ' + str(sum))
    return sum


def subtract (n,m):
    subtract = n - m
    total = print('The result is: ' + str(subtract))
    return subtract


def divide (n,m):
    divide = n / m
    total = print('The result is: ' + str(divide))
    return divide


def multiply (n,m):
    multiply = n * m
    total = print('The result is: ' + str(multiply))
    return multiply

    
if __name__ == "__main__":
    # height(100.5,200)
    n = input('Enter the firt number: ')
    n = float(n)
    m = input('Enter the second number: ')
    m = float(m)
    menu = """ 
            Welcome to the menu 😁🙌
            1-Sum
            2-Subtract
            3-Divide
            4-Multiply
            """

    print(menu)
    option = int(input('Choose a option: '))
    if option == 1:
        sum(n,m)
    elif option == 2:
        subtract(n,m)
    elif option == 3:
        divide(n,m)
    elif option == 4:
        multiply(n,m)
    else:
        print('The option is not valid.')