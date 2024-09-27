import math

def funkcja():
    aStr = input("Podaj a:")
    bStr = input("Podaj b:")
    cStr = input("Podaj c:")
    print(aStr)
    print(bStr)
    print(cStr)
    
    if (aStr.isdigit() == False) or (bStr.isdigit() == False) or (cStr.isdigit == False):
        print("Podane wartosci sa niepoprawne - mozesz uzywac tylko liczb")
        return
    
    a = int(aStr)
    b = int(bStr)
    c = int(cStr)
    
    x1 = 0
    x2 = 0
    odp = 1
    delta = 1
    delta = (b*b) - (4*(a*c))
    
    if(delta<0):
        print("nie ma odpowiedzi")
    elif(delta==0):
        odp = -1*(b/(2*a))
        print("miejsce zerowe to: ",odp)
    elif(delta > 0):
        delta= math.sqrt(delta)
        x1 = ((-1*b)-delta)/(2*a)
        x2 = ((-1*b)+delta)/(2*a)
        print("miejsce x1 to: ",x1," miejsce x2 to: ",x2)
        
    return

funkcja()