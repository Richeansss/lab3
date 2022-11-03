i_numb = int(input("Введите число: "))
str_strok = ""

if(i_numb >= 1 and i_numb <= 9):
    for i_count in range(1, i_numb+1, 1):
        str_strok += str(i_count)
    print(str_strok)
