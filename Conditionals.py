def statements():
    x  = str(2)
    x1 = int(2)
    x2 = bool(1)
    x3 = float(2)
    x4 = complex(1,1)
    print(type(x4))

    num = int(input("ingrese dato: "))
    if num < 0:
       print(num)
    else:
        print("equivale a: ", num)

    
    cad = str(input("ingresar dato: "))
    if cad == '2' or cad == '3' :
        print(cad)
    elif cad != '3':
        print("es diferente a 3 ")
    else:
        print("el dato es: ",cad)

    
    n = input("Dato: ")
    n = int(n)
    if n < 3 and n != 0 :
        print(n)
    elif n > 3 :
        print(n)   
    else:
        print("error")

    n1 = input("Dato: ")
    n1 = int(n1)
    if n1 == 3:
        print(n1 is 3)  #is solo devuelve true o false comparador
    else:
        print("error")   


    words = ['alex','camilo','marta']
    print(len(words))

    for f in words:
        print(f, len(f)) #len me permite contar palabras o vocales o numeros o datos


    for p in words:
        print(words[1])
        print(len(words[1]))
        
        print(words[2])
        print(len(words[2]))


    for i in range(0, 20, 3):   #range(1,10)      #range(0,20,3) empieza desde 0 se va en 3 en 3 y no pasa el 20
        print(i) #incrementarle a la i + 1
    
    print(range(1,10)) #range(0, 10)
    
    print(sum(range(4)))  #0+1+2+3

    print(list(range(5)))


if __name__ == '__main__':    #valida si funcion raiz existe
    statements()   #indico funcion raiz