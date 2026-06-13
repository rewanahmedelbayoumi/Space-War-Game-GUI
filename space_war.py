import turtle
import random
import time
from tkinter import *
from tkinter import colorchooser

class GameObject(turtle.Turtle):
    def __init__(self, shape, color, x, y):
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.shapesize(stretch_wid=1, stretch_len=1)

class SpaceCraft(GameObject):
    def __init__(self, color, x, y, controls):
        super().__init__("triangle", color, x, y)
        self.__speed = 0
        self.__rotation_speed = 15
        self.__controls = controls
        self.__points = 0
        self.setheading(90)
    
    def get_points(self):
        return self.__points
    
    def add_points(self, amount):
        self.__points += amount
    
    def rotate_left(self):
        self.left(self.__rotation_speed)
    
    def rotate_right(self):
        self.right(self.__rotation_speed)
    
    def accelerate(self):
        self.__speed = min(5, self.__speed + 0.5)
    
    def decelerate(self):
        self.__speed = max(0, self.__speed - 0.2)
    
    def move(self):
        self.forward(self.__speed)

class Ball(GameObject):
    def __init__(self, color, x, y):
        super().__init__("circle", color, x, y)
        self.shapesize(0.5, 0.5)
        self.__is_gift = random.random() < 0.1
    
    def is_gift(self):
        return self.__is_gift
    
    def respawn(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
        self.__is_gift = random.random() < 0.1
        if self.__is_gift:
            self.color("gold")
        else:
            self.color(game.ball_color)

class GiftBox(GameObject):
    def __init__(self, x, y):
        super().__init__("square", "gold", x, y)
        self.shapesize(1, 1)
        self.__points_value = random.randint(5, 20)
    
    def get_points_value(self):
        return self.__points_value

class Game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(800, 600)
        self.screen.title("Space War")
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        
        self.spacecraft_color = "white"
        self.ball_color = "red"
        self.game_mode = None
        self.players = []
        self.balls = []
        self.gift_boxes = []
        
        self.score_displays = []
        
        self.setup_menu()
    
    def setup_menu(self):
        self.menu = Tk()
        self.menu.title("Space War Menu")
        
        Label(self.menu, text="Welcome to Space War!", font=("Arial", 20)).pack(pady=20)     #pack,grid,place
        
        Label(self.menu, text="Space Craft Color:").pack()
        Button(self.menu, text="Choose", command=self.choose_spacecraft_color).pack()
        
        Label(self.menu, text="Balls Color:").pack()
        Button(self.menu, text="Choose", command=self.choose_ball_color).pack()
        
        Label(self.menu, text="Game Mode:").pack(pady=10)
        Button(self.menu, text="1 Player", command=lambda: self.start_game(1)).pack()
        Button(self.menu, text="Multiplayer", command=lambda: self.start_game(2)).pack()
        
        self.menu.mainloop()
    
    def choose_spacecraft_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.spacecraft_color = color
    
    def choose_ball_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.ball_color = color

    def start_game(self, num_players):
        self.game_mode = num_players
        self.menu.destroy()
        self.initialize_game()
        self.run_game()
    
    def initialize_game(self):
        if self.game_mode == 1:
            self.players.append(SpaceCraft(self.spacecraft_color, 0, 0, "arrows"))
        else:
            self.screen.setup(800, 600)
            self.players.append(SpaceCraft(self.spacecraft_color, -100, 0, "arrows"))
            self.players.append(SpaceCraft(self.spacecraft_color, 100, 0, "wasd"))
        
        for _ in range(15):
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            self.balls.append(Ball(self.ball_color, x, y))
        
        for i, player in enumerate(self.players):
            display = turtle.Turtle()
            display.color("white")
            display.penup()
            display.hideturtle()
            display.goto(-380 if i == 0 else 100, 260)
            self.score_displays.append(display)
        
        self.update_scores()
    
    def update_scores(self):
        for i, (player, display) in enumerate(zip(self.players, self.score_displays)):
            display.clear()
            display.write(f"Player {i+1}: {player.get_points()}", 
                         font=("Arial", 16, "normal"))
    
    def handle_controls(self):
        for player in self.players:
            if player._SpaceCraft__controls == "arrows":
                self.screen.onkeypress(player.rotate_left, "Left")
                self.screen.onkeypress(player.rotate_right, "Right")
                self.screen.onkeypress(player.accelerate, "Up")
                self.screen.onkeypress(player.decelerate, "Down")
            else:
                self.screen.onkeypress(player.rotate_left, "a")
                self.screen.onkeypress(player.rotate_right, "d")
                self.screen.onkeypress(player.accelerate, "w")
                self.screen.onkeypress(player.decelerate, "s")
        
        self.screen.listen()
    
    def check_collisions(self):
        for player in self.players:
            for ball in self.balls[:]:
                if player.distance(ball) < 20:
                    if ball.is_gift():
                        gift = GiftBox(ball.xcor(), ball.ycor())
                        self.gift_boxes.append(gift)
                    
                    ball.respawn()
                    player.add_points(1)
                    self.update_scores()
            
            for gift in self.gift_boxes[:]:
                if player.distance(gift) < 25:
                    gift.hideturtle()
                    self.gift_boxes.remove(gift)
                    player.add_points(gift.get_points_value())
                    self.update_scores()
    
    def check_boundaries(self):
        for player in self.players:
            x, y = player.pos()
            if x > 400: player.setx(-400)
            elif x < -400: player.setx(400)
            if y > 300: player.sety(-300)
            elif y < -300: player.sety(300)
    
    def run_game(self):
        self.handle_controls()
        
        while True:
            for player in self.players:
                player.move()
            
            self.check_collisions()
            self.check_boundaries()
            self.screen.update()
            time.sleep(0.02)

if __name__ == "__main__":
    game = Game()