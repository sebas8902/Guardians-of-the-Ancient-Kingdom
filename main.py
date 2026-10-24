from personajes import Guerrero, Mago, Arquero, Combate
import pytest


# ==========================================
# PRUEBAS AUTOMATIZADAS (RETO 2 - PYTEST)
# ==========================================

def test_creacion_personaje_valido():
    guerrero = Guerrero("Arthas", 100, 30, 20)
    assert guerrero.nombre == "Arthas"
    assert guerrero.vida == 100
    assert guerrero.ataque == 30
    assert guerrero.defensa == 20


def test_rechazo_valores_incorrectos():
    with pytest.raises(ValueError):
        Guerrero("", 100, 30, 20)
    with pytest.raises(ValueError):
        Mago("Gandalf", 150, 40, 10)
    with pytest.raises(ValueError):
        Arquero("Legolas", -10, 30, 5)
    with pytest.raises(ValueError):
        Arquero("Legolas", 80, -10, 5)
    with pytest.raises(ValueError):
        Guerrero("Arthas", 100, 30, -5)


def test_calculo_danio_clases():
    guerrero = Guerrero("Arthas", 100, 30, 20)
    mago = Mago("Gandalf", 80, 40, 10)
    arquero = Arquero("Legolas", 90, 35, 15)
    
    # Guerrero vs Mago (Daño esperado: 26)
    objetivo_m = Mago("ObjetivoM", 80, 20, 10)
    danio_g = guerrero.atacar(objetivo_m)
    assert danio_g == 26

    # Mago vs Guerrero (Daño esperado: 40, ignora defensa)
    objetivo_g = Guerrero("ObjetivoG", 100, 20, 20)
    danio_m = mago.atacar(objetivo_g)
    assert danio_m == 40

    # Arquero vs Guerrero (Daño esperado: 40, duplica base)
    objetivo_a = Guerrero("ObjetivoA", 100, 20, 15)
    danio_a = arquero.atargui(objetivo_a) if hasattr(arquero, 'atargui') else arquero.atacar(objetivo_a)
    assert danio_a == 40


def test_vida_no_negativa():
    objetivo = Guerrero("Objetivo", 20, 20, 10)
    mago = Mago("Gandalf", 80, 40, 10)
    mago.atacar(objetivo)
    assert objetivo.vida == 0


def test_personaje_derrotado_no_puede_atacar():
    derrotado = Guerrero("Derrotado", 0, 20, 0)
    rival = Mago("Rival", 80, 40, 10)
    with pytest.raises(ValueError):
        derrotado.atacar(rival)


def test_combate_resultado_ganador():
    arthas = Guerrero("Arthas", 100, 30, 20)
    gandalf = Mago("Gandalf", 80, 40, 10)
    combate = Combate(arthas, gandalf)
    combate.iniciar()
    assert combate.ganador == gandalf


# ==========================================
# EJECUCIÓN MANUAL Y SIMULACIONES
# ==========================================

def ejecutar_casos_de_prueba():
    print("Verificación de validaciones y casos de prueba:\n")

    print("Prueba de empate técnico:")
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
    