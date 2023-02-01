#egy komment
jlapok=[1,2,3,4,5]
glapok=[6,7,8,9,10]
def kiirat(jatekos: list, gep: list):
    kiirat = ""
def osszeg(lap):
    ossz = 0
    for i in lap:
        ossz += i

    return osszeg

def eredmeny(jatekos: list, gep: list  ):
    if osszeg(jatekos) > 21:
        kiirat="A játkos vesztett"
    elif osszeg(gep) > 21:
        kiirat="A gép vesztett"

eredmeny(jlapok, glapok)
