print("Bienvenido al conversor, aquí podrás convertir números romanos a decimales o a la inversa.")
print("Para convertir de romanos a decimales, escribe 1")
print("Para convertir de decimales a romanos, escribe 2")
print("Si quiere salir del conversor,escribe 3")
entrada=int(input())
while entrada != 3:
    if entrada == 1:
        romano=input("Introduce un número romano: ")
        romano=romano.upper()
        decimal=0
        for i in range(len(romano)):
            valores={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}	
            decimal+=valores[romano[i]]
        print("El número romano ", romano, " equivale a ", decimal, " decimales")

    elif entrada == 2:
        decimal=int(input("Introduce un número decimal: "))
        numero_inicial=decimal
        romano=""
        while decimal > 0:
            valores2=(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
            romanos=("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
            for i in range(len(valores2)):
                while decimal >= valores2[i]:
                    decimal -= valores2[i]
                    romano += romanos[i]
        
        print("El número decimal ", numero_inicial, " equivale a ", romano, " romanos")

    print("Bienvenido al conversor, aquí podrás convertir números romanos a decimales o a la inversa.")
    print("Para convertir de romanos a decimales, escribe 1")
    print("Para convertir de decimales a romanos, escribe 2")
    print("Si quiere salir del conversor,escribe 3")
    entrada=int(input())

