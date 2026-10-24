# Guardians of the Ancient Kingdom

**Proyecto Integrador — Parcial II (Programación Orientada a Objetos)**  
**Estudiante:** [Tu Nombre Completo]  
**Asignatura:** Programación Orientada a Objetos con Python  


## 1. Descripción del Proyecto

**Guardians of the Ancient Kingdom** es un sistema de combate por turnos programado en Python que simula los enfrentamientos entre tres órdenes de guardianes del reino de Eldoria: **Guerreros**, **Magos** y **Arqueros**.

El proyecto resuelve la necesidad de automatizar los combates, controlando de forma segura las reglas de ataque de cada personaje, el cálculo de daño según su habilidad especial, las validaciones de vida y el flujo de turnos hasta determinar un vencedor o un empate.


## 2. Estructura del Repositorio

- `personajes.py`: Contiene la definición de la clase base abstracta `Personaje`, las subclases (`Guerrero`, `Mago`, `Arquero`) y la clase `Combate`. Define la lógica, el encapsulamiento y los comportamientos del sistema.
- `main.py`: Archivo principal encargado de instanciar los objetos, demostrar los casos de prueba manuales y ejecutar la suite de pruebas automatizadas con Pytest.
- `README.md`: Documentación completa del sistema, explicaciones teóricas/prácticas de POO y evidencia de los retos adicionales.


## 3. Clases y Responsabilidades

- **`Personaje` (Clase Abstracta):** Define y encapsula los atributos comunes (`nombre`, `vida`, `ataque`, `defensa`). Contiene los métodos compartidos como `recibir_danio()`, `esta_vivo()` y define la firma abstracta de `atacar(objetivo)`.
- **`Guerrero` (Subclase):** Aplica la habilidad *Golpe poderoso* (aumenta su ataque un 20% antes de restar la defensa enemiga).
- **`Mago` (Subclase):** Aplica la habilidad *Hechizo penetrante* (ignora completamente la defensa del rival).
- **`Arquero` (Subclase):** Aplica la habilidad *Disparo crítico* (duplica el daño base si su ataque supera la defensa).
- **`Combate`:** Administrador independiente del enfrentamiento. Maneja turnos, verifica condiciones de victoria, límites de rondas y empates técnicos.


## 4. Relaciones entre Clases

1. **Herencia:** `Guerrero`, `Mago` y `Arquero` heredan de `Personaje` (`Guerrero is-a Personaje`).
2. **Asociación:** Ocurre cuando un personaje ejecuta `atacar(objetivo)`, interactuando directamente con el método `recibir_danio()` de la instancia objetivo.
3. **Agregación:** La clase `Combate` recibe dos objetos `Personaje` creados independientemente fuera de ella (`Combate has-a Personaje`).


## 5. Aplicación de Conceptos de POO

- **Abstracción:** Se modela la esencia de un combatiente en `Personaje` sin permitir instancias directas, delegando la implementación específica del ataque a las subclases.
- **Encapsulamiento:** Atributos protegidos con prefijo `_` (`_nombre`, `_vida`, `_ataque`, `_defensa`) accesibles mediante getters y setters con validaciones estrictas.
- **Polimorfismo:** En `Combate`, la llamada `atacante.atacar(defensor)` ejecuta dinámicamente la habilidad especial de cada subclase sin necesidad de condicionales sobre el tipo de objeto.


## 6. Lógica de Combate y Reglas de Daño

- **Guerrero:** Daño = máximo(0, floor(ataque * 1.20) - defensa_objetivo)
- **Mago:** Daño = ataque_mago (ignora la defensa enemiga)
- **Arquero:** Si ataque > defensa_objetivo, Daño = (ataque - defensa_objetivo) * 2. De lo contrario, 0.


## 7. Instrucciones de Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd Guardians-of-the-Ancient-Kingdom


1. Ejecutar simulación y pruebas manuales:
python main.py

2. Ejecutar pruebas automatizadas con Pytest:
pip install pytest
pytest main.py


8. Casos de Prueba Verificados
**Se verificaron los 12 casos obligatorios exigidos:

**Creación correcta de los tres tipos de personajes.

**Rechazo de valores de vida superiores a 100 o negativos.

**Rechazo de nombres vacíos.

**Rechazo de ataques y defensas fuera de los rangos válidos.

**Cálculo del ataque potenciado del Guerrero.

**Aplicación del ataque del Mago ignorando defensa.

**Disparo crítico del Arquero cuando supera la defensa.

**Control de vida mínima en cero (sin valores negativos).

**Bloqueo de ataque si el atacante está derrotado.

**Simulación completa de combate por turnos.

**Determinación y reporte del ganador.

**Finalización por empate técnico cuando ningún personaje causa daño.

# RETOS PARA LA CALIFICACIÓN MÁXIMA (5.0)
 Reto Extra 1 — Diagrama de Clases UML
 classDiagram
    class Personaje {
        <<Abstract>>
        - str _nombre
        - int _vida
        - int _ataque
        - int _defensa
        + nombre() str
        + vida() int
        + ataque() int
        + defensa() int
        + recibir_danio(cantidad: int) int
        + esta_vivo() bool
        + mostrar_estado() str
        + atacar(objetivo: Personaje)* int
    }

    class Guerrero {
        + atacar(objetivo: Personaje) int
    }

    class Mago {
        + atacar(objetivo: Personaje) int
    }

    class Arquero {
        + atacar(objetivo: Personaje) int
    }

    class Combate {
        + Personaje p1
        + Personaje p2
        + Personaje turno_actual
        + Personaje siguiente_turno
        + Personaje ganador
        + bool empate
        + cambiar_turno()
        + verificar_ganador() bool
        + iniciar(verbose: bool)
        + mostrar_resultado()
    }

    Personaje <|-- Guerrero : Herencia
    Personaje <|-- Mago : Herencia
    Personaje <|-- Arquero : Herencia
    Combate o-- Personaje : Agregación
    Personaje ..> Personaje : Asociación (Atacar)
