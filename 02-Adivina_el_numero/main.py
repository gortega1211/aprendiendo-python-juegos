import random

intentos_realizados = 0

nombre_jugador = input("Hola, ¿como te llamas?: ")

numero_a_adivinar = random.randint(1, 20)

print(f"Bueno {nombre_jugador}, estoy pensando en un número entre 1 y 20, ¿Podrás adivinarlo en un máximo de 5 intentos?")

while intentos_realizados < 5:
    print("Vamos, intenta adivinar")
    estimacion = int(input())

    intentos_realizados += 1

    if estimacion < numero_a_adivinar:
        print("Tu estimación es muy baja.")
    elif estimacion > numero_a_adivinar:
        print("Tu estimacion es muy alta.")
    else:
        print(f"¡Buen trabajo {nombre_jugador}! ¡Has adivinado mi número en {intentos_realizados} intentos!")
        break
else:
    print(f"Pues no. El número que estaba pensando era {numero_a_adivinar}.")
