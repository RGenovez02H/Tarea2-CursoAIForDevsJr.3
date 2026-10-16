# Informe de uso de IA generativa

**Actividad:** Vibecoding guiado: desarrollo de una aplicación o mini-juego con IA como copiloto  
**Proyecto:** Atrapa las estrellas  
**Estudiante:** Renzo Genovez  
**Curso:** AI For Devs Jr. 3

## 1. Aplicación o mini-juego funcional

Desarrollé *Atrapa las estrellas*, un mini-juego en Python utilizando Pygame. El objetivo es controlar una nave espacial para atrapar estrellas, acumular puntos y evitar meteoritos.

El juego cuenta con tres vidas iniciales, puntuación de 10 puntos por estrella atrapada, dificultad progresiva, pantalla de inicio, pantalla de fin de partida y guardado local del récord en `record.txt`.

El proyecto busca aplicar los conceptos de programación mediante un juego interactivo. Las instrucciones para instalar y ejecutar el programa, así como sus controles, se encuentran en el archivo `README.md`.

## 2. Evidencia de vibecoding (prompts)

Durante el desarrollo utilicé la inteligencia artificial como copiloto para crear la estructura inicial del juego, agregar funcionalidades y mejorar su comportamiento. A continuación, se describen tres etapas del proceso.

### Prompt 1: estructura inicial

**Prompt de referencia:**

“Crea un mini-juego en Python con Pygame llamado Atrapa las estrellas. Incluye una ventana, una nave que se mueva horizontalmente, estrellas que caigan y un sistema de puntuación. Organiza el código en clases y explica las partes principales”.

**¿Qué solicité?**

Crear la base del juego, el movimiento de la nave y la puntuación.

**¿Por qué?**

Necesitaba una estructura inicial que me permitiera desarrollar el juego y comprender cómo se organizan sus componentes.

### Prompt 2: incorporación de funcionalidades

**Prompt de referencia:**

“Agrega meteoritos que resten vidas, tres vidas iniciales, una pantalla de inicio, una pantalla de fin de partida y la opción de reiniciar. Guarda el récord en un archivo local”.

**¿Qué solicité?**

Incorporar obstáculos, vidas, pantallas y guardado del récord.

**¿Por qué?**

Quería ampliar la interacción y las reglas del juego para obtener una versión más completa.

### Prompt 3: ajuste de dificultad

**Prompt de referencia:**

“Los objetos caen demasiado rápido. Reduce su velocidad y conserva el movimiento horizontal, las colisiones y la puntuación. Explica qué modificación realizaste”.

**¿Qué solicité?**

Ajustar la velocidad de caída sin modificar las demás mecánicas.

**¿Por qué?**

La solicitud se centró en un problema específico e indicó qué funcionalidades debían conservarse, facilitando la identificación del cambio realizado.

## 3. Iteración y mejora

Una mejora identificada en el código fue el ajuste del desplazamiento vertical de los objetos. En el método `Objeto.actualizar()` aparece la siguiente instrucción:

`self.y += self.velocidad * 0.4`

Esta expresión reduce el desplazamiento vertical por actualización al 40 % del valor de velocidad calculado. El propósito del cambio es controlar la velocidad de caída y mejorar la experiencia de juego.

Esta iteración demuestra cómo se puede identificar un comportamiento que necesita ajustes, solicitar una modificación concreta a la IA y revisar el código resultante. Para confirmar que la mejora es adecuada, es necesario ejecutar el juego y comprobar que las colisiones, la puntuación y las vidas sigan funcionando correctamente.

## 4. Validación del resultado

Para comprobar el funcionamiento del juego, lo ejecuté y revisé sus principales funcionalidades. Probé los controles para mover la nave, la puntuación al atrapar estrellas y la pérdida de vidas al chocar con meteoritos o dejar pasar estrellas. También comprobé el funcionamiento de las pantallas de inicio y fin de partida, la opción de reiniciar y el guardado del récord.

Durante la revisión del código identifiqué una limitación en el movimiento de los objetos: la posición vertical se actualiza sin utilizar directamente el tiempo transcurrido (`dt`). Esto podría provocar diferencias en la velocidad de caída según el rendimiento del juego.

Para ajustar este comportamiento, se utiliza la expresión `self.velocidad * 0.4` en el método `Objeto.actualizar()`, que reduce el desplazamiento vertical por actualización. Considero importante comprobar que este ajuste mantenga una dificultad adecuada y que las colisiones y demás funcionalidades continúen funcionando correctamente.
## 5. Reflexión final

El desarrollo de *Atrapa las estrellas* me permitió conocer cómo la inteligencia artificial generativa puede utilizarse como copiloto para crear funcionalidades, explicar código y proponer mejoras mediante instrucciones específicas.

Entre las ventajas del vibecoding identifico la rapidez para desarrollar una primera versión, la posibilidad de explorar soluciones y el apoyo para comprender conceptos de programación. Entre sus limitaciones están la posibilidad de recibir sugerencias incorrectas y el riesgo de incorporar código sin comprenderlo o probarlo adecuadamente.

Comprendo el objetivo general del juego, las reglas de puntuación y vidas, los controles y la función principal de las clases `Jugador`, `Objeto` y `Juego`. Necesito reforzar aspectos como el manejo del tiempo en Pygame, la lógica de las colisiones y la actualización de los objetos.

Concluyo que la IA es una herramienta útil para apoyar el desarrollo de software, pero no sustituye la comprensión ni la responsabilidad del programador. Es necesario revisar las sugerencias, entender los cambios y realizar pruebas para validar el resultado final.