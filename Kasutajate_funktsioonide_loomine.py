from ctypes.wintypes import LGRPID
from lib2to3.pgen2.driver import load_grammar
from math import lgamma


#1
def arithmetic(arv1:float,arv2:float,tehe:str)-> any :
    """Funktsioon töötab nagu lihtne kalkulaator
    + - liitmine,
    - - lahutamine,
    * - korrutamine,
    / - jagamine
    kui sisend ei ole järjendis [+,-,/,*],siis tagastab sõne "Tundmatu tehe"
    :param float arv1: Sisend ujukomaarvu tüübina
    :param float arv2: Sisend ujukomaarvu tüübina
    :param str tehe: sisend listist [+,-,/,*]
    :rtype: varMääramata tüüp (float või str)
    """
    if tehe in ["+","-","*","/"]:
        if arv2==0 and tehe=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="Tundmatu tehe"
    return vastus 
#2
def is_year_leap(aasta:int)->bool:
    """
    Liigaasta leidmine.
    Tagastab True, kui aasta on liigaasta ja False, kui aasta on tavaline aasta.
    :param int aasta: Sisend kasutajalt
    :rtype: bool
    """
    if aasta%4==0:
     v-True
    else:
        v=False
    return v
#3
def square(külg:float)->any:
    """funkrioon tagastab 
    :param:Ruudu külg
    :rtype: float
    :return: Perimeeter, pindala ja diagonaal
    """
    S=külg**2
    P=4*külg
    d=(2)**(1/2)*külg
    return S,P,d
#4 
def season(param:int)->str:
    """
    param:Kuu number (1 - 13)
    :type month: int
    :return: Aastaeg, millele kuu kuulub ("talv", "kevad", "suvi" või "sügis")
    :rtype: str
    """
    if param in [1,2,12]:
        H="Talv"
    elif param in [3,4,5]:
        H="Kevad"
    elif param in [6,7,8]:
        H="Suvi"
    else:
        H="Sügis"
    return H
#5
def bank(summa: float,aastad:int)->float:
    """
    :param algkapital(eurodes)
    :param aastad: Investeerimise kestus(aastades)
    :type aastad: int
    :return: Lõppsumma pärast teatud aastat(arvestades 10% intressi)
    :rtype float
    """
    for aasta in range(aastad):
        summa*=1.1
    return summa 
