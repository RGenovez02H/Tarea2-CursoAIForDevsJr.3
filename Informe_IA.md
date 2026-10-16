# Informe de uso de IA generativa

**Actividad:** Vibecoding guiado: desarrollo de una aplicación o mini-juego con IA como copiloto  
**Proyecto:** Atrapa las estrellas  
**Estudiante:** Renzo Genovez  
**Curso:** AI For Devs Jr. 3

## 1. Objetivo del proyecto

Desarrollar un mini-juego en Python con Pygame en el que el jugador controla una nave espacial para atrapar estrellas y evitar meteoritos. El juego incorpora puntuación, vidas, dificultad progresiva, pantalla inicial, pantalla de fin de partida y guardado local del récord.

## 2. Uso de IA e iteraciones

La IA se utilizó como copiloto para orientar el desarrollo, explicar partes del código y proponer mejoras. Las siguientes etapas resumen el proceso; los prompts son ejemplos de referencia y deben ajustarse a las instrucciones que realmente se utilizaron.

### Iteración 1: estructura inicial

**Prompt de referencia:**  
“Crea un mini-juego en Python con Pygame llamado Atrapa las estrellas. Incluye una ventana, una nave que se mueva horizontalmente, estrellas que caigan y una puntuación. Organiza el código en clases y explica las partes principales”.

**Objetivo:** crear la base del juego, los controles y el ciclo principal.

### Iteración 2: nuevas mecánicas

**Prompt de referencia:**  
“Agrega vidas, meteoritos que resten vidas, una pantalla inicial, una pantalla de fin de partida y la opción de reiniciar. Guarda el récord en un archivo local”.

**Objetivo:** incorporar reglas adicionales y persistencia del récord.

### Iteración 3: ajuste de dificultad

**Problema identificado:** los objetos que caían se percibían demasiado rápidos.

**Prompt de referencia:**  
“Los objetos caen demasiado rápido. Reduce su velocidad y conserva el movimiento horizontal, las colisiones y la puntuación. Explica qué modificación realizaste”.

**Cambio presente en el código:** el método `Objeto.actualizar()` contiene la instrucción `self.y += self.velocidad * 0.4`, que reduce el desplazamiento vertical por actualización al 40 % del valor de velocidad calculado.

**Validación necesaria:** ejecutar el juego y comprobar que el ritmo sea adecuado y que las demás mecánicas sigan funcionando.

## 3. Comprensión del código

- **Configuración:** define dimensiones de la ventana, FPS, vidas, puntos por estrella y colores.
- **Clase `Jugador`:** controla la posición de la nave, su movimiento y los límites de la pantalla.
- **Clase `Objeto`:** representa estrellas y meteoritos, calcula su posición y velocidad y dibuja sus figuras.
- **Clase `Juego`:** controla los estados de la partida, la creación de objetos, las colisiones, las vidas, la puntuación y la interfaz.
- **Funciones de récord:** `cargar_record()` lee el récord guardado y `guardar_record()` intenta escribirlo en `record.txt`.
- **Método `actualizar(dt)`:** utiliza el tiempo transcurrido para regular la frecuencia de aparición de objetos.

Una observación técnica es que el movimiento vertical se calcula por actualización y no se multiplica por `dt`. Por ello, su velocidad real puede depender del rendimiento y de la frecuencia efectiva de actualización.

## 4. Beneficios y riesgos del uso de IA

### Beneficios

- Acelera la creación de una primera versión funcional.
- Ayuda a comprender clases, funciones y lógica del juego.
- Permite explorar soluciones para problemas concretos.
- Facilita la documentación y la propuesta de pruebas.

### Riesgos

- El código generado puede contener errores o no cumplir exactamente los requisitos.
- Un cambio en la velocidad puede afectar la dificultad y la experiencia de juego.
- La apariencia de funcionamiento correcto no sustituye las pruebas.
- Aceptar código sin comprenderlo dificulta el mantenimiento y la corrección de errores.

Por estas razones, las sugerencias de IA deben revisarse, comprenderse y probarse. La responsabilidad de validar el resultado final corresponde al desarrollador.

## 5. Reflexión final

La IA generativa puede acelerar el desarrollo y servir como apoyo para comprender código, explorar soluciones y mejorar una aplicación. Sin embargo, no reemplaza el criterio técnico del desarrollador. La experiencia de ajustar la velocidad demuestra la importancia de identificar un problema, aplicar un cambio concreto y comprobar que la mejora no afecte las demás funcionalidades.

El uso responsable de IA implica revisar las propuestas, comprender las modificaciones y validar el comportamiento del programa antes de considerar terminada la tarea.