from abc import ABC, abstractmethod
import math


class Personaje(ABC):
    def __init__(self, nombre: str, vida: int, ataque: int, defensa: int):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def vida(self) -> int:
        return self.__vida

    @vida.setter
    def vida(self, valor: int):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise ValueError("La vida debe ser un número entero.")
        if not 0 <= valor <= 100:
            raise ValueError(
                "La vida debe ser un número entero entre 0 y 100."
            )
        self.__vida = valor

    @property
    def ataque(self) -> int:
        return self.__ataque

    @ataque.setter
    def ataque(self, valor: int):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise ValueError("El ataque debe ser un número entero.")
        if valor <= 0:
            raise ValueError("El ataque debe ser un entero positivo.")
        self.__ataque = valor

    @property
    def defensa(self) -> int:
        return self.__defensa

    @defensa.setter
    def defensa(self, valor: int):
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise ValueError("La defensa debe ser un número entero.")
        if valor < 0:
            raise ValueError(
                "La defensa debe ser un entero no negativo."
            )
        self.__defensa = valor

    def esta_vivo(self) -> bool:
        return self.__vida > 0

    def recibir_danio(self, cantidad: int) -> int:
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise ValueError("El daño debe ser un número entero.")

        if cantidad < 0:
            raise ValueError("El daño no puede ser negativo.")

        vida_anterior = self.__vida
        self.__vida = max(0, self.__vida - cantidad)

        return vida_anterior - self.__vida

    def mostrar_estado(self) -> str:
        return (
            f"{self.__nombre} [Vida: {self.__vida} | "
            f"Ataque: {self.__ataque} | Defensa: {self.__defensa}]"
        )

    @abstractmethod
    def atacar(self, objetivo):
        pass


class Guerrero(Personaje):
    def atacar(self, objetivo) -> int:
        if not self.esta_vivo():
            raise ValueError(
                f"{self.nombre} está derrotado y no puede atacar."
            )

        if not isinstance(objetivo, Personaje):
            raise ValueError("El objetivo no es válido.")

        if not objetivo.esta_vivo():
            raise ValueError("El objetivo está derrotado.")

        calculo = (self.ataque * 1.20) - objetivo.defensa
        danio_final = max(0, math.floor(calculo))

        return objetivo.recibir_danio(danio_final)


class Mago(Personaje):
    def atacar(self, objetivo) -> int:
        if not self.esta_vivo():
            raise ValueError(
                f"{self.nombre} está derrotado y no puede atacar."
            )

        if not isinstance(objetivo, Personaje):
            raise ValueError("El objetivo no es válido.")

        if not objetivo.esta_vivo():
            raise ValueError("El objetivo está derrotado.")

        danio_final = self.ataque

        return objetivo.recibir_danio(danio_final)


class Arquero(Personaje):
    def atacar(self, objetivo) -> int:
        if not self.esta_vivo():
            raise ValueError(
                f"{self.nombre} está derrotado y no puede atacar."
            )

        if not isinstance(objetivo, Personaje):
            raise ValueError("El objetivo no es válido.")

        if not objetivo.esta_vivo():
            raise ValueError("El objetivo está derrotado.")

        base = max(0, self.ataque - objetivo.defensa)

        if self.ataque > objetivo.defensa:
            danio_final = base * 2
        else:
            danio_final = 0

        return objetivo.recibir_danio(danio_final)


class Combate:
    def __init__(self, p1: Personaje, p2: Personaje):
        if not isinstance(p1, Personaje) or not isinstance(p2, Personaje):
            raise ValueError(
                "Los participantes deben ser objetos de tipo Personaje."
            )

        self.p1 = p1
        self.p2 = p2
        self.turno_actual = p1
        self.defensor_actual = p2
        self.ronda = 0
        self.ganador = None

    def cambiar_turno(self):
        if self.turno_actual == self.p1:
            self.turno_actual = self.p2
            self.defensor_actual = self.p1
        else:
            self.turno_actual = self.p1
            self.defensor_actual = self.p2

    def verificar_ganador(self) -> bool:
        if not self.p1.esta_vivo() and self.p2.esta_vivo():
            self.ganador = self.p2
            return True

        if not self.p2.esta_vivo() and self.p1.esta_vivo():
            self.ganador = self.p1
            return True

        if not self.p1.esta_vivo() and not self.p2.esta_vivo():
            self.ganador = "Empate (Ambos cayeron en combate)"
            return True

        return False

    def iniciar(self):
        print(f"Combate: {self.p1.nombre} vs {self.p2.nombre}")
        print(f"Participante 1: {self.p1.mostrar_estado()}")
        print(f"Participante 2: {self.p2.mostrar_estado()}")
        print()

        max_rondas = 50

        while self.ronda < max_rondas:
            if self.verificar_ganador():
                break

            self.ronda += 1
            danio_primero = 0
            danio_segundo = 0

            atacante = self.turno_actual
            defensor = self.defensor_actual

            if atacante.esta_vivo() and defensor.esta_vivo():
                danio_primero = atacante.atacar(defensor)

                print(
                    f"Turno {((self.ronda - 1) * 2) + 1:02d} | "
                    f"Ataca {atacante.nombre} "
                    f"({type(atacante).__name__}) - "
                    f"Daño infligido: {danio_primero}"
                )
                print(
                    f"          Estado: {self.p1.nombre}: "
                    f"{self.p1.vida} HP | {self.p2.nombre}: "
                    f"{self.p2.vida} HP"
                )
                print()

            if self.verificar_ganador():
                break

            self.cambiar_turno()

            atacante = self.turno_actual
            defensor = self.defensor_actual

            if atacante.esta_vivo() and defensor.esta_vivo():
                danio_segundo = atacante.atacar(defensor)

                print(
                    f"Turno {((self.ronda - 1) * 2) + 2:02d} | "
                    f"Ataca {atacante.nombre} "
                    f"({type(atacante).__name__}) - "
                    f"Daño infligido: {danio_segundo}"
                )
                print(
                    f"          Estado: {self.p1.nombre}: "
                    f"{self.p1.vida} HP | {self.p2.nombre}: "
                    f"{self.p2.vida} HP"
                )
                print()

            if self.verificar_ganador():
                break

            if danio_primero == 0 and danio_segundo == 0:
                self.ganador = "Empate técnico (Ningún personaje causó daño)"
                break

            self.cambiar_turno()

        if not self.ganador and self.ronda >= max_rondas:
            self.ganador = (
                "Empate técnico (Límite de 50 rondas alcanzado)"
            )

        self.mostrar_resultado()

    def mostrar_resultado(self):
        print()
        print("Resultado final del combate:")

        if isinstance(self.ganador, Personaje):
            print(
                f"Ganador: {self.ganador.nombre} "
                f"({type(self.ganador).__name__})"
            )
        else:
            print(f"Resultado: {self.ganador}")

        print("Estado final:")
        print(f"{self.p1.mostrar_estado()}")
        print(f"{self.p2.mostrar_estado()}")