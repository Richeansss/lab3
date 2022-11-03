def check(str):
    count = 0
    for s in range(0, len(str), 1):
        if (str[s].isspace()):
            count += 1
            if count == 2 and (s + 1) < len(str) and str[s + 1].isalpha():
                return True
        if str[s].isdigit():
            count = 0
    return False

print("text =", "one 2 two three four 5 six", ", результат ", check("one 2 two three four 5 six"))
print("text =", "one 2 two 3 four 5 six ", ", результат ", check("one 2 two 3 four 5 six "))