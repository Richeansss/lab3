f_numb = float(input("Введите число: "))


if(f_numb % 2 != 0):
    print("Плохо")
elif (f_numb >= 2 and f_numb <= 5):
    print("Нелохо")
elif (f_numb >= 6 and f_numb <= 20):
    print("Так себе")
else:
    print("Отлично")