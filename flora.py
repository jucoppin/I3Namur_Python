import turtle
import time
import math

WIDTH = 400
HEIGHT = 300
PLAYER_WIDTH = 10
pos_x = 50
pos_y = 0

window = turtle.Screen()  # pour crée une fenetre pour le jeux
window.title("ping pong first game")  # titre du jeux
window.bgcolor("darkgrey")  # pour la couleur d'arriere plan
window.setup(width=WIDTH * 2, height=HEIGHT * 2)  # pour dimensioner la taille de la fenetre
window.tracer(0)  # pour arreter que la fenetre du jeu s'update constament


class Player(turtle.Turtle):
    SPEED = 20

    def __init__(self, shape: str, color: str, start_pos: int, end_pos: int):
        super().__init__()

        self.start_pos = start_pos
        self.end_pos = end_pos
        self.score = 0

        self.speed(0)  # pour la vitesse d'animation
        self.shape(shape)  # pour donner une forme a ton joueur dans ce cas ci c'est un carré
        self.color(color)  # couleur du joueur

        self.height_size = 100
        self.width_size = 20

        self.shapesize(stretch_len=self.width_size / 20, stretch_wid=self.height_size / 20)

        self.penup()
        self.reset_position()

    def reset_position(self):
        self.goto(self.start_pos, self.end_pos)

    def up(self):
        self.sety(self.ycor() + Player.SPEED)

    def down(self):
        self.sety(self.ycor() - Player.SPEED)

    def get_x(self):
        return abs(self.xcor()) - self.width_size / 2

    def get_y(self):
        return abs(self.ycor()) - self.height_size / 2


class Ball(turtle.Turtle):
    def __init__(self, shape: str, color: str, start_pos: int = 0, end_pos: int = 0):
        super().__init__()

        self.start_pos = start_pos
        self.end_pos = end_pos
        self.score = 0

        self.speed(0)  # pour la vitesse d'animation
        self.shape(shape)  # pour donner une forme a ton joueur dans ce cas ci c'est un carré
        self.color(color)  # couleur du joueur

        self.height_size = 20
        self.width_size = 20

        self.shapesize(stretch_len=self.width_size / 20, stretch_wid=self.height_size / 20)

        self.penup()
        self.reset_position()

        self.speed_x = 10
        self.speed_y = 0

    def reset_position(self):
        self.goto(self.start_pos, self.end_pos)

    def move(self, left: Player, right: Player):
        ycor = self.ycor() + self.speed_y  # Target Y position
        if ycor < -HEIGHT + self.height_size:
            self.speed_y = -self.speed_y
            ycor = -HEIGHT + self.height_size
        elif ycor > HEIGHT - self.height_size:
            self.speed_y = -self.speed_y
            ycor = HEIGHT - self.height_size
        self.sety(ycor)
        xcor = self.xcor() + self.speed_x
        if xcor < 0:
            self.test_player_impact(left, xcor, ycor)
        elif xcor > 0:
            self.test_player_impact(right, xcor, ycor)
        else:
            self.setx(xcor)

    def test_player_impact(self, player: Player, x: float, y: float):
        player_x = player.get_x()
        player_y = player.get_y()

        if player_x - player.width_size / 2 <= x <= player_x + player.width_size / 4:
            self.reverse()

        self.setx(x)

    def reverse(self):
        self.speed_x = -self.speed_x
        self.speed_y = -self.speed_y


droite = Player("square", "green", WIDTH - pos_x, pos_y)
gauche = Player("square", "lightblue", -(WIDTH - pos_x), pos_y)
balle = Ball("circle", "red")

# keyboard binding
window.listen()
window.onkeypress(droite.up, "p")
window.onkeypress(droite.down, "m")

window.onkeypress(gauche.up, "a")
window.onkeypress(gauche.down, "w")
window.onkeypress(gauche.down, "q")

# boucle principale
while True:
    window.update()

    # move the ball
    balle.move(gauche, droite)
    # border checking (ce que l'on veu que cela fasse quand la balle touche les bord)

    """
    if balle.ycor() > 290:
        balle.sety(290)
        balle.dy *= -1
    if balle.ycor() < -290:
        balle.sety(-290)
        balle.dy *= -1
    # lorsque la balle passe derière le camp le point ira au tireur après x fois on annonce le gagnant
    if balle.xcor() < -390:
        balle.goto(0, 0)
        balle.dx *= -1
        # scored+=1

    if balle.xcor() < 390:
        balle.goto(0, 0)
        balle.dx *= -1

    # colision joueur/balle verifier si les +et les- sont a gauche ou droite

    if (balle.xcor() > 340 and balle.xcor() < 350) and (balle.ycor() < droite.ycor() + 40 and balle.ycor() > droite.ycor() - 40):
        balle.setx(340)
        balle.dx *= -1

    if (balle.xcor() > -340 and balle.xcor() > -350) and (balle.ycor() < droite.ycor() + 40 and balle.ycor() > gauche.ycor() - 40):
        balle.setx(-340)
        balle.dx *= -1
    """

    time.sleep(0.1)
