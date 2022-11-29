print("""
Menú:
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
0. Salir
""")
opción=input("Selecciona la opción que quieras: ")
a = input("Indica el primer operante: ")
b = input("Indica el segundo operante: ")
match opción:
    case "1":
        c=int(a)+int(b)
        print("La suma de ",a," más ",b," es ",c)
    case "2":
        c=int(a)-int(b)
        print("La resta de ",a," menos ",b," es ",c)
    case "3":
        c=int(a)*int(b)
        print("La multiplicación de ",a," por ",b," es ",c)
    case "4":
        c=int(a)/int(b)
        print("La división de ",a," división ",b," es ",c)
    case "0":
        print("Adiós")
    case other:
        print("Opción no válida")