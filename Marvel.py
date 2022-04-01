puede_volar = input("¿Puede Volar?")
es_humano = input("¿Es Humano?")
tiene_mascara = input("¿Tiene Mascara?")

if puede_volar =="si":
    if es_humano == "si":
        if tiene_mascara == "si":
            print("Ironman")
        else:
            print("Capitan Marvel")
    else:
        if tiene_mascara =="si":
            print("Ronan Accuser")
        else:
            print("Vision")
else:
    if es_humano =="si":
        if tiene_mascara =="si":
            print("Spiderman")
        else:
            print("Hulk")
    else:
        if tiene_mascara =="si":
            print("Black Bolt")
        else:
            print("Thanos")