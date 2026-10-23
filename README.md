# Guardians-of-the-Ancient-Kingdom

Guardians of the Ancient Kingdom

1. Descripción del proyecto

Guardians of the Ancient Kingdom es un proyecto desarrollado en Python que simula un sistema de combate entre personajes de un reino ficticio. Su objetivo es aplicar los fundamentos de la Programación Orientada a Objetos (POO), incluyendo clases, herencia, encapsulamiento, abstracción y polimorfismo.

El sistema cuenta con una clase abstracta llamada "Personaje" y tres tipos de personajes: "Guerrero", "Mago" y "Arquero". Cada uno implementa su propia forma de atacar. Además, la clase "Combate" administra los turnos, calcula el resultado de la batalla y determina cuándo termina el enfrentamiento.

La simulación principal enfrenta a Arthas, un guerrero, contra Gandalf, un mago.

2. Objetivos

- Aplicar los principios de la Programación Orientada a Objetos en Python.
- Implementar una clase abstracta y clases derivadas mediante herencia.
- Proteger los atributos mediante encapsulamiento y validaciones.
- Implementar diferentes comportamientos de ataque mediante polimorfismo.
- Administrar los turnos y determinar el resultado de un combate.
- Comprobar el funcionamiento mediante pruebas y casos de validación.

3. Estructura del proyecto

guardians-of-the-ancient-kingdom/
├── README.md
├── personajes.py
├── main.py
├── test_personajes.py
└── requirements.txt

Descripción de los archivos

- "personajes.py": contiene la clase abstracta "Personaje", las clases "Guerrero", "Mago" y "Arquero", y la clase "Combate".
- "main.py": ejecuta las validaciones, las pruebas de funcionamiento y la simulación oficial.
- "test_personajes.py": contiene pruebas automatizadas con pytest.
- "requirements.txt": especifica las dependencias necesarias para ejecutar las pruebas.
- "README.md": documenta el funcionamiento, el diseño y las pruebas del proyecto.

4. Clases del sistema

4.1. Personaje

Es la clase abstracta base de los personajes. Define los atributos y comportamientos comunes.

Atributos:

- "nombre": nombre del personaje, no puede estar vacío.
- "vida": cantidad de vida entre 0 y 100.
- "ataque": valor entero positivo que determina la capacidad de ataque.
- "defensa": valor entero no negativo que representa la protección del personaje.

Métodos principales:

- "esta_vivo()": comprueba si el personaje tiene vida superior a cero.
- "recibir_danio(cantidad)": reduce la vida y evita que sea inferior a cero. Devuelve el daño efectivo recibido.
- "mostrar_estado()": presenta los datos actuales del personaje.
- "atacar(objetivo)": método abstracto que cada subclase debe implementar.

4.2. Guerrero

Representa a un combatiente que aumenta su ataque en un 20 % y después resta la defensa del objetivo.

Fórmula:

"daño = max(0, floor(ataque * 1.2 - defensa_del_objetivo))"

4.3. Mago

Representa a un personaje que utiliza magia y cuyo ataque ignora la defensa del objetivo.

Fórmula:

"daño = ataque"

4.4. Arquero

Representa a un personaje que realiza un ataque doble cuando su ataque supera la defensa del objetivo. Si no la supera, no causa daño.

Fórmula:

Si ataque > defensa:
    daño = 2 * max(0, ataque - defensa)
En caso contrario:
    daño = 0

Los tres tipos de personajes deben estar vivos para atacar y requieren un objetivo válido que también esté vivo.

4.5. Combate

Administra el enfrentamiento entre dos personajes.

Responsabilidades:

- Inicializar los participantes y el orden de los turnos.
- Ejecutar los ataques de manera alternada.
- Mostrar el daño efectivo y el estado de los participantes.
- Verificar si existe un ganador.
- Detectar empates técnicos.
- Finalizar el combate al cumplirse una condición de terminación.

5. Diagrama UML de clases

El siguiente diagrama representa las clases y sus principales relaciones.

classDiagram
    class Personaje {
        <<abstract>>
        -nombre: str
        -vida: int
        -ataque: int
        -defensa: int
        +esta_vivo() bool
        +recibir_danio(cantidad) int
        +mostrar_estado() str
        +atacar(objetivo)* int
    }

    class Guerrero {
        +atacar(objetivo) int
    }

    class Mago {
        +atacar(objetivo) int
    }

    class Arquero {
        +atacar(objetivo) int
    }

    class Combate {
        -p1: Personaje
        -p2: Personaje
        -turno_actual: Personaje
        -ronda: int
        -ganador: Personaje
        +iniciar()
        +cambiar_turno()
        +verificar_ganador() bool
        +mostrar_resultado()
    }

    Personaje <|-- Guerrero
    Personaje <|-- Mago
    Personaje <|-- Arquero
    Combate o-- "2" Personaje : participantes

6. Aplicación de los principios de POO

Encapsulamiento

Los atributos de "Personaje" se almacenan como atributos privados y se accede a ellos mediante propiedades con validaciones. Esto evita asignar datos inválidos, como una vida superior a 100 o un ataque negativo.

Herencia

"Guerrero", "Mago" y "Arquero" heredan de "Personaje". Comparten las características comunes, pero implementan su propio método "atacar()".

Abstracción

"Personaje" es una clase abstracta. No representa un tipo concreto de combatiente y obliga a las clases derivadas a implementar "atacar()".

Polimorfismo

La clase "Combate" llama al método "atacar()" sin tener que comprobar si el atacante es un guerrero, un mago o un arquero. Python ejecuta automáticamente la implementación correspondiente al tipo de objeto.

Relaciones entre clases

- Herencia: las clases "Guerrero", "Mago" y "Arquero" heredan de "Personaje".
- Asociación: un personaje interactúa con otro cuando lo utiliza como objetivo de un ataque.
- Agregación: "Combate" mantiene referencias a los dos personajes que participan en el enfrentamiento. Los personajes se crean de forma independiente y pueden existir fuera del combate.

7. Lógica del combate

1. Se crean los personajes de manera independiente.
2. Se inicializa el combate con dos participantes.
3. Se muestra el estado inicial de ambos.
4. El primer personaje ataca al segundo.
5. Se muestra el daño efectivo y la vida actualizada.
6. Se comprueba si el combate ha terminado.
7. Si ambos siguen vivos, se alternan los turnos y continúa el enfrentamiento.
8. El combate termina cuando existe un ganador, se detecta un empate técnico o se alcanza el límite de rondas.
9. Se muestra el resultado final.

El sistema debe impedir que un personaje derrotado ataque y debe evitar que la vida de un personaje sea inferior a cero.

8. Retos adicionales

Reto 1. Pruebas automatizadas con pytest

Se incorpora el archivo "test_personajes.py" para comprobar automáticamente el comportamiento del sistema.

Las pruebas deben cubrir:

- Rechazo de nombres vacíos.
- Rechazo de valores de vida fuera del rango permitido.
- Rechazo de ataques inválidos y defensas negativas.
- Cálculo de daño de cada tipo de personaje.
- Reducción de la vida hasta cero sin valores negativos.
- Rechazo de ataques realizados por personajes derrotados.
- Rechazo de objetivos inválidos o derrotados.
- Comportamiento de la clase abstracta y sus subclases.

Reto 2. Empate técnico

Si los dos participantes completan una ronda sin causar daño efectivo, el combate debe terminar en empate técnico.

Esta condición evita que el enfrentamiento continúe indefinidamente cuando ninguno de los participantes puede reducir la vida del otro.

Reto 3. Límite máximo de rondas

El combate no puede superar las 50 rondas. Si se alcanza el límite sin determinar un ganador, el sistema debe declarar un empate técnico por límite de rondas.

Reto 4. Verificación del polimorfismo

El sistema debe ejecutar los ataques mediante el método común "atacar()", sin utilizar condicionales específicos por tipo de personaje dentro de la lógica general del combate.

9. ¿Por qué "atacar()" es abstracto y "recibir_danio()" tiene implementación?

El método "atacar()" es abstracto porque cada tipo de personaje tiene una forma diferente de calcular el daño. El guerrero aumenta su ataque, el mago ignora la defensa y el arquero duplica el daño bajo una condición determinada. Por eso, la clase base define el método, pero las clases derivadas implementan su comportamiento.

En cambio, "recibir_danio()" tiene una implementación en "Personaje" porque todos los personajes comparten la misma regla para recibir daño: reducir su vida sin permitir que sea inferior a cero y devolver el daño efectivo. Implementar esta operación una sola vez evita duplicar código y mantiene un comportamiento uniforme.

10. Instalación y ejecución

Se requiere Python 3.

Para ejecutar el programa principal:

python main.py

Para instalar pytest:

python -m pip install pytest

Para ejecutar las pruebas automatizadas:

python -m pytest -v

Si se utiliza "requirements.txt", las dependencias se pueden instalar con:

python -m pip install -r requirements.txt

11. Simulación oficial

El enfrentamiento principal se realiza entre:

Personaje| Clase| Vida inicial| Ataque| Defensa
Arthas| Guerrero| 100| 30| 20
Gandalf| Mago| 80| 40| 10

El guerrero calcula su daño aplicando el aumento del 20 % y restando la defensa del mago. El mago inflige su valor de ataque sin tener en cuenta la defensa del guerrero.

El programa muestra los turnos, el daño efectivo, la vida restante y el resultado final del combate.

12. Conclusión

Este proyecto demuestra la aplicación de los principales conceptos de la Programación Orientada a Objetos en Python. La separación de responsabilidades, las validaciones, la herencia, la abstracción y el polimorfismo permiten construir un sistema de combate organizado y extensible.

Las pruebas automatizadas y los retos adicionales ayudan a verificar el funcionamiento y a controlar situaciones especiales, como los empates técnicos y el límite máximo de rondas.