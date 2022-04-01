print("1.Predra")
print("2.Papel")
print("3.Tijera")

opcion = int(input("¿Que eliges Persona 1?"))
opcion2 = int(input("¿Que eliges Persona 2?"))

if opcion == 1:
    eligepersona = "piedra"
elif opcion == 2:
    eligepersona = "papel"
elif opcion == 3:
    eligepersona = "tijera"
print("Elige: ", eligepersona)

if opcion2 == 1:
    eligep2 = "piedra"
elif opcion2 == 2:
    eligep2 = "papel"
elif opcion2 == 3:
    eligep2 = "tijera"


if eligep2 == "papel" and eligepersona == "piedra":
    print("Gana persona 2, papel envuelve la piedra")
elif eligep2 == "papel" and eligepersona == "tijera":
    print("Ganas, tijera corta papel")
elif eligep2 == "tijera" and eligepersona == "piedra":
    print("Ganaste, Piedra pisa tiejra")
if eligep2 == "papel" and eligepersona == "piedra":
    print("Perdiste, papel envuelve piedra")
elif eligep2 == "tijera" and eligepersona == "papel":
    print("Perdiste, tijera corta papel")
elif eligep2 == "piedra" and eligepersona == "tijera":
    print("Perdiste, piedra pisa tijera")
elif eligep2 == eligepersona:
    print("empate")
