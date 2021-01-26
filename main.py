#Найдите последовательность повторяющихся символов (к примеру AAAA, BBBbbB) и запишите в строку, и если после символов будут цифры, то найдите и запишите их в строку, где были до этого символы(добавьте к тому), если конечно цифры после последовательности есть.
#Помимо этого если будут цифры, то найдите сумму всех цифр(не чисел(для AAAA12372 вы должны сделать так 1+2+3+7+2 = 15)) и выведите.
#Запишите длину получившейся строки и выведите.
def check(number):
    try:
        int(number)
        return True
    except Exception:
        return False
f = open("24-3.txt", "r")
connctn = f.readline()
maxlen = 1
minlen = 0
data = ""
data_2 = ""
size = len(connctn) - 1
sum = 0
for i in range(150, size):
    smthng = connctn[i]
    number_1 = connctn[i]
    number_2 = connctn[i + 1]
    number_prev = connctn[i - 1]
    if number_1.lower() == number_2.lower() and i != size:
        minlen += 1
        data_2 = data_2 + smthng
    elif number_prev == number_1:
        minlen += 1
        data_2 = data_2 + smthng
    elif data_2 != "" and check(number_1) == True:
        data_2 = data_2 + number_1
    else:
        if maxlen < minlen:
            maxlen = minlen
            minlen = 0
            data = data_2
            data_2 = ""
        else:
            minlen = 0
            data_2 = ""
f.close()
for i in data:
    if check(i) == True:
        sum += int(i)
print(maxlen)
print(data)
print(sum)