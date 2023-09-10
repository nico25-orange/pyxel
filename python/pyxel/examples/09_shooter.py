import pyxel

# Configuration
SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2

NUM_STARS = 100
STAR_COLOR_HIGH = 12
STAR_COLOR_LOW = 5

PLAYER_WIDTH = 8
PLAYER_HEIGHT = 8
PLAYER_SPEED = 2

BULLET_WIDTH = 2
BULLET_HEIGHT = 8
BULLET_COLOR = 11
BULLET_SPEED = 4

ENEMY_WIDTH = 8
ENEMY_HEIGHT = 8
ENEMY_SPEED = 1.5

BLAST_START_RADIUS = 1
BLAST_END_RADIUS = 8
BLAST_COLOR_IN = 7
BLAST_COLOR_OUT = 10

enemies = []
bullets = []
blasts = []

def update_list(list):
    for elem in list:
        elem.update()

def draw_list(list):
    for elem in list:
        elem.draw()

def cleanup_list(list):
    i = 0
    while i < len(list):
        elem = list[i]
        if not elem.is_alive:
            list.pop(i)
        else:
            i += 1

class Background:
    def __init__(self):
        self.stars = []
        for i in range(NUM_STARS):
            self.stars.append(
                (
                pyxel.rndi(0, pyxel.width - 1),
                pyxel.rndi(0, pyxel.height -1),
                pyxel.rndf(1, 2.5),
                )
            )

    def update(self):
        for i, (x, y, speed) in enumerate(self.stars):
            y += speed
            if y >= pyxel.height:
                y -= pyxel.height
            self.stars[i] = (x, y, speed)

    def draw(self):
        for x, y, speed in self.stars:
            pyxel.pset(x, y, STAR_COLOR_HIGH if speed > 1.8 else STAR_COLOR_LOW)
