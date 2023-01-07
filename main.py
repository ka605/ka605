why = ('(｢•-•)｢ ʷʱʸ?')
first_number = ('Ok, then type in your first number. ')
second_number = ('Ok, now type in you second number. ')
q1 = input('''Hello! this is my calculator to help you do your homework. But before we get started, I need to know what type of operation you want to use, 
    type multiplication for multiplication,
    type division for division, 
    type addition for addition,
    type subtraction for subtraction,
    type floor division for floor division which is division without remainders,
    type exponents for exponents,
    and type modulus for modulus, the modulus is basiclly the remainder of division.
    ''')

# Simple Equations
if q1 == 'multiplication':
    num1 = input(first_number)
    num2 = input(second_number)
    print('The product is ' + str(int(num1) * int(num2)))
elif q1 == 'division':
    num1 = input(first_number)
    num2 = input(second_number)
    print('The quotient is ' + str(int(num1) / int(num2)))
elif q1 == 'addition':
    num1 = input(first_number)
    num2 = input(second_number)
    print('The sum is ' + str(int(num1) + int(num2)))
elif q1 == 'subtraction':
    num1 = input(first_number)
    num2 = input(second_number)
    print('The difference is ' + str(int(num1) - int(num2)))
elif q1 == 'floor division':
    num1 = input(first_number)
    num2 = input(second_number)
    print('The floor quotient is ' + str(int(num1) // int(num2)))
elif q1 == 'exponents':
    num1 = input(first_number)
    num2 = input(second_number)
    if num2 == '1':
        st = print('st')
    print('The answer is ' + str(int(num1) ** int(num2)))
elif q1 == 'modulus':
    num1 = input(first_number)
    num2 = input(second_number)
    print('The remainder is ' + str(int(num1) % int(num2)))

else:
    print('Invalid Entry. Please Try Again. :(')
