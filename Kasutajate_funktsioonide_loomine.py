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

