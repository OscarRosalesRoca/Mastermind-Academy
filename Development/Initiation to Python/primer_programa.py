num1 = int(input("Introduce el número 1:"))
num2 = int(input("Introduce el número 2:"))
num3 = int(input("Introduce el número 3:"))

num_max1 = str(max(num1, num2, num3))
num_min1 = str(min(num1, num2, num3))

num_max2 = max (num1, num2, num3)
num_min2 = min (num1, num2, num3)

print("El número más grande que has introducido es: " + num_max1 + " y el número más pequeño es: " + num_min1)

print("El numero más alto de los que me has dado es: {}".format(num_max2))
print("El numero más bajo de los que me has dado es: {}".format(num_min2))

print("El número más grande es: {}".format(max(num1, num2, num3)))

print("El número más grande entre: {}, {} y {} es: {}".format(num1, num2, num3, max(num1, num2, num3)))
