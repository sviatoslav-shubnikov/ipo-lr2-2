n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))

apples_for_student = k // n
apples_left_in_basket = k % n

print(f"Каждому школьнику достанется: {apples_for_student}")
print(f"Яблок останется в корзинке: {apples_left_in_basket}")