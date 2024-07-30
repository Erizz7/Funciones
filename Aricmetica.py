def sumar(n1, n2):
    return n1+n2

def restar(n1, n2):
    return n1-n2

def multiplicar(n1, n2):
    return n1*n2

def dividir(n1, n2):
    return n1/n2


def operaciones(nombre,n1,n2):
    print(nombre)
    print(17*"-") 
    print("Sumar",sumar(n1,n2))
    print("Resta:", restar(n1,n2))
    print("Multiplicar: ", multiplicar(n1,n2))
    print("División: ", dividir(n1,n2))
    print(17*"-")


def edad(nombre,n1):
    print(20*"-")
    print("Mi Nombre es:",nombre)
    print("Mi edad es:", n1)

edad(input("Ingresa Tu nombre: "),int(input("Ingresa tu edad: ")))