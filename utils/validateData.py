import os

def validateInt(msg:str)->int:
    try:
        x = int(input(msg))
    except ValueError:
        print("ERROR: VALOR INVALIDO")
        os.system("pause")
        return validateInt(msg)
    else:
        return x

def validatatext(msg):
    x = input(msg)
    if all(c.isalnum() or c.isspace() for c in x) and x.strip():
        return x
    else:
        print("ERROR: VALOR INVALIDO")
        os.system("pause")
        return validatatext(msg)
    
def validateflot(msg:str)->float:
    try:
        x = input(msg)
        return float(x)
    except ValueError:
        print('ERROR: VALOR INVALIDO. Ingrese un número válido.')
        os.system("pause")
        return validateflot(msg)