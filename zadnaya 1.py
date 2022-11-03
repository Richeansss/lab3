i_numb = int(input("Введите целое число: "))


if(i_numb % 3 == 0 and i_numb  % 5 == 0):
    print("Fizz Buzz")
elif (i_numb % 3 == 0):
    print("Fizz")
elif (i_numb % 5 == 0):
    print("Buzz")

