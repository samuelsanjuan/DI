#1

def tabla(num):
    multiplo=0
    while multiplo<11:
        print(num * multiplo)
        multiplo= multiplo + 1
#tabla(10)

#2

def nums10a20():
    num=10
    while num<21:
        print(num)
        num+=1
#nums10a20()

#3

def grados(faren):
    print((faren-32)*5/9)
#grados(100)

#4

def bisiesto(ano):
    if ano%4==0:
        if ano%100==0:
            if ano%400==0:
                print("es bisiesto")
            else:
                print("no es bisiesto")
        else:
            print("es bisiesto")
    else:
        print("no es bisiesto")

#bisiesto(200)

#5
def diasMes(mes):
    meses={'enero': '31 dias','febrero':'28 dias','marzo':'31 dias','abril':'30 dias','mayo':'31 dias','junio':'30 dias','julio':'31 dias','agosto':'31 dias','septiembre':'30 dias','octubre':'31 dias','noviembre':'30 dias','diciembre':'31 dias'}
    print (meses[mes])

#diasMes('enero')

#6
def diaValido(dia, mes, ano):
    if (mes>12):
        print('mes valido')
        if (mes==1,3,5,7,8,10,12 ):
