from Kasutajate_funktsioonide_loomine import*

a=float(input("arv1:"))
a=float(input("arv2:"))
t=input("tehe:")
vastus=arithmetic(a,b,t)
print(vastus)

vastus=arithmetic(float(input("arv1:")),float(input("arv2:")),input("tehe:"))
print(vastus)

#is_year_leap funktsiooni kasutamine
aasta=int(input("Mis aasta tahad kontrollida? "))
if aasta>0:
    v=is_year_leap(aasta)
    print(v)
    if v:
        print(f"{aasta} on liigasta")
    else:
        print(f"{aasta} ei ole liigasta")
