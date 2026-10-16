
import random
import math
import sys
from pathlib import Path

import pygame

# ---------------- CONFIGURACIÓN ----------------
ANCHO, ALTO = 900, 600
FPS = 60
VIDAS_INICIALES = 3
PUNTOS_ESTRELLA = 10

FONDO = (13, 20, 48)
BLANCO = (245, 248, 255)
AMARILLO = (255, 220, 85)
AZUL = (46, 107, 220)
CELESTE = (78, 220, 255)
ROJO = (255, 82, 100)
NARANJA = (255, 135, 70)
MORADO = (150, 115, 255)

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atrapa las estrellas")
reloj = pygame.time.Clock()

fuente = pygame.font.Font(None, 30)
fuente_grande = pygame.font.Font(None, 68)
fuente_titulo = pygame.font.Font(None, 82)

ARCHIVO_RECORD = Path(__file__).resolve().parent / "record.txt"


def cargar_record():
    """Carga el récord guardado o devuelve cero."""
    try:
        return max(0, int(ARCHIVO_RECORD.read_text(encoding="utf-8").strip()))
    except (OSError, ValueError):
        return 0


def guardar_record(record):
    """Guarda el récord en un archivo local."""
    try:
        ARCHIVO_RECORD.write_text(str(record), encoding="utf-8")
    except OSError:
        print("Aviso: no se pudo guardar el récord.")


def dibujar_texto(texto, fuente_usada, color, x, y):
    imagen = fuente_usada.render(str(texto), True, color)
    rectangulo = imagen.get_rect(center=(x, y))
    pantalla.blit(imagen, rectangulo)


def crear_fondo():
    """Genera estrellas decorativas para el fondo espacial."""
    return [
        (random.randrange(ANCHO), random.randrange(ALTO),
         random.choice([1, 1, 2, 2, 3]))
        for _ in range(100)
    ]


class Jugador:
    def __init__(self):
        self.ancho = 76
        self.alto = 44
        self.x = ANCHO // 2
        self.y = ALTO - 75
        self.velocidad = 7

    @property
    def rectangulo(self):
        return pygame.Rect(
            self.x - self.ancho // 2,
            self.y - self.alto // 2,
            self.ancho,
            self.alto
        )

    def actualizar(self, teclas):
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.x -= self.velocidad

        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.x += self.velocidad

        # Impide que el jugador salga de la pantalla.
        self.x = max(
            self.ancho // 2,
            min(ANCHO - self.ancho // 2, self.x)
        )

    def dibujar(self):
        x, y = self.x, self.y

        puntos = [
            (x, y - 24),
            (x + 38, y + 20),
            (x - 38, y + 20)
        ]

        pygame.draw.polygon(pantalla, AZUL, puntos)
        pygame.draw.polygon(pantalla, CELESTE, puntos, 3)
        pygame.draw.ellipse(
            pantalla, MORADO,
            (x - 12, y - 4, 24, 18)
        )
        pygame.draw.circle(pantalla, BLANCO, (x, y + 2), 4)


class Objeto:
    def __init__(self, tipo, dificultad):
        self.tipo = tipo
        self.tamano = random.randint(16, 24) if tipo == "estrella" else 25
        self.x = random.randint(self.tamano, ANCHO - self.tamano)
        self.y = -self.tamano

        velocidad_base = random.uniform(2.5, 4.0)
        self.velocidad = velocidad_base + dificultad
        self.fase = random.random() * math.tau

    @property
    def rectangulo(self):
        margen = self.tamano * 0.3
        return pygame.Rect(
            int(self.x - self.tamano + margen),
            int(self.y - self.tamano + margen),
            int((self.tamano - margen) * 2),
            int((self.tamano - margen) * 2)
        )

    def actualizar(self):
        self.y += self.velocidad * 0.4
        self.x += math.sin(self.y / 35 + self.fase) * 1.2
        self.x = max(self.tamano, min(ANCHO - self.tamano, self.x))

    def dibujar(self):
        x, y, r = int(self.x), int(self.y), self.tamano

        if self.tipo == "estrella":
            puntos = []

            for i in range(10):
                angulo = -math.pi / 2 + i * math.pi / 5
                radio = r if i % 2 == 0 else r * 0.45

                puntos.append((
                    int(x + math.cos(angulo) * radio),
                    int(y + math.sin(angulo) * radio)
                ))

            pygame.draw.polygon(pantalla, AMARILLO, puntos)
            pygame.draw.polygon(pantalla, BLANCO, puntos, 2)

        else:
            pygame.draw.circle(pantalla, NARANJA, (x, y), r)
            pygame.draw.circle(pantalla, ROJO, (x - 4, y - 4), int(r * 0.65))
            pygame.draw.circle(pantalla, (120, 47, 78), (x + 7, y + 5), 7)


class Juego:
    def __init__(self):
        self.record = cargar_record()
        self.estado = "inicio"
        self.reiniciar()

        self.estrellas_fondo = crear_fondo()

    def reiniciar(self):
        self.jugador = Jugador()
        self.objetos = []
        self.puntos = 0
        self.vidas = VIDAS_INICIALES
        self.temporizador = 0

    def crear_objeto(self):
        # La probabilidad de meteoritos aumenta con la puntuación.
        probabilidad = min(0.20 + self.puntos / 1500, 0.40)
        tipo = "meteorito" if random.random() < probabilidad else "estrella"
        dificultad = min(self.puntos / 500, 3)
        self.objetos.append(Objeto(tipo, dificultad))

    def procesar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return False

                if self.estado in ("inicio", "fin"):
                    if evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                        self.reiniciar()
                        self.estado = "jugando"

        return True

    def actualizar(self, dt):
        if self.estado != "jugando":
            return

        teclas = pygame.key.get_pressed()
        self.jugador.actualizar(teclas)

        # Los objetos aparecen progresivamente más rápido.
        intervalo = max(0.30, 0.80 - self.puntos / 2000)
        self.temporizador += dt

        if self.temporizador >= intervalo:
            self.temporizador = 0
            self.crear_objeto()

        for objeto in self.objetos[:]:
            objeto.actualizar()

            if objeto.rectangulo.colliderect(self.jugador.rectangulo):
                if objeto.tipo == "estrella":
                    self.puntos += PUNTOS_ESTRELLA
                else:
                    self.vidas -= 1

                self.objetos.remove(objeto)
                continue

            # Perder una estrella también resta una vida.
            if objeto.y - objeto.tamano > ALTO:
                if objeto.tipo == "estrella":
                    self.vidas -= 1

                self.objetos.remove(objeto)

        if self.puntos > self.record:
            self.record = self.puntos
            guardar_record(self.record)

        if self.vidas <= 0:
            self.vidas = 0
            self.estado = "fin"

    def dibujar_fondo(self):
        pantalla.fill(FONDO)

        for x, y, radio in self.estrellas_fondo:
            pygame.draw.circle(
                pantalla, (120, 154, 220), (x, y), radio
            )

    def dibujar_hud(self):
        pygame.draw.rect(pantalla, (11, 17, 40), (0, 0, ANCHO, 62))

        pantalla.blit(
            fuente.render(f"Puntos: {self.puntos}", True, BLANCO),
            (20, 18)
        )

        dibujar_texto(
            f"Récord: {self.record}",
            fuente, AMARILLO, ANCHO // 2, 30
        )

        pantalla.blit(
            fuente.render(f"Vidas: {self.vidas}", True, ROJO),
            (ANCHO - 145, 18)
        )

    def dibujar_inicio(self):
        self.dibujar_fondo()

        dibujar_texto(
            "ATRAPA LAS", fuente_titulo, BLANCO,
            ANCHO // 2, 180
        )

        dibujar_texto(
            "ESTRELLAS", fuente_titulo, AMARILLO,
            ANCHO // 2, 250
        )

        dibujar_texto(
            "Atrapa estrellas y esquiva meteoritos",
            fuente, BLANCO, ANCHO // 2, 325
        )

        dibujar_texto(
            "Flechas o A/D para moverte",
            fuente, CELESTE, ANCHO // 2, 380
        )

        dibujar_texto(
            "Presiona ENTER para jugar",
            fuente, BLANCO, ANCHO // 2, 445
        )

        dibujar_texto(
            f"Récord: {self.record}",
            fuente, AMARILLO, ANCHO // 2, 500
        )

    def dibujar_fin(self):
        capa = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
        capa.fill((5, 8, 25, 210))
        pantalla.blit(capa, (0, 0))

        dibujar_texto(
            "FIN DE LA PARTIDA", fuente_grande, ROJO,
            ANCHO // 2, 220
        )

        dibujar_texto(
            f"Puntuación: {self.puntos}",
            fuente, BLANCO, ANCHO // 2, 305
        )

        dibujar_texto(
            f"Récord: {self.record}",
            fuente, AMARILLO, ANCHO // 2, 350
        )

        dibujar_texto(
            "ENTER para volver a jugar",
            fuente, CELESTE, ANCHO // 2, 420
        )

        dibujar_texto(
            "ESC para salir",
            fuente, BLANCO, ANCHO // 2, 465
        )

    def dibujar(self):
        if self.estado == "inicio":
            self.dibujar_inicio()
        else:
            self.dibujar_fondo()

            for objeto in self.objetos:
                objeto.dibujar()

            self.jugador.dibujar()
            self.dibujar_hud()

            if self.estado == "fin":
                self.dibujar_fin()

        pygame.display.flip()

    def ejecutar(self):
        activo = True

        while activo:
            dt = min(reloj.tick(FPS) / 1000, 0.05)

            activo = self.procesar_eventos()
            self.actualizar(dt)
            self.dibujar()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Juego().ejecutar()
