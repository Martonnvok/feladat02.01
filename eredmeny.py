#egy komment
jlapok=[1,2,3,4,5]
glapok=[6,7,8,9,10]
def osszeg(lap):
    ossz = 0
    for i in lap:
        ossz += i

    return osszeg

def eredmeny(jatekos, gep  ):
    if osszeg(jatekos) > 21:
        print("A játékos Vesztett")
    elif osszeg(gep) > 21:
        print("A gép vesztett")

