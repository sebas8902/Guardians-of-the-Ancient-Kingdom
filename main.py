from personajes import Guerrero, Mago, Arquero, Combate


def ejecutar_casos_de_prueba():
    print("Verificación de validaciones y casos de prueba:")

    try:
        Guerrero("", 100, 30, 20)
    except ValueError as e:
        print(f"[PRUEBA PASADA] Nombre vacío rechazado correctamente: {e}")

    try:
        Mago("Gandalf", 150, 40, 10)
    except ValueError as e:
        print(f"[PRUEBA PASADA] Vida mayor a 100 rechazada: {e}")

    try:
        Arquero("Legolas", -10, 30, 5)
    except ValueError as e:
        print(f"[PRUEBA PASADA] Vida negativa rechazada correctamente: {e}")

    try:
        Arquero("Legolas", 80, -10, 5)
    except ValueError as e:
        print(f"[PRUEBA PASADA] Ataque inválido rechazado correctamente: {e}")

    try:
        Guerrero("Arthas", 100, 30, -5)
    except ValueError as e:
        print(f"[PRUEBA PASADA] Defensa inválida rechazada correctamente: {e}")

    print("\nCreación correcta de personajes:")

    guerrero = Guerrero("Arthas", 100, 30, 20)
    mago = Mago("Gandalf", 80, 40, 10)
    arquero = Arquero("Legolas", 90, 35, 15)

    print(guerrero.mostrar_estado())
    print(mago.mostrar_estado())
    print(arquero.mostrar_estado())

    print("\nPrueba de habilidad del Guerrero:")

    objetivo = Mago("Objetivo", 80, 20, 10)
    danio = guerrero.atacar(objetivo)

    print(f"Daño causado por el Guerrero: {danio}")
    print(f"Vida restante del objetivo: {objetivo.vida}")

    print("\nPrueba de habilidad del Mago:")

    objetivo = Guerrero("Objetivo", 100, 20, 20)
    danio = mago.atacar(objetivo)

    print(f"Daño causado por el Mago: {danio}")
    print(f"Vida restante del objetivo: {objetivo.vida}")

    print("\nPrueba de habilidad del Arquero:")

    objetivo = Guerrero("Objetivo", 100, 20, 15)
    danio = arquero.atacar(objetivo)

    print(f"Daño causado por el Arquero: {danio}")
    print(f"Vida restante del objetivo: {objetivo.vida}")

    print("\nPrueba de vida mínima:")

    objetivo = Guerrero("Objetivo", 20, 20, 10)
    danio = mago.atacar(objetivo)

    print(f"Daño efectivo recibido: {danio}")
    print(f"Vida final del objetivo: {objetivo.vida}")

    print("\nPrueba de personaje derrotado:")

    objetivo = Guerrero("Objetivo", 1, 20, 0)
    mago.atacar(objetivo)

    try:
        objetivo.atacar(mago)
    except ValueError as e:
        print(f"[PRUEBA PASADA] Ataque de derrotado rechazado: {e}")

    print("\nPrueba de empate técnico:")

    guerrero_empate = Guerrero("Arthas", 100, 10, 20)
    guerrero_empate_2 = Guerrero("Garrosh", 100, 10, 20)

    combate_empate = Combate(guerrero_empate, guerrero_empate_2)
    combate_empate.iniciar()

    print("\nSimulación oficial: Guerrero vs Mago\n")

    arthas = Guerrero("Arthas", 100, 30, 20)
    gandalf = Mago("Gandalf", 80, 40, 10)

    combate_oficial = Combate(arthas, gandalf)
    combate_oficial.iniciar()


if __name__ == "__main__":
    ejecutar_casos_de_prueba()