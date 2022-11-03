array_str = ["bright", "left", "right"]
print(array_str)
new_str = ""
for str in array_str:
    new_str += str + ","
print("Новая строка: ", new_str)
new_str = new_str[:len(new_str) - 1]
print("Удалим последний символ: ", new_str)
new_str = new_str.replace("right", "TEMP")
new_str = new_str.replace("left", "right")
new_str = new_str.replace("TEMP", "left")
print("Результат: ", new_str)