first_input=input("Enter your first number: ")
second_input=input("Enter your second numder: ")

App_operators="1_+\n2_-\n3_*\n4_/\n5_^\n6_% "

if first_input.isdigit()and second_input.isdigit():
    print(App_operators)
user_operators=input("please enter your choise: ")
result=0
is_success=False

if user_operators=="+"or user_operators=="1":
    result =int(first_input) + int(second_input)
    is_success=True
elif user_operators=="-"or user_operators=="2":
    result=int(first_input) - int(second_input)
    is_success=True
elif user_operators=="*"or user_operators=="3":
    result=int(first_input) *int(second_input)
    is_success=True
elif user_operators=="/"or user_operators=="4":
    result=int(first_input)/ int(second_input)
    is_success=True
elif user_operators=="^"or user_operators=="5":
    result=int(first_input) ^ int(second_input)
    is_success=True
elif user_operators=="%"or user_operators=="6":
    result=int(first_input) % int(second_input)
    is_success=True
else:
    print("Invalid input, please try again!")


if is_success==True:
    print(result)
    print(" Do you want to make more oprations?:\n1_round\n2_without a decimal point\n3_out")
    opr_choice=input("your choice: ")
    print(result)

else:
    print("Invalid input, please try again!")
