# 2048 Game
Implementación del juego 2048 en Python, siguiendo la metodología TDD.

**Descripción**

Este proyecto es una implementación del juego 2048, utilizando Python. El objetivo del juego es combinar fichas de valores iguales en un tablero 4x4 para llegar a la ficha con el valor 2048. Está desarrollado siguiendo la metodología TDD (Test-Driven Development), asegurando que el código esté respaldado por pruebas unitarias en cada paso. 

**Características**

- Movimiento de fichas en cuatro direcciones (izquierda, derecha, arriba, abajo)
- Fusión de fichas con el mismo valor
- Generación aleatoria de nuevas fichas (2 o 4)
- Pruebas unitarias para la lógica de juego

**Requisitos**

- Python 3.x

**Instalación**

1. Clonar repositorio: 

git clone https://github.com/TheFuryUsS/2048_Game

2. Acceder al directorio del proyecto

cd 2048_Game

3. Instala las dependencias

pip install -r requirements.txt

4. Ejecutar el juego: 

python game.py

**Cómo jugar**

Para mover las fichas hay que utilizar las flechas del teclado:
    - Izquierda, derecha, arriba, abajo

Cuando dos fichas con el mismo valor se encuentran, se fusionan en
una sola ficha con el valor combinado.

El juego termina cuando no hay más movimientos posibles o cuando se alcanza la ficha con el valor 2048. 
