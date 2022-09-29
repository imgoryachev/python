'''
# Comments
'''

# Цикл
i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1

# Объявляем функцию
def func():
    print("Yo")

# Вызываем функцию
func()


variable = func()
print(variable)


# Преобразование типов данных
a = "2"
b = 3
c = int(a) + b
print(c)


age = 22
message = "Age: " + str(age)   # Age: 22
print(message)