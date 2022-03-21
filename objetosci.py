import math

def objetoscKuli(r):
    return (4*math.pi*r**3)/3
def objetoscProstopadloscianu(a,b,c):
    return a*b*c
def objetoscGraniastoslupa(a,b,h):
    pp = a/2 * b
    return pp * h

if __name__ == "__main__":
    r = int(input("Podaj promień kuli: "))
    a = int(input("Podaj a: "))
    b = int(input("Podaj b "))
    c = int(input("Podaj c: "))
    h = int(input("Podaj h: "))
    print("Objętość kuli: " + str(objetoscKuli(r)))
    print("Objętość prostopadłościanu: " + str(objetoscProstopadloscianu(a,b,c)))
    print("Objętość graniastosłupa: " + str(objetoscGraniastoslupa(a,b,h)))